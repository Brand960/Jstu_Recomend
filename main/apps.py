from django.apps import AppConfig
import requests
import json
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
# 通过页数范围在系统中拿取数据
def get_by_page(_type,_page,_size):
    if (_type=="paper"):
        url=URL+"papers/get?page="+_page+"&size="+_size
    elif(_type=="book"):
        url=URL+"books/get?page="+_page+"&size="+_size
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

def ilike(_type,_id):
    url="http://120.77.57.236:8080/feedback/like?id="+_id+"&type="+_type
    like=requests.get(url)
    like=json.loads(like.text)
    return like

class MainConfig(AppConfig):
    name = 'main'
