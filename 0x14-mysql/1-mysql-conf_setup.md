# [How to] check if server configurations are working properly

Create a user and password for both MySQL databases which will allow the
checker access to them.
* Create USER
* GRANT Replication access permissions
```
cat mysql_setup_conf.sql | sudo mysql
```
