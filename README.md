# jstu_Recomend
Jstu2016������ѧԺ�ƴ���Ŀǰ��
====================
3��24��ʼ
# ǰ�˽������
> ˼·��ͨ�����Ƽ�ϵͳ�Ľ����õ���ȷ��ʾϵͳ����Ƽ����������û������ޡ�ϵͳ���ԡ�ͼ�������Ĺ�����Ԫ�顱����ʽ�����û������Ż������ʹ���ں�����Դ�����С�ͬʱʹ�÷�������������߰�ȫ�ԡ�

## һ��Ŀ������˼·
### Ŀ��
���ź�̨�Ƽ�ϵͳ���ݵ��ۻ����û��ܲ���ʼ��ʹ�������м���ϵͳ�ķ����������ѯ��һϵ�л�������ʹ�ñ���Ŀ��Ҫһ��������ӵ�ǰ�ˣ������ͨ�û���רҵϵͳ֮���ì�ܡ�
### ���˼·
Django��Python�������������һ����Դģ��-��ͼ-��������MVC������WebӦ�ó����ܡ�ʹ��Django�����ǿ����ó���ļ����ṩһϵ�н�����������������ޣ�����ʽ����������ʹ���˳����AJAX�����Լ�Bootstrap��ʽ�⡣
## ����ҵ��������
���û��������װ��׼������ȥ���õ��Ƽ�ϵͳ��api���õ�JSON��ʽ�Ľ�����ٽ�����Ϊ����۲�����Ľ�����ʾ����Ϊ�û��ṩ�����ޡ�����ʹ���û��Ĳ��������ܲ��뵽�Ƽ�ϵͳ�ķ����С�
## ���������������
## 1.JSON��ʽ���ݲ���
### 1������
�������û�����Ĺؼ��ַ�װƴ�ӳɱ�׼��get�����ɷ����������Ƽ�ϵͳ�ķ������ݣ��ٱ�׼����ʽ�����ʾ��ͼ���£�

### 2�������û�����
��Ϊ����ͼ�����ݺ�����������������

```
# ������̨api����
URL="http://120.77.57.236:8080/"
# ���ݹؼ��ִμ�ͼ��/���Ķ����ȡ���
def get_by_keyword(_type,_keyword):
    if (_type=="book"):
        url=URL+"books/search?keyword="+_keyword
    elif(_type=="paper"):
        url=URL+"papers/search?keyword="+_keyword
    req=requests.get(url)
    res=json.loads(req.text)
    return res
# ͨ��ID��ȥ������ϸ��Ϣ
def get_by_id(_type,_id):
    if (_type=="book"):
        url=URL+"books/"+_id
    elif(_type=="paper"):
        url=URL+"papers/"+_id
    req=requests.get(url)
    res=json.loads(req.text)
    return res
# ͨ��ͼ���Ƽ�
def recommend__book_by_id(_type,_id):
    url=URL+"recommend/books?id="+_id+"&type="+_type
    req1=requests.get(url)
    res1=json.loads(req1.text)
    return res1
# ͨ�������Ƽ�
def recommend__paper_by_id(_type,_id):
    url=URL+"recommend/papers?id="+_id+"&type="+_type
    req2=requests.get(url)
    res2=json.loads(req2.text)
    return res2
```

