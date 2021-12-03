create database chat;
create user chat@localhost;
grant all privileges on chat@localhost to chat.*;
create table manager(
    id int unsigned primary key auto_increment,
    login varchar(20) not null default '',
    password varchar(20) not null default ''
) engine=innodb default charset=utf8;
insert into manager(id,login,password) values(1,'user1','user1'),(2,'user2','user2');

create table messages(
    id int unsigned primary key auto_increment,
    ts timestamp not null default current_timestamp,
    manager_id int unsigned not null,
    message text,
    constraint foreign key(manager_id) references manager(id) on update cascade on delete cascade
) engine=innodb default charset=utf8;