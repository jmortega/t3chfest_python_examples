from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application, url, asynchronous
 
class HelloHandler(RequestHandler):
    @asynchronous
    def get(self):
        self.write("Hello, world")
 
    def post(self):
        self.write("Hello, world")    
 
app = Application([ url(r"/", HelloHandler), ])
app.listen(9090)
IOLoop.current().start()