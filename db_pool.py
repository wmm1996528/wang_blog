from peewee import *
from pathlib import Path
from Models import *
from config import *


# 连接sqlite
# db = SqliteDatabase(str(Path.joinpath(data_path, 'blogs.db')))


# 插入函数


# 查找函数
class DBUtil():
	def __init__(self):
		self.db = SqliteData

	def find(self, Tables, **kw):
		if kw:
			key = list(kw.keys())[0]
			value = list(kw.values())[0]
		# p = Tables.select().where(Tables['key']=value)
		# for i in p:
		# 	print(i)
		else:
			p = Tables.select()
			return p

	# 博客数据查找
	def blog_find(self):
		blog_data = self.find(Blogs)
		datas = []
		for data in blog_data:
			blog_dic = {
				'user': data.user,
				'title': data.title,
				'publish_time': data.publish_time,
				'content': data.content,
			}
			datas.append(blog_dic)
		return datas

	def insert(self, Tables, **kw):
		p = Tables(**kw)
		p.save()
	# insert(Blogs,
	#        user='wang',
	#        title='wang',
	#        publist_time='2018-12-19',
	#        content='wang',
	#        )

# find(Blogs)
