use db_fast_api;
drop table if exists user;

create table user(
    id integer primary key auto_increment,
    username varchar(20) not null,
    auth_string varchar(200) not null,
    nick_name varchar(20),
    phone char(11),
    email varchar(30),
	city varchar(20) default '武汉',
	lat float comment '维度',
	lng float comment '经度',
	avatar varchar(100) comment '用户头像',
	active int(1) DEFAULT 0 comment '激活状态',
	unique (`username`)
);

insert into user(username, auth_string, active) VALUES
('disen', '123', 1), ('jack', '123', 0);

select id, username, auth_string, active from user;