### 3������JSON��ʽ����
```
[{  "id":28,
    "marcRecId":904107,
    "callId":"O13",
    "title":"�ߵ���ѧѧϰָ����ϰ�����",
    "author":"����[����]",
    "publisher":"�Ͼ���ѧ������",
    "pubYear":"2001",
    "isbn":"7-305-02062-1",
    "imageUrl":null,
    "likeCount":0,
    "disLikeCount":0
    },
    {"id":60,
    "marcRecId":908358,
    "callId":"O1-42",
    "title":"��ѧ����̽����ʵ��",
    "author":"�������",
    "publisher":"���ʳ�����",
    "pubYear":"2000",
    "isbn":"7-116-03142-1",
    "imageUrl":null,
    "likeCount":0,
    "disLikeCount":0
    },
    {"id":605,
    "paperId":"10003-2009083320.nh",
    "title":"��ѧ��ģ�ڹ�Ӧ�������е�Ӧ���о�",
    "searchWord":null,
    "source":"�廪��ѧ",
    "url":"http://wap.cnki.net/touch/web/Dissertation/Article/10003-2009083320.nh",
    "intro":"\n\n\n\n\t��ʿ���Ƽ�����DT(II)��Ʒ��ҵ���Ǽ����ڴ��¸��˵��Դ�����������������ҵ,����Ҫ�ͻ�Ϊȫ����˵�������������һ��D��˾��������漤�ҵ�ͬҵ����,�ù�˾Ϊǿ�����г�������,��ȡ���ֲ��Խ��ͳɱ���ǿ���Ʒ����������˱���˾���ٺܴ�Ŀͻ��ɱ�ת�ڵ�ѹ������κ�����֯����,���ƿ��,���������ɱ���Ϊ��˾���ٵ���Ҫ���⡣\n\n\n\n\t������������ҵ,����Ӫ���̶��Ǹ��ݿͻ����г�֮��Ҫ,������Ʒ������ԭ�ϡ��ӹ������Ʒ������Ʒ����ʽ���۸��ͻ����ṩ�ۺ�����������ӹ�����ʼ,���Ź�Ӧ����ֵ�Ļ���(ԭ���ϡ�����Ʒ�����Ʒ��
    Ʒ)���跽�ƶ�,�γ�һ������(SupplyChain)��\n\n\n\n\t������Ҫ�ӹ�Ӧ����ֵ�ĸ���������,ͨ����ѧ��ģ�ķ���,����������Ӧ���ڲ������ϵ�������ɱ�����ѧģ��,������������ģ��,����ʵ�������м���Ӧ��,�Դﵽ���ʵ�������й���ì�ܼ����������ɱ�֮Ŀ�ġ�\n\n\n\n\t������Ҫ����Ϊ�Ա���λ��Ӧ���ڲ�������״���������ռ������,�Ӷ�ȷ���Կ�漰����������Ϊ����Ŀ�ꡣͨ���������ֳ����ݽ����ռ���ɸѡ,���ÿ���������ģ��ȷ���˿ɱ�֤�����ȶ���֮���ſ��(��ȫ���);����������ϩp΢���ֵ���ѧ����,Ѱ�ҵ����������뵥������ɱ���Ķ�Ӧ��ϵ����������,�Լ����ɱ������������仯�����ϵĺ�������;���ͨ����ѧ����,�ó��������Ƴ�ˮƽ������֮��������,ʹ�������ɱ���͡�\n\n\n\n\t���,��ģ��������Ľ������ʵ�������м���Ӧ��,ʹ��������������Ч����,�����Ȳ�����,��Ч�Ľ�������������ɱ�,�ﵽ�˱�������о�Ŀ�ġ�",
    "likeCount":0,
    "disLikeCount":0}]
```

