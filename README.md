# jstu_Recomend
Jstu2016��ƴ���Ŀǰ��
====================
3��24��ʼ
--------------
		�ǳ���ª
		���
		��л����Ԭ��ĺ�̨���������ݣ��������ֻ�Ǹ��տ�
http://120.77.57.236:8080
# RESTful API���
>ͨ�����µ�api��ȡͼ�飨book�������ģ�paper�����ղأ�collection������Ϊ��behavior������Դ��

## 1.ͼ�鲿��
|����|��Դ��ַ|ʾ��|
| --- | --- | --- |
|���|POST /books|POST /books|
|ɾ��|DELETE /books/{id}|DELETE /books/1|
|����|PUT /books/{id}|PUT /books/1|
|��õ���|GET /books/{id}|GET /books/1|
|��ö��|GET /books/get?page={page}&size={size}|GET /books/get?page=1&size=10|
|�ؼ��ʲ�ѯ|GET /books/search?keyword={keyword}|GET /books/search?keyword=���˼|
|����ͼ��ID��ȡ�����Ƽ�|GET /books/recommend?id={id}|GET /books/recommend?id=1|

## 2.���Ĳ���
|����|��Դ��ַ|ʾ��|
| --- | --- | --- |
|���|POST /papers|POST /papers|
|ɾ��|DELETE /papers/{id}|DELETE /papers/1|
|����|PUT /papers/{id}|PUT /papers/1|
|��õ���|GET /papers/{id}|GET /papers/1|
|��ö��|GET /papers/get?page={page}&size={size}|GET /papers/get?page=1&size=10|
|�ؼ��ʲ�ѯ|GET /papers/search?keyword={keyword}|GET /papers/search?keyword=���˼|
|��������ID��ȡͼ���Ƽ�|GET /pape