-- 达梦线上实验室学习笔记DM8：https://eco.dameng.com/tour/
-- 用户权限，操作数据表，检索数据，创建索引，事务特性

-- 检查数据库版本
select * from v$version;

-- 检查服务状态
select status$ from v$instance;

-- 创建用户
create user dm identified by "administrator12300";

-- 授权用户
grant resource to dm;

grant select on dmhr.employee to dm;

select * from dba_users where username='DM';

-- 创建数据库
CREATE SCHEMA DMHR AUTHORIZATION "SYSDBA";


-- 创建表
create table DMHR.employee(
	employee_id integer,
	employee_name varchar(20) not null,
	hire_date date,
	salary integer,
	department_id integer not null
);

create table DMHR.department(
	department_id integer primary key,
	department_name varchar(30) not null
);

-- 切换用户
-- conn dm/administrator12300;

-- 添加非空约束
alter table DMHR.employee modify(hire_date not null);


-- 添加主键约束
alter table DMHR.employee add constraint pk_emp_id primary key(employee_id);

-- 添加外键约束
alter table DMHR.employee add constraint fk_dept_id
foreign key(department_id) references DMHR.department(department_id);


-- 查看表结构
-- DESC DMHR.employee;

-- 查看表主键外键
select * from all_constraints where owner='DMHR' and table_name='EMPLOYEE';

-- 插入数据
insert into DMHR.department values(1, '数据库产品中心');
insert into DMHR.employee values(1,'王达梦','2008-05-30 00:00:00', 30000, 1);
commit;

-- 修改数据
update DMHR.employee set salary=35000 where employee_id=1;
commit;

select * from DMHR.employee;

-- 删除数据
delete from DMHR.employee where employee_id=1;
delete from DMHR.department;
commit;

select * from DMHR.employee;

-- 批量插入数据
create table DMHR.t1 as
select rownum as id, trunc(dbms_random.value(0, 100)) as random_id,
dbms_random.string('x', 20) as random_string from dual connect by level <= 100000;

select count(*) from DMHR.t1;

-- 排序数据
select * FROM DMHR.T1 WHERE ROWNUM < 5 order by id desc;

-- 验证分组查询
insert into DMHR.department values(1, '数据库研发中心');
insert into DMHR.department values(2, '数据库产品部');
insert into DMHR.department values(3, '数据库运营中心');
insert into DMHR.department values(4, '数据库销售中心');
insert into DMHR.employee values(1,'王达梦','2008-05-30 00:00:00', 30000, 1);
insert into DMHR.employee values(2,'张达梦','2008-05-30 00:00:00', 30000, 2);
insert into DMHR.employee values(3,'章达梦','2008-05-30 00:00:00', 30000, 3);
insert into DMHR.employee values(4,'李达梦','2008-05-30 00:00:00', 30000, 1);
insert into DMHR.employee values(5,'符达梦','2008-05-30 00:00:00', 30000, 2);
insert into DMHR.employee values(6,'黄达梦','2008-05-30 00:00:00', 30000, 3);
insert into DMHR.employee values(7,'牛达梦','2008-05-30 00:00:00', 30000, 4);
commit;

select * from DMHR.department;
select * from  DMHR.employee;

select dept.department_name as 部门, count(*) as 人数
from DMHR.EMPLOYEE emp, DMHR.DEPARTMENT dept
where emp.DEPARTMENT_ID = dept.DEPARTMENT_ID
group by dept.DEPARTMENT_NAME having count(*) > 1;

-- 创建视图
create or replace view DMHR.v1 as
select dept.department_name, emp.employee_name, emp.salary, emp.hire_date
from DMHR.EMPLOYEE emp, DMHR.DEPARTMENT dept
where emp.SALARY > 10000 and emp.HIRE_DATE >='2013-08-01'
and emp.DEPARTMENT_ID = dept.DEPARTMENT_ID;

update DMHR.employee set hire_date = '2018-05-30 00:00:00' where EMPLOYEE_ID=7;
commit;

-- 查询视图
select * from DMHR.V1 where V1.HIRE_DATE > '2018-08-01';

-- 创建索引
create index DMHR.idx_emp_salary on DMHR.EMPLOYEE(SALARY);

-- 查看索引
select table_name, index_name, index_type from user_indexes where index_name='IDX_EMP_SALARY';

-- 删除索引
drop INDEX DMHR.idx_emp_salary;

-- 插入数据并创建保存点
insert into DMHR.employee values(8,'罗小刚','2020-05-30 00:00:00', 30500, 1);
savepoint my_insert;

select * from DMHR.employee;
update DMHR.employee set department_id=2 where employee_id=8;
select * from DMHR.employee where EMPLOYEE_ID=8;

-- 回滚到保存点
rollback to my_insert;
select * from DMHR.employee where EMPLOYEE_ID=8;

