Nginx 安装

```bash
# 1.安装 gcc、gcc-c++
yum install -y gcc gcc-c++

# 2.安装 pcre
wget http://jaist.dl.sourceforge.net/project/pcre/pcre/8.33/pcre-8.33.tar.gz
tar -zxvf pcre-8.33.tar.gz
mv pcre-8.33/ /usr/local/pcre/
cd /usr/local/pcre/
./configure
make
make install

# 3.安装 ssl 库
wget http://www.openssl.org/source/openssl-1.0.1j.tar.gz
tar -zxvf openssl-1.0.1j.tar.gz
mv openssl-1.0.1j/ /usr/local/openssl/
cd /usr/local/openssl/
./config
make
make install

# 4.安装 zlib 库
wget http://zlib.net/zlib-1.2.11.tar.gz
tar -zxvf zlib-1.2.11.tar.gz
mv zlib-1.2.11/ /usr/local/zlib
cd /usr/local/zlib
./configure
make
make install

# 4.安装 Nginx
wget http://nginx.org/download/nginx-1.8.0.tar.gz
tar -zxvf nginx-1.8.0.tar.gz
cd nginx-1.8.0
./configure --user=nobody --group=nobody --prefix=/usr/local/nginx --with-http_stub_status_module --with-http_gzip_static_module --with-http_realip_module --with-http_sub_module --with-http_ssl_module
# 若此时报错：./configure: error: SSL modules require the OpenSSL library. 先执行下面的命令
yum -y install openssl openssl-devel
# 再次执行上面的 ./configure -- ... 命令
make
make install
```

防火墙开放 80 端口

```bash
firewall-cmd --zone=public --add-port=80/tcp --permanent
firewall-cmd --reload
```

配置开机自启动

```bash
vi /etc/rc.d/rc.local
在最后添加一行
/usr/local/nginx/sbin/nginx -c /usr/local/nginx/conf/nginx.conf

# 修改文件权限
chmod +x /etc/rc.d/rc.local
```

至此，Nginx 安装完毕

