#!/usr/bin/env python
# coding:utf-8

import logging

from spiders.china_degrees_spider import ChinaDegreesSpider

logger = logging.getLogger('root')


def main():
    """
    主体函数
    """

    spider = ChinaDegreesSpider()
    spider.crawler()


if __name__ == '__main__':

    logging.basicConfig(filename='service.log',
                        format='%(asctime)s %(name)s %(levelname)s [line %(lineno)s]: %(message)s',
                        filemode='w',
                        level=logging.INFO)
    main()
