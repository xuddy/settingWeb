安装 MySQL

```bash
# 1.安装 wget
yum -y install wget

# 2.下载并安装MySQL官方的Yum Repository
wget -i -c http://dev.mysql.com/get/mysql57-community-release-el7-10.noarch.rpm

# 3.安装MySQL服务器
yum -y install mysql-community-server

# 此时出现异常：网卡 ip 又没有了，不要慌，重启网络服务就解决了。
```

配置 MySQL

```bash
# 1. systemctl start mysqld.service 启动 mysql 时报没有找到 mysql，改用service mysqld start 启动显示重定向到 /bin/systemctl start mysqld.service ，这时却启动成功了
service mysqld start

# 2.查看MySQL运行状态，以确保服务已启动
systemctl status mysqld.service

# 3.找出 root 密码
grep "password" /var/log/mysqld.log

# 4.登录 MySQL
mysql -uroot -p

# 5.输入密码后登录成功，但此时还不能操作 mysql ，要修改密码
ALTER USER 'root'@'localhost' IDENTIFIED BY 'mysql';

# 6.上述命令尝试将 root 用户的密码改为 mysql ，但是失败了，因为密码太简单了，查看初始的密码规则
show variables like 'validate_password';

# 7.通过以下命令修改（不建议修改，会降低安全程度）
set global validate_password_policy=0;  # 密码验证级别
set global validate_password_length=1;  # 密码最小长度

# 8.重设密码
ALTER USER 'root'@'localhost' IDENTIFIED BY 'mysql';

# 9.卸载Yum Repository（非必需，但不卸载每次使用yum就会更新）
yum -y remove mysql57-community-release-el7-10.noarch

# 10.经过上述步骤后 MySQL 数据库就安装配置完成了，不过只能在本地使用，远程连接并没有开启。
```

修改远程连接权限

```bash
# 1.查看 mysql 中用户能从哪些主机登录
use mysql;
select user, host from user;

# 新增用户
create user 'test'@'localhost' identified by '123'; # 只能从本地登录
create user 'test'@'192.168.7.22' identified by '123'; # 从指定ip登录
create user 'test'@'%' identified by '123';  # 可以从外网登录

# 删除用户
格式：drop user 'username'@'host';

# 授权
# myuser使用mypassword从任何主机连接到mysql服务器
GRANT ALL PRIVILEGES ON *.* TO 'myuser'@'%' IDENTIFIED BY 'mypassword' WITH GRANT OPTION;
# 用户myuser从ip为192.168.1.6的主机连接到mysql服务器，并使用mypassword作为密码
GRANT ALL PRIVILEGES ON *.* TO 'myuser'@'192.168.1.3' IDENTIFIED BY 'mypassword' WITH GRANT OPTION;
# 用户myuser从ip为192.168.1.6的主机连接到mysql服务器的dk数据库，并使用mypassword作为密码
GRANT ALL PRIVILEGES ON dk.* TO 'myuser'@'192.168.1.3' IDENTIFIED BY 'mypassword' WITH GRANT OPTION;

# 刷新权限
FLUSH PRIVILEGES;

# 仍然连不上，报 10060 错误，可能是防火墙配置的问题
systemctl status firewalld  # 查看防火墙状态
firewall-cmd --zone=public --add-port=3306/tcp --permanent  # 开启3306端口
firewall-cmd --reload # 重启防火墙

# 到这里在本机的 shell 窗口中能连接到虚拟机中的 mysql 了
```

配置 MySQL 支持中文字符集

```bash
# 1.修改 /etc/my.cnf 文件，添加如下内容：
# 在开头（未确定是否必须）添加：
[client]
default-character-set=utf8
# 在 socket 配置项后（未确定是否必须）添加：
character-set-server=utf8
collation-server=utf8_general_ci

# 2.重启 MySQL
service mysqld restart

至此，MySQL 的安装和常规配置已经全部配置完，虚拟机中的 mysql 数据库已经具备了基本的使用功能
```

