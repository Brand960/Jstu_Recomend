from django.shortcuts import render
from django.http import HttpResponse
from main.apps import *
import random
# 主页方法，获取随机文章和图书显示，使用了random方法随机1到2000之间的页数
def home(request):
	_page= str(random.randint(1, 2000))
	_size=str(10)
	res_book=get_by_page("book",_page,_size)
	res_paper=get_by_page("paper",_page,_size)
	return render(request,'home.html',{'res_book':res_book,'res_paper':res_paper,})

# 展示查询结果，根据输入的关键字词分别获取图书和论文查询结果
def show(request):
	if request.GET['keyword' ]:
		_keyword=request.GET['keyword' ]
		res_book=get_by_keyword("book", _keyword)
		res_paper=get_by_keyword("paper", _keyword)
		
		res_book.sort(key = lambda x:x["likeCount"])
		return render(request,'show.html',{"res_book":res_book,"res_paper":res_paper,"keyword":_keyword,})
	return HttpResponse("抱歉！请输入查询关键字")
	
# 获取推荐结果，若没有则提供数据配合网页脚本用随机结果展示
def recommend(request):	

	# 正常访问下
	if request.GET['id']:
		_page= str(random.randint(1, 2000))
		_size=str(10)
		res_book_r=get_by_page("book",_page,_size)
		res_paper_r=get_by_page("paper",_page,_size)
		# 获取论文/图书的ID
		_id=request.GET['id']
		# 获取类型
		_type=request.GET['type']
		# 获取推荐结果
		res_rec_paper=recommend__paper_by_id(_type, _id)
		res_rec_book=recommend__book_by_id(_type, _id)
		# 根据查询类型不同分别返回被查询的对象
		if _type=="paper":
			res_paper=get_by_id("paper",_id)
			return render(request,'recommend.html',{'res_paper':res_paper,"res_paper_r":res_paper_r,"res_book_r":res_book_r,
 																		'res_rec_paper':res_rec_paper,"res_rec_book":res_rec_book,})
		elif _type=="book":
			res_book=get_by_id("book",_id)
			return render(request,'recommend.html',{'res_book':res_book,"res_paper_r":res_paper_r,"res_book_r":res_book_r,
 																		'res_rec_paper':res_rec_paper,"res_rec_book":res_rec_book,})
		else:
			pass
	# 非正常访问处理
	return HttpResponse("抱歉！未知错误，请刷新试试")
	
	
	
	
	
	
	
	
	
	
	
	