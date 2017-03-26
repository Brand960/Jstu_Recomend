# jstu_Recomend
Jstu2016年科创项目前端
====================
3月24日始
--------------
		非常简陋
		真的
		感谢大佬袁臻的后台（分析数据），我这边只是个空壳

# 部署
```Bash
sudo apt-get -y install python3 python3-pip nginx
sudo pip3 install django uwsgi
```
## 文件夹
* Jstu

	* manage.py

	* jstuLib/

		* __init__.py

		* settings.py

		* urls.py

		* wsgi.py

	* jstu.ini

#### uwsgi设置
		# jstu.ini file
		[uwsgi]

		# Django-related settings

		socket = :8000

		# the base directory (full path)
		chdir           = /home/jstu

		# Django s wsgi file
		module          = jstuLib.wsgi

		# process-related settings
		# master
		master          = true

		# maximum number of worker processes
		processes       = 4

		# ... with appropriate permissions - may be needed
		# chmod-socket    = 664
		# clear environment on exit
		vacuum          = true
		
>jstu.ini文件放于Jstu下

#### nginx server设置	
		server {
			listen         8099; 
			server_name    127.0.0.1 
			charset UTF-8;
			access_log      /var/log/nginx/myweb_access.log;
			error_log       /var/log/nginx/myweb_error.log;

			client_max_body_size 75M;

			location / { 
				include uwsgi_params;
				uwsgi_pass 127.0.0.1:8000;
				uwsgi_read_timeout 2;
			}   
			location /static {
				expires 30d;
				autoindex on; 
				add_header Cache-Control private;
				alias /home/Jstu/static/;
			 }
		 }
		 
```Python
manage.py collectstatic 收集静态资源
```

```Bash
cd /home/Jstu
uwsgi --ini jstu.ini 
```
		 
# API地址
http://120.77.57.236:8080
# RESTful API设计
>通过以下的api存取图书（book）、论文（paper）等资源。

## 1.图书部分
|功能|资源地址|示例|
| --- | --- | --- |
|添加|POST /books|POST /books|
|删除|DELETE /books/{id}|DELETE /books/1|
|更新|PUT /books/{id}|PUT /books/1|
|获得单个|GET /books/{id}|GET /books/1|
|获得多个|GET /books/get?page={page}&size={size}|GET /books/get?page=1&size=10|
|关键词查询|GET /books/search?keyword={keyword}|GET /books/search?keyword=马克思|

## 2.论文部分
|功能|资源地址|示例|
| --- | --- | --- |
|添加|POST /papers|POST /papers|
|删除|DELETE /papers/{id}|DELETE /papers/1|
|更新|PUT /papers/{id}|PUT /papers/1|
|获得单个|GET /papers/{id}|GET /papers/1|
|获得多个|GET /papers/get?page={page}&size={size}|GET /papers/get?page=1&size=10|
|关键词查询|GET /papers/search?keyword={keyword}|GET /papers/search?keyword=马克思|

## 3.推荐部分
|功能|资源地址|示例|
| --- | --- | --- |
|根据图书ID获取论文推荐|GET /recommend/papers?id={id}&type=book|GET /recommend/papers?id=1&type=book|
|根据论文ID获取论文推荐|GET /recommend/papers?id={id}&type=paper|GET /recommend/papers?id=1&type=paper|
|根据图书ID获取图书推荐|GET /recommend/books?id={id}&type=book|GET /recommend/books?id=1&type=book|
|根据论文ID获取图书推荐|GET /recommend/books?id={id}&type=paper|GET /recommend/books?id=1&type=paper|