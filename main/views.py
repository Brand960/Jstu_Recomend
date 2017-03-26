from django.shortcuts import render
# from django.http import HttpResponse

import requests
import json
import random
from django.http.response import HttpResponse
import time

URL="http://120.77.57.236:8080/"

def get_by_keyword(_type,_keyword):
	if (_type=="book"):
		url=URL+"books/search?keyword="+_keyword
	elif(_type=="paper"):
		url=URL+"papers/search?keyword="+_keyword
	req=requests.get(url)
	res=json.loads(req.text)
	return res

# def get_books(i):
# 	url=URL+"books/"+i
# 	req=requests.get(url)
# 	res=json.loads(req.text)
# 	return res
	
def get_by_id(_type,_id):
	if (_type=="book"):
		url=URL+"books/"+_id
	elif(_type=="paper"):
		url=URL+"papers/"+_id
	req=requests.get(url)
	res=json.loads(req.text)
	return res

def get_by_page(_type,_page,_size):
	if (_type=="paper"):
		url=URL+"papers/get?page="+_page+"&size="+_size
	elif(_type=="book"):
		url=URL+"books/get?page="+_page+"&size="+_size
	req=requests.get(url)
	res=json.loads(req.text)
	return res

# def recommend_by_id(_type,_id):
# 	if (_type=="book"):
# 		url=URL+"books/recommend?id="+_id
# 	elif(_type=="paper"):
# 		url=URL+"papers/recommend?id="+_id
# 	
# 	req=requests.get(url)
# 	res=json.loads(req.text)
# 	return res

def recommend__book_by_id(_type,_id):
	url=URL+"/recommend/books?id="+_id+"&type="+_type
	req=requests.get(url)
	res=json.loads(req.text)
	return res

def recommend__paper_by_id(_type,_id):
	url=URL+"/recommend/papers?id="+_id+"&type="+_type
	req=requests.get(url)
	res=json.loads(req.text)
	return res

def home(request):
	_page= str(random.randint(1, 2000))
	_size=str(10)
	res_book=get_by_page("book",_page,_size)
	res_paper=get_by_page("paper",_page,_size)
	#res_book=get_by_keyword(book_type,book_title)
	#res_paper=get_by_keyword(paper_type,paper_title)
	#res=recommend_by_id(_type,_id)
	return render(request,'home.html',{'res_book':res_book,'res_paper':res_paper,})
	
def show(request):
	if request.GET['keyword' ]:
		_keyword=request.GET['keyword' ]
		res_book=get_by_keyword("book", _keyword)
		res_paper=get_by_keyword("paper", _keyword)
		
		res_book.sort(key = lambda x:x["likeCount"])
		return render(request,'show.html',{"res_book":res_book,"res_paper":res_paper,"keyword":_keyword,})
	return HttpResponse("抱歉！请输入查询关键字")
	
def recommend(request):	
	
	if request.GET['id']:
		_page= str(random.randint(1, 2000))
		_size=str(10)
		res_book_r=get_by_page("book",_page,_size)
		res_paper_r=get_by_page("paper",_page,_size)
		
		_id=request.GET['id']
		
		_type=request.GET['type']
		res_rec_paper=recommend__paper_by_id(_type, _id)
		res_rec_book=recommend__book_by_id(_type, _id)

		if _type=="paper":
			res_paper=get_by_id("paper",_id)
			return render(request,'recommend.html',{'res_paper':res_paper,"res_paper_r":res_paper_r,"res_book_r":res_book_r,
 																		'res_rec_paper':res_rec_paper,"res_rec_book":res_rec_book,})
		elif _type=="book":
			res_book=get_by_id("book",_id)
			return render(request,'recommend.html',{'res_book':res_book,"res_paper_r":res_paper_r,"res_book_r":res_book_r,
 																		'res_rec_paper':res_rec_paper,"res_rec_book":res_rec_book,})
# 		if request.GET['type']=="paper":
# 			res_paper=get_by_id("paper",_id)
# 			res_rec_paper=recommend_by_id("paper",_id)
# 			return render(request,'recommend.html',{'res_paper':res_paper,"res_paper_r":res_paper_r,"res_book_r":res_book_r,
# 																		'res_rec_paper':res_rec_paper,})
# 		if request.GET['type']=="book":
# 			res_book=get_by_id("book",_id)
# 			res_rec_book=recommend_by_id("book",_id)
# 			return render(request,'recommend.html',{'res_book':res_book,"res_paper_r":res_paper_r,"res_book_r":res_book_r,
# 																		'res_rec_book':res_rec_book,})
		
		
	return HttpResponse("抱歉！未知错误，请刷新试试")
	
	
	
	
	
	
	
	
	
	
	
	