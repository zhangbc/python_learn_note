#!/usr/bin/env python
# coding:utf-8


"""
中国学位与研究教育信息网-全国第四轮学科评估
@Date:         2021/11/7 19:19
@Author:       zhangbocheng
@Version:      1.0.0
@Contact:      zhangbocheng189@163.com
@Description:
"""
import logging

import requests
from pyquery import PyQuery as pq
from utils.mysqlutils import MysqlUtils

logger = logging.getLogger('ChinaDegreesSpider')


class ChinaDegreesSpider:
    """
    全国第四轮学科评估
    """

    def __init__(self):
        self.research_url = r'http://www.chinadegrees.cn/webrms/pages/Ranking/xkpgKY2016.htm'
        self.url = r'http://www.chinadegrees.cn/webrms/pages/Ranking/xkpmGXZJ2016.jsp?xkdm=01,02,03,04,05,06'
        self.discipline_url = r'http://www.chinadegrees.cn/webrms/pages/Ranking/{0}'
        self.tb_category = 'category'
        self.tb_disciplines = 'disciplines'
        self.tb_school_ranking = 'school_ranking'

    def crawler(self):
        """
        入口
        @return:
        """

        logger.info('crawler begin...')
        rs = requests.session()
        resp = rs.get(self.url)
        resp.encoding = 'GBK'
        categories, disciplines, levels = pq(resp.text).find('div.BOX>div>table>tr>td')
        # 大类解析
        categories = [(pq(item).attr('href'), item.text) for item in pq(categories).find('p>a')]
        logger.info(f'大类解析: {categories}')
        for category in categories:
            discipline_url = self.discipline_url.format(category[0])
            data_row = {'name': category[1]}
            self.save_data(self.tb_category, data_row, ['name'])
            self.crawler_disciplines(category[1], discipline_url)

        # 科研单位
        self.crawler_research_institutes()
        logger.info('crawler end.')

    def crawler_disciplines(self, discipline_name, discipline_url):
        """
        学科类
        @param discipline_name:
        @param discipline_url:
        @return:
        """

        rs = requests.session()
        resp = rs.get(discipline_url)
        resp.encoding = 'GBK'
        categories, disciplines, levels = pq(resp.text).find('div.BOX>div>table>tr>td')
        # 学科类解析
        disciplines = [(pq(item).attr('href'), item.text) for item in pq(disciplines).find('p>a')]
        logger.info(f'{discipline_name} 学科类解析: {disciplines}')
        for discipline in disciplines:
            category_url = self.discipline_url.format(discipline[0])
            self.crawler_schools(discipline_name, category_url)

    def crawler_schools(self, discipline_name, category_url):
        """
        学科排名 & 学校汇总
        egg: {'87903': ('0101', '哲学', '87903', '上海社会科学院', 'C+')}
        @param discipline_name:
        @param category_url:
        @return:
        """

        rs = requests.session()
        resp = rs.get(category_url)
        resp.encoding = 'GBK'
        categories, disciplines, levels = pq(resp.text).find('div.BOX>div>table>tr>td')
        trs = pq(levels).find('table>tr')
        category = pq(trs[0]).text()
        category_code, category_name = category.split()
        evaluate = pq(trs[1]).text()
        logger.info(f'{category} 简介: {evaluate}')
        # 存储学科信息
        data_row = {'code': category_code,
                    'name': category_name,
                    'description': evaluate,
                    'category_id': self.get_category_id(discipline_name)}
        self.save_data(self.tb_disciplines, data_row, ['code'])

        schools = pq(trs[3]).text()
        dict_schools = dict()
        level = None
        for item in schools.split(' '):
            if item[0] in ('A', 'B', 'C'):
                level = item
                continue

            level_school = item.split()
            # {'87903': ('0101', '哲学', '87903', '上海社会科学院', 'C+')}
            dict_schools[level_school[0]] = (category.split()[0],
                                             category.split()[1],
                                             level_school[0],
                                             level_school[-1],
                                             level)
            # 存储学校评级信息
            data_row = {'code': level_school[0],
                        'name': level_school[-1],
                        'dis_code': category_code,
                        'dis_name': category_name,
                        'ranking': level}
            self.save_data(self.tb_school_ranking, data_row, ['code', 'dis_code'])
        logger.info(f'total schools: {len(dict_schools)}')
        logger.info(dict_schools)

    def crawler_research_institutes(self):
        """
        科研单位
        egg: {'0101-87903': ('0101', '哲学', '87903', '上海社会科学院', 'C+')}
        @return:
        """

        rs = requests.session()
        resp = rs.get(self.research_url)
        resp.encoding = 'GBK'
        content = pq(resp.text).find('div>div>table')
        evaluate = pq(content).find('tr>td').eq(0).text()
        logger.info(f'科研机构 简介: {evaluate}')
        data_list = pq(content).find('tr').eq(2).text().split()
        dict_schools = dict()
        discipline_code, discipline_name = None, None
        index = 0
        while index < len(data_list):
            if len(data_list[index]) == 4:
                discipline_code = data_list[index]
                discipline_name = data_list[index + 1]
                index += 3

            dict_schools[f'{discipline_code}-{data_list[index]}'] = (discipline_code,
                                                                     discipline_name,
                                                                     data_list[index],
                                                                     data_list[index + 1],
                                                                     data_list[index + 2])
            # 存储学校评级信息
            data_row = {'code': data_list[index],
                        'name': data_list[index + 1],
                        'dis_code': discipline_code,
                        'dis_name': discipline_name,
                        'ranking': data_list[index + 2]}
            self.save_data(self.tb_school_ranking, data_row, ['code', 'dis_code'])
            index += 3

        logger.info(f'total schools: {len(dict_schools)}')
        logger.info(dict_schools)

    @staticmethod
    def save_data(table: str, data_row: dict, primary_columns: list):
        """

        @param table:
        @param primary_columns:
        @param data_row:
        @return:
        """

        if not primary_columns:
            logger.error('please check primary keys!')
            return

        columns = ','.join(data_row.keys())
        values = ','.join(['%s'] * len(data_row))
        row = list(data_row.values())
        condition = ''
        for idx, column in enumerate(primary_columns):
            condition += f'{column}=%s'
            row.append(data_row[column])
            if idx < len(primary_columns) - 1:
                condition += ' and '

        update_query = f'''INSERT INTO {table}({columns}) VALUES({values}) ON DUPLICATE KEY UPDATE {condition};'''

        conn = MysqlUtils.connect()
        cursor = conn.cursor()
        cursor.execute(update_query, row)
        if cursor:
            cursor.close()

        conn.commit()
        conn.close()

    def get_category_id(self, discipline_name):
        """
        获取学科学科类别ID
        @param discipline_name:
        @return:
        """

        conn = MysqlUtils.connect()
        cursor = MysqlUtils.column_select(conn=conn, table=self.tb_category, column='name', value=discipline_name)
        idx = None
        if cursor:
            idx = cursor.fetchone()[0]
            cursor.close()
        conn.close()
        return idx


if __name__ == '__main__':

    spider = ChinaDegreesSpider()
    spider.crawler()
    spider.crawler_research_institutes()
