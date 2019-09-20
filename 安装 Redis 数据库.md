安装 Redis 数据库

```bash
# 1.下载
wget http://download.redis.io/releases/redis-4.0.9.tar.gz

# 2.解压
tar xzf redis-4.0.9.tar.gz

# 3.移动
mv ./redis-4.0.9 /usr/local/redis/  # 同时将文件夹名改为了 redis

# 4.进入 redis 目录下
cd /usr/local/redis/

# 5.编译
make

# 6.如果上一步报了cc错误，执行下面的步骤
yum -y install gcc automake autoconf libtool make

# 7.再次执行编译命令，会报错，将整个 redis 文件夹删除，重新执行 2-5 步，等编译完成后执行安装
make install

# 8.创建 /etc/redis/ 目录并将 /usr/local/redis/redis.conf 配置文件移动到该文件下
mkdir /etc/redis/
cp /usr/local/redis/redis.conf /etc/redis/

# 至此，redis 数据库安装完毕
```

配置 redis

```bash
# 1.redis 默认配置文件基本不需要进行修改
vi /etc/redis/redis.conf

# 日志文件， 要先创建日志文件，不然启动会报找不到文件
logfile "/var/log/redis/redis-server.log"
# 守护进程
daemonize yes
# 远程连接
# bind 127.0.0.1 这行注掉远程就可以连接了，也可以将远程的IP写入这里
```

开放6379端口

```bash
firewall-cmd --zone=public --add-port=6379/tcp --permanent  # 开启3306端口
firewall-cmd --reload # 重启防火墙
```

配置开机启动

```bash
# 1.将启动脚本（/usr/local/redis/utils/redis_init_script）复制一份放到 /etc/init.d/ 目录下
cp /usr/local/redis/utils/redis_init_script /etc/init.d/redis # 改名字为 redis

# 2.编辑 /etc/init.d/redis 文件，在文件头部加两行注释
# chkconfig: 2345 90 10
# description: Redis is a persistent key-value database

# 3.执行开机自启命令
chkconfig redis on
```

至此，redis 的安装和配置已经完成