-- 创建序列
create SEQUENCE DMHR.SEQ1
start with 1 increment by 1 maxvalue 10000 cache 5 nocycle;

-- 查询下一个序列号
select DMHR.SEQ1.nextval() from dual;

-- 查询当前序列号
select DMHR.SEQ1.currval() from dual;

-- 定义物化视图
create materialized view DMHR.mv1 build IMMEDIATE REFRESH COMPLETE ON COMMIT AS
select department_id as 部门编号, count(*) as 人数
from DMHR.EMPLOYEE group by department_id;

select * from DMHR.MV1 WHERE 部门编号=1;

insert into DMHR.employee values(9,'苏林','2021-05-30 00:00:00', 30500, 1);
commit;

select * from DMHR.MV1 WHERE 部门编号=1;

-- 创建函数
create or replace function DMHR.random_password (pass_len in number) return varchar2 as pwd varchar(128);
begin pwd = dbms_random.string('x', pass_len);
return pwd;
end;

-- 调用函数生成随机数
select DMHR.RANDOM_PASSWORD(12) from dual;

-- 创建存储过程
select employee_id, employee_name, salary from DMHR.EMPLOYEE
where department_id=1 and hire_date >= to_date('2012-03-01 00:00:00', 'yyyy-mm-dd hh24:mi:ss');

create or replace PROCEDURE DMHR.proc(dept_in DMHR.employee.department_id%type, hire_in VARCHAR2(24))
as CURSOR by_dept_cur is
select * from DMHR.EMPLOYEE where department_id=dept_in;
begin for rec in by_dept_cur
loop
if rec.hire_date > to_date(hire_in, 'yyyy-mm-dd hh24:mi:ss')
then
update DMHR.EMPLOYEE set salary = salary * 1.15 where employee_id=rec.employee_id;
end if;
end loop;
commit;
end;

-- 调用存储过程
begin DMHR.proc(1,'2012-03-01 00:00:00');
end;

select employee_id, employee_name, salary from DMHR.EMPLOYEE
where department_id=1 and hire_date >= to_date('2012-03-01 00:00:00', 'yyyy-mm-dd hh24:mi:ss');

-- 创建表级触发器
create table DMHR.trg(name_old VARCHAR, name_new VARCHAR);

create or replace TRIGGER DMHR.trg1
before
update of employee_name on DMHR.employee
for each row
declare
begin
insert into DMHR.trg VALUES(:old.employee_name, :new.employee_name);
end;

update DMHR.employee set employee_name='达梦' where employee_id=1;
commit;

select * from DMHR.trg;

-- 删除触发器
drop TRIGGER DMHR.trg1;

-- 创建间隔分区表
create table DMHR.emp_part(
  employee_id int PRIMARY KEY,
  employee_name varchar(20),
  indentity_card varchar(18),
  email varchar(50) not null,
  phone varchar(20),
  hire_date date not null,
  job_id varchar(10) not null,
  salary float,
  commission_pct int,
  manager_id int,
  department_id int
) PARTITION BY RANGE(hire_date)
interval(numtoyminterval(1, 'year'))(
  PARTITION p_before_2015 VALUES less than (to_date('2015-01-01', 'yyyy-mm-dd'))
) STORAGE(
  fillfactor 85,
  branch(32,32)
);


insert into DMHR.emp_part(employee_id, employee_name, email, hire_date, job_id, department_id) values
(1,'苏林1','sul1@os-easy.com','2013-05-30 00:00:00', 1, 1),
(2,'苏林2','sul2@os-easy.com','2014-05-30 00:00:00', 1, 2),
(3,'苏林3','sul3@os-easy.com','2019-05-30 00:00:00', 1, 3);
commit;

select * from DMHR.emp_part;

-- 查看分区信息
select table_name, partition_name, high_value from user_tab_partitions
where table_name='EMP_PART' order by high_value;


-- 检索某个分区数据
select * from DMHR.emp_part PARTITION(P_BEFORE_2015);


INSERT INTO emp_part(employee_id, employee_name, indentity_card, email,
     phone, hire_date, job_id, salary, commission_pct, manager_id, department_id)
     VALUES(10,'武达梦','340102196202303999','wudm@dameng.com','15312348566',
     '2021-05-30','11',50000.00,0,1,1);
commit;

-- with子句
with FUNCTION get_salary(emp_id int) RETURN int AS
declare
sal int;
BEGIN
select salary into sal from DMHR.EMPLOYEE where employee_id=emp_id;
return sal;
end;

select get_salary(1) from dual;


-- with as 子句
with t as(
select max(hire_date) max_hd, min(hire_date) min_hd from DMHR.EMPLOYEE)
select employee_id, employee_name, hire_date from DMHR.EMPLOYEE
where hire_date in (
select t.max_hd from t UNION ALL select t.min_hd from t
);
