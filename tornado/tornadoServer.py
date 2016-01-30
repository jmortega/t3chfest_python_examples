import tornado.ioloop
import tornado.web
import tornado.websocket
from tornado.options import define, options, parse_command_line
class Client:
    def __init__(self, clientId, name, cont, connection):
        self.id = clientId
        self.name = name
        self.cont = cont
        self.connection = connection 
 
clients = []
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("test.html")
 
class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self, *args):
        self.id = self.get_argument("Id")
        self.name = self.get_argument("name")
        self.cont = self.get_argument("continue")
        newclient = True
        for client in clients:
            if client.id == self.id:
                client.connection.write_message("Hello Again %s !" %(client.name))
                newclient = False
                break
        if newclient:
            clientRef = Client(self.id, self.name, self.cont, self)
            clients.append(clientRef)
            self.write_message("Hello %s !" %(self.name))
            
 
    def on_message(self, message):        
        for client in clients:
            if client.id == self.id:
                print "Message from %s received : %s" % (client.name, message)
     
       
    def on_close(self):
        for client in clients:
            if self.id == client.id:
                clients.remove(client)
                break
 
define("port", default=8888, help="run on the given port", type=int)
app = tornado.web.Application([
    (r'/', IndexHandler),
    (r'/ws', WebSocketHandler),
])
 
if __name__ == '__main__':
    parse_command_line()
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()