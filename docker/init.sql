-- init.sql
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '123' WITH GRANT OPTION;
CREATE USER 'crm'@'%' IDENTIFIED BY '';
GRANT ALL PRIVILEGES ON crm.* TO 'crm'@'%' WITH GRANT OPTION;
#GRANT ALL PRIVILEGES ON svcms.* TO 'svcms'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;