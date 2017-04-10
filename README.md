# jstu_Recomend
Jstu2016年计算机学院科创项目前端
====================
3月24日始
# 前端解决方案
> 思路：通过对推荐系统的交互访的正确显示系统里的推荐结果，设计用户“点赞”系统，以“图书与论文关联三元组”的形式，用用户反馈优化结果，使得在后续资源检索中。同时使用反向代理服务器提高安全性。

## 一、目标与解决思路
### 目标
随着后台推荐系统数据的累积，用户总不能始终使用命令行监视系统的返回数据与查询等一系列互动，这使得本项目需要一个合理可视的前端，解决普通用户与专业系统之间的矛盾。
### 解决思路
Django是Python编程语言驱动的一个开源模型-视图-控制器（MVC）风格的Web应用程序框架。使用Django，我们可以用成熟的技术提供一系列解决方案。因人手有限，在样式，交互方面使用了成熟的AJAX技术以及Bootstrap样式库。
## 二、业务解决方案
对用户的请求包装标准化发送去调用到推荐系统的api，得到JSON格式的结果后再将其拆封为方便观察操作的界面显示，且为用户提供“点赞”功能使得用户的操作数据能参与到推荐系统的分析中。
## 三、技术解决方案
## 1.JSON格式数据部分
### 1）概述
将来自用户请求的关键字封装拼接成标准的get请求，由服务器接收推荐系统的返回数据，再标准化格式输出，示意图如下：

### 2）处理用户请求
分为请求图书数据和请求论文数据两种

```
# 分析后台api设置
URL="http://120.77.57.236:8080/"
# 根据关键字次及图书/论文对象获取结果
def get_by_keyword(_type,_keyword):
    if (_type=="book"):
        url=URL+"books/search?keyword="+_keyword
    elif(_type=="paper"):
        url=URL+"papers/search?keyword="+_keyword
    req=requests.get(url)
    res=json.loads(req.text)
    return res
# 通过ID过去单个详细信息
def get_by_id(_type,_id):
    if (_type=="book"):
        url=URL+"books/"+_id
    elif(_type=="paper"):
        url=URL+"papers/"+_id
    req=requests.get(url)
    res=json.loads(req.text)
    return res
# 通过图书推荐
def recommend__book_by_id(_type,_id):
    url=URL+"recommend/books?id="+_id+"&type="+_type
    req1=requests.get(url)
    res1=json.loads(req1.text)
    return res1
# 通过论文推荐
def recommend__paper_by_id(_type,_id):
    url=URL+"recommend/papers?id="+_id+"&type="+_type
    req2=requests.get(url)
    res2=json.loads(req2.text)
    return res2
```

### 3）接受JSON格式数据
```
[{  "id":28,
    "marcRecId":904107,
    "callId":"O13",
    "title":"高等数学学习指导与习题解析",
    "author":"陈仲[编著]",
    "publisher":"南京大学出版社",
    "pubYear":"2001",
    "isbn":"7-305-02062-1",
    "imageUrl":null,
    "likeCount":0,
    "disLikeCount":0
    },
    {"id":60,
    "marcRecId":908358,
    "callId":"O1-42",
    "title":"数学教育探索与实践",
    "author":"主编杨春宏",
    "publisher":"地质出版社",
    "pubYear":"2000",
    "isbn":"7-116-03142-1",
    "imageUrl":null,
    "likeCount":0,
    "disLikeCount":0
    },
    {"id":605,
    "paperId":"10003-2009083320.nh",
    "title":"数学建模在供应链管理中的应用研究",
    "searchWord":null,
    "source":"清华大学",
    "url":"http://wap.cnki.net/touch/web/Dissertation/Article/10003-2009083320.nh",
    "intro":"\n\n\n\n\t富士康科技集团DT(II)产品事业处是集团内从事个人电脑代工生产的制造型企业,其主要客户为全球个人电脑销量排名第一的D公司。面对日益激烈的同业竞争,该公司为强化其市场竞争力,采取多种策略降低成本增强其产品竞争力。因此本公司面临很大的客户成本转稼的压力。如何合理组织生产,控制库存,降低生产成本成为公司面临的首要问题。\n\n\n\n\t对于制造型企业,其运营过程都是根据客户或市场之需要,开发产品、购进原料、加工制造产品、以商品的形式销售给客户、提供售后服务。制造对象从供方开始,沿着供应链增值的环节(原材料→在制品→半成品→
    品)向需方移动,形成一条长链(SupplyChain)。\n\n\n\n\t本文主要从供应链增值的各环节着手,通过数学建模的方法,建立描述供应链内部供需关系和生产成本的数学模型,进而分析求解该模型,并在实际生产中加以应用,以达到解决实际生产中供需矛盾及降低生产成本之目的。\n\n\n\n\t本文主要内容为对本单位供应链内部运作现状进行数据收集与分析,从而确定以库存及生产批量做为改善目标。通过对生产现场数据进行收集与筛选,采用库存管理理论模型确定了可保证生产稳定性之最优库存(安全库存);采用曲线拟合﹑微积分等数学工具,寻找到生产批量与单件制造成本间的对应关系及特征函数,以及库存成本随生产批量变化所符合的函数规律;最后通过数学运算,得出了现有制程水平下最优之生产批量,使得生产成本最低。\n\n\n\n\t最后,将模型所求出的结果导入实际生产中加以应用,使得生产线连续高效运行,产能稳步提升,有效的降低了生产制造成本,达到了本课题的研究目的。",
    "likeCount":0,
    "disLikeCount":0}]
```

### 4）标准化JSON格式数据表格输出
大致如下
```
  <tr class="info" style="height:75px;">
	<td>标题</td>
	<td>来源</td>
	<td>ID</td>
	<td><font size="2px">关键词</font></td>
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

## 2.用户点赞反馈

### 1)概述
为提高用户交互价值并将其反馈入推荐系统，在不影响正常访问的情况下使用了ajax异步响应技术

### 2)页面脚本设置
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
  alert("点赞成功！");
  
var URL="http://120.77.57.236:8080/feedback/like"+"?id="+ID+"&type="+TYPE;

xmlhttp.open("GET",URL,false);
xmlhttp.send();
}
```
html
```
<button type="button" class="btn btn-primary" onclick="myFunction({{item.id}},'book')" id="bookLike">赞</button>
```

### 3)交互展示
![Markdown](http://i2.muimg.com/1949/51a6633097b0bb3a.png)

## 3.整体页面整合

### 1)概述
为人性化界面设计，简化界面内容突出其专业性，需要整合查询，返回结果，推荐结果的页面分别显示。

### 2)url设置
```
# Django路由正则匹配设置
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #主页
    url(r'^$', views.home, name='home'),
    #展示查询结果
    url(r'^show/$', views.show, name='show'),
    #根据图书/论文返回推荐
    url(r'^recommend/$', views.recommend, name='recommend'),
]
```

### 3)页面展示
##### 查询界面
![Markdown](http://i1.piimg.com/1949/48ce852eb6ea8ef3.png)
##### 查询结果
![Markdown](http://i4.buimg.com/1949/4ac9644d640f1566.png)
##### 推荐结果
![Markdown](http://i1.piimg.com/1949/830c7b0e00f804f4.png)

### 4)服务器设置
uwsgi服务设置
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
nginx server文件设置
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

## 四、成本分析和可行性分析

## 五、项目实施方案
### 1）硬件
|类别|详情|数量|
| --- | --- | --- |
|服务器|阿里云学生机单核版/1G内存/120GB硬盘|1|
|用户端|2.6主频以上处理器/4G内存/500GB硬盘|1|

### 2）软件
|类别|详情|版本|
| --- | --- | --- |
|python|开发环境|3.6.3|
|nginx|反向代理服务器|全版本|
|django|服务框架|1.11.10|
|bootstrap|Css样式库|3.0|
。



# 目录
## 文件夹
* Jstu

	* manage.py

	* jstuLib/

		* __init__.py

		* settings.py

		* urls.py

		* wsgi.py

	* jstu.ini


>jstu.ini文件放于Jstu下


		 
```Python
manage.py collectstatic 收集静态资源
```

```Bash
cd /home/Jstu
uwsgi --ini jstu.ini 
```
		 
# API地址

	http://120.77.57.236:8080

### 2.数据实时服务部分
#### 1）RESTful API设计
通过以下的api存取图书（book）、论文（paper）等资源，以及完成反馈的动作。

##### （1）图书部分
|功能|资源地址|示例|
| --- | --- | --- |
|添加|POST /books|POST /books|
|删除|DELETE /books/{id}|DELETE /books/1|
|更新|PUT /books/{id}|PUT /books/1|
|获得单个|GET /books/{id}|GET /books/1|
|获得多个|GET /books/get?page={page}&size={size}|GET /books/get?page=1&size=10|
|关键词查询|GET /books/search?keyword={keyword}|GET /books/search?keyword=马克思|

##### （2）论文部分
|功能|资源地址|示例|
| --- | --- | --- |
|添加|POST /papers|POST /papers|
|删除|DELETE /papers/{id}|DELETE /papers/1|
|更新|PUT /papers/{id}|PUT /papers/1|
|获得单个|GET /papers/{id}|GET /papers/1|
|获得多个|GET /papers/get?page={page}&size={size}|GET /papers/get?page=1&size=10|
|关键词查询|GET /papers/search?keyword={keyword}|GET /papers/search?keyword=马克思|

##### （3）推荐部分
|功能|资源地址|示例|
| --- | --- | --- |
|根据图书ID获取论文推荐|GET /recommend/papers?id={id}&type=book|GET /recommend/papers?id=1&type=book|
|根据论文ID获取论文推荐|GET /recommend/papers?id={id}&type=paper|GET /recommend/papers?id=1&type=paper|
|根据图书ID获取图书推荐|GET /recommend/books?id={id}&type=book|GET /recommend/books?id=1&type=book|
|根据论文ID获取图书推荐|GET /recommend/books?id={id}&type=paper|GET /recommend/books?id=1&type=paper|

##### （4）反馈部分
|功能|资源地址|示例|
| --- | --- | --- |
|根据图书ID点赞图书|GET /feedback/like?id={id}&type=book|GET /feedback/like?id=1&type=book|
|根据论文ID点赞论文|GET /feedback/like?id={id}&type=paper|GET /feedback/like?id=1&type=paper|