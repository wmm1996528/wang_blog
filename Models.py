from peewee import *
from config import *
# 建立博客表
class Blogs(Model):
	user = CharField()
	title = CharField()
	publish_time = DateTimeField()
	content = TextField()
	class Meta:
		database = SqliteData
# Blogs.create_table()


