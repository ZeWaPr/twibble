import web

urls = (
	'/', 'index'
)

class index:
	def GET(self):
		# if not name:
			# name = 'World'
		# return 'Hello, ' + name + '!'
		return 'Hello, world!'

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()