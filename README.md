# jstu_Recomend
Jstu2016��ƴ���Ŀǰ��
====================
3��24��ʼ
--------------
		�ǳ���ª
		���
		��л����Ԭ��ĺ�̨���������ݣ��������ֻ�Ǹ��տ�

# ����
```Bash
sudo apt-get -y install python3 python3-pip nginx
sudo pip3 install django uwsgi
```
## �ļ���
* Jstu

	* manage.py

	* jstuLib/

		* __init__.py

		* settings.py

		* urls.py

		* wsgi.py

	* jstu.ini

#### uwsgi����
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
		
>jstu.ini�ļ�����Jstu��

#### nginx server����	
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
manage.py collectstatic �ռ���̬��Դ
```

```Bash
cd /home/Jstu
uwsgi --ini jstu.ini 
```
		 
# API��ַ
http://120.77.57.236:8080
# RESTful API���
>ͨ�����µ�api��ȡͼ�飨book�������ģ�paper������Դ��

## 1.ͼ�鲿��
|����|��Դ��ַ|ʾ��|
| --- | --- | --- |
|���|POST /books|POST /books|
|ɾ��|DELETE /books/{id}|DELETE /books/1|
|����|PUT /books/{id}|PUT /books/1|
|��õ���|GET /books/{id}|GET /books/1|
|��ö��|GET /books/get?page={page}&size={size}|GET /books/get?page=1&size=10|
|�ؼ��ʲ�ѯ|GET /books/search?keyword={keyword}|GET /books/search?keyword=���˼|

## 2.���Ĳ���
|����|��Դ��ַ|ʾ��|
| --- | --- | --- |
|���|POST /papers|POST /papers|
|ɾ��|DELETE /papers/{id}|DELETE /papers/1|
|����|PUT /papers/{id}|PUT /papers/1|
|��õ���|GET /papers/{id}|GET /papers/1|
|��ö��|GET /papers/get?page={page}&size={size}|GET /papers/get?page=1&size=10|
|�ؼ��ʲ�ѯ|GET /papers/search?keyword={keyword}|GET /papers/search?keyword=���˼|

## 3.�Ƽ�����
|����|��Դ��ַ|ʾ��|
| --- | --- | --- |
|����ͼ��ID��ȡ�����Ƽ�|GET /recommend/papers?id={id}&type=book|GET /recommend/papers?id=1&type=book|
|��������ID��ȡ�����Ƽ�|GET /recommend/papers?id={id}&type=paper|GET /recommend/papers?id=1&type=paper|
|����ͼ��ID��ȡͼ���Ƽ�|GET /recommend/books?id={id}&type=book|GET /recommend/books?id=1&type=book|
|��������ID��ȡͼ���Ƽ�|GET /recommend/books?id={id}&type=paper|GET /recommend/books?id=1&type=paper|