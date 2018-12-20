import tornado.httpserver
import tornado.ioloop
import tornado.options
import os
import tornado.web
import logging

logging.basicConfig(level=logging.INFO)
from tornado.options import define, options
from db_pool import *

db = DBUtil()


class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		blog_data = db.blog_find()
		# print(blog_data)
		s = [1, 2, 3, 4]
		self.render('index.html', blog_data=blog_data)


class BlogHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('blog.html')


class LoginHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('login.html')

	def post(self, *args, **kwargs):
		print(self.request.remote_ip)
		user = self.get_argument('user')
		password = self.get_argument('password')
		if user == '123' and password == '123':
			self.render('')

if __name__ == '__main__':
	app = tornado.web.Application(handlers=[
		(r'/', IndexHandler),
		(r'/blog/', BlogHandler),
		(r'/login', LoginHandler)
	],
		template_path=os.path.join(os.path.dirname(__file__), 'templates'),
		static_path=os.path.join(os.path.dirname(__file__), "static"),
	)
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(8000)
	logging.info('Tornado Web App at http://127.0.0.1:8000 ... ')
	tornado.ioloop.IOLoop.instance().start()