### 4����׼��JSON��ʽ���ݱ�����
��������
```
  <tr class="info" style="height:75px;">
	<td>����</td>
	<td>��Դ</td>
	<td>ID</td>
	<td><font size="2px">�ؼ���</font></td>
  </tr>
  {%for item in res_paper%}
  <tr title={{item.intro}}>
		<td><font size="2px"><a href='/recommend/?id={{item.id}}&type=paper'>{{item.title}}</a></font></td>
		<td><font size="2px">{{item.source}}</font></td>
		<td><font size="2px"><a href={{item.url}}>{{item.paperId}}</a></font></td>
		<td><font size="2px">{{item.searchWord}}</font></td>
  </tr>
{%endfor%}
```
![](http://i1.piimg.com/1949/830c7b0e00f804f4.png)

## 2.�û����޷���

### 1)����
Ϊ����û�������ֵ�����䷴�����Ƽ�ϵͳ���ڲ�Ӱ���������ʵ������ʹ����ajax�첽��Ӧ����

### 2)ҳ��ű�����
javascript
```
<script type="text/javascript">
function myFunction(ID,TYPE)
{
var xmlhttp;
if (window.XMLHttpRequest)
  {// code for IE7+, Firefox, Chrome, Opera, Safari
  xmlhttp=new XMLHttpRequest();
  }
else
  {// code for IE6, IE5
  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }
  alert("���޳ɹ���");
  
var URL="http://120.77.57.236:8080/feedback/like"+"?id="+ID+"&type="+TYPE;

xmlhttp.open("GET",URL,false);
xmlhttp.send();
}
```
html
```
<button type="button" class="btn btn-primary" onclick="myFunction({{item.id}},'book')" id="bookLike">��</button>
```

### 3)����չʾ
![Markdown](http://i2.muimg.com/1949/51a6633097b0bb3a.png)

## 3.����ҳ������

### 1)����
Ϊ���Ի�������ƣ��򻯽�������ͻ����רҵ�ԣ���Ҫ���ϲ�ѯ�����ؽ�����Ƽ������ҳ��ֱ���ʾ��

### 2)url����
```
# Django·������ƥ������
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #��ҳ
    url(r'^$', views.home, name='home'),
    #չʾ��ѯ���
    url(r'^show/$', views.show, name='show'),
    #����ͼ��/���ķ����Ƽ�
    url(r'^recommend/$', views.recommend, name='recommend'),
]
```

### 3)ҳ��չʾ
##### ��ѯ����
![Markdown](http://i1.piimg.com/1949/48ce852eb6ea8ef3.png)
##### ��ѯ���
![Markdown](http://i4.buimg.com/1949/4ac9644d640f1566.png)
##### �Ƽ����
![Markdown](http://i1.piimg.com/1949/830c7b0e00f804f4.png)

### 4)����������
uwsgi��������
```
# jstu.ini file
	[uwsgi]

	# Django-related settings

	socket = :8000

	# the base directory (full path)
	chdir           = /home/Jstu

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
```
nginx server�ļ�����
```
user www-data;
worker_processes 4;
pid /run/nginx.pid;

events {
	worker_connections 768;
	# multi_accept on;
}

http {
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
    location /static/ {
        expires 30d;
        autoindex on; 
        add_header Cache-Control private;
        alias /home/Jstu/static/;
     }
 }
```
![Markdown](http://i1.piimg.com/1949/0a96f552c041cf3e.jpg)

## �ġ��ɱ������Ϳ����Է���

## �塢��Ŀʵʩ����
### 1��Ӳ��
|���|����|����|
| --- | --- | --- |
|������|������ѧ�������˰�/1G�ڴ�/120GBӲ��|1|
|�û���|2.6��Ƶ���ϴ�����/4G�ڴ�/500GBӲ��|1|

### 2�����
|���|����|�汾|
| --- | --- | --- |
|python|��������|3.6.3|
|nginx|������������|ȫ�汾|
|django|������|1.11.10|
|bootstrap|Css��ʽ��|3.0|
��



# Ŀ¼
## �ļ���
* Jstu

	* manage.py

	* jstuLib/

		* __init__.py

		* settings.py

		* urls.py

		* wsgi.py

	* jstu.ini


>jstu.ini�ļ�����Jstu��


		 
```Python
manage.py collectstatic �ռ���̬��Դ
```

```Bash
cd /home/Jstu
uwsgi --ini jstu.ini 
```
		 
# API��ַ

	http://120.77.57.236:8080

### 2.����ʵʱ���񲿷�
#### 1��RESTful API���
ͨ�����µ�api��ȡͼ�飨book�������ģ�paper������Դ���Լ���ɷ����Ķ�����

##### ��1��ͼ�鲿��
|����|��Դ��ַ|ʾ��|
| --- | --- | --- |
|���|POST /books|POST /books|
|ɾ��|DELETE /books/{id}|DELETE /books/1|
|����|PUT /books/{id}|PUT /books/1|
|��õ���|GET /books/{id}|GET /books/1|
|��ö��|GET /books/get?page={page}&size={size}|GET /books/get?page=1&size=10|
|�ؼ��ʲ�ѯ|GET /books/search?keyword={keyword}|GET /books/search?keyword=���˼|

##### ��2�����Ĳ���
|����|��Դ��ַ|ʾ��|
| --- | --- | --- |
|���|POST /papers|POST /papers|
|ɾ��|DELETE /papers/{id}|DELETE /papers/1|
|����|PUT /papers/{id}|PUT /papers/1|
|��õ���|GET /papers/{id}|GET /papers/1|
|��ö��|GET /papers/get?page={page}&size={size}|GET /papers/get?page=1&size=10|
|�ؼ��ʲ�ѯ|GET /papers/search?keyword={keyword}|GET /papers/search?keyword=���˼|

##### ��3���Ƽ�����
|����|��Դ��ַ|ʾ��|
| --- | --- | --- |
|����ͼ��ID��ȡ�����Ƽ�|GET /recommend/papers?id={id}&type=book|GET /recommend/papers?id=1&type=book|
|��������ID��ȡ�����Ƽ�|GET /recommend/papers?id={id}&type=paper|GET /recommend/papers?id=1&type=paper|
|����ͼ��ID��ȡͼ���Ƽ�|GET /recommend/books?id={id}&type=book|GET /recommend/books?id=1&type=book|
|��������ID��ȡͼ���Ƽ�|GET /recommend/books?id={id}&type=paper|GET /recommend/books?id=1&type=paper|

##### ��4����������
|����|��Դ��ַ|ʾ��|
| --- | --- | --- |
|����ͼ��ID����ͼ��|GET /feedback/like?id={id}&type=book|GET /feedback/like?id=1&type=book|
|��������ID��������|GET /feedback/like?id={id}&type=paper|GET /feedback/like?id=1&type=paper|