use db_spiders;

show table status;

drop table if exists `category`;

create table category (
    id integer primary key auto_increment comment '自增标识',
    name varchar(20) not null unique key comment '名称')
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='学科类别';

drop table if exists `disciplines`;

create table disciplines (
    id integer primary key auto_increment comment '自增标识',
    code varchar(20) not null unique key comment '学科代码',
    name varchar(20) comment '学科名称',
    description text comment '描述',
    category_id int comment '学科类别'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='学科详情';

drop table if exists `school_ranking`;

create table school_ranking (
    id integer primary key auto_increment comment '自增标识',
    code varchar(20) not null comment '学校代码',
    name varchar(50) not null comment '学校名称',
    dis_code varchar(20) not null comment '学科代码',
    dis_name varchar(20) comment '学科名称',
    ranking varchar(4) comment '评级',
    unique key uniq_codes(`code`, `dis_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='学校学科评级详情';


select * from category;
