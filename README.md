# LostAndFoundServiceV2
LostAndFoundService ECNU校园失物招领服务端V2 重构版   
主要是为了传承，老学长毕业了，写个详细的文档。   

V1 repo : [LostFoundDjangoService](https://github.com/Above-The-Cloud/LostFoundDjangoService)

[TOC]   

目录：   
1.服务介绍   
2.部署流程   
3.上线流程   
   
### 1.服务介绍   
* [x] 用户服务[user](./user/README.md)   
* [x] 动态服务[dynamic](./dynamic/README.md)    
* [ ] 上传服务[upload](./upload/README.md)   
* [ ] 通知服务notify   

### 2.部署流程
#### 2.1安装依赖: 
```
pip install -r requirements.txt
```

安装Nginx, uwsgi, mysql
```shell script
apt install nginx uwsgi mysql-server
```

设置mysql utf-8编码   
>输入下面的命令，打开第一个配置文件
>```
>vim /etc/mysql/conf.d/mysql.cnf
>```
>在 [mysql] 标签的下一行添加下面的配置
>```
>default-character-set=utf8
>```
>输入下面的命令，打开第二个配置文件
>```
>vim /etc/mysql/mysql.conf.d/mysqld.cnf
>```
>找到 [mysqld] 标签，在其下一行添加下面的配置
>```
>character-set-server=utf8
>```
>配置文件修改成功之后，输入下面的命令重启mysql服务
>```
>service mysql restart
>```
>重启之后再去查看数据库的默认编码方式
>```
>show variables like '%character%';
>```
>
>```
>mysql> show variables like '%character%';
>+--------------------------+----------------------------+
>| Variable_name            | Value                      |
>+--------------------------+----------------------------+
>| character_set_client     | utf8                       |
>| character_set_connection | utf8                       |
>| character_set_database   | utf8                       |
>| character_set_filesystem | binary                     |
>| character_set_results    | utf8                       |
>| character_set_server     | utf8                       |
>| character_set_system     | utf8                       |
>| character_sets_dir       | /usr/share/mysql/charsets/ |
>+--------------------------+----------------------------+
>```
创建数据库并设置数据库编码
```
CREATE DATABASE dbname DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
```
#### 2.2新建微服务
```shell script
python manage.py startapp service
```
在service文件夹下创建urls.py(设置路由)   
在models.py对数据库进行设计
在views.py里写好接口，基本的增删改查（create,delete,update,list），遵循django ORM   
将models的改动同步到数据库   
```shell script
python manage.py makemigrations
python manage.py migrate
```
运行调试(仅调试，上线请勿用此方法)
```shell script
python manage.py runserver {IP}:{PORT}
```

### 3.上线流程
需要Nginx，uwsgi支持

