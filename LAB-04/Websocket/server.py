import tornado.ioloop
import tornado.web
import tornado.websocket

class MyWebSocketHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        print("Client da ket noi!")

    def on_message(self, message):
        print(f"Nhan tu Client: {message}")
        self.write_message(f"Server phan hoi: {message}")

    def on_close(self):
        print("Client da ngat ket noi!")

def make_app():
    return tornado.web.Application([
        (r"/ws", MyWebSocketHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Websocket Server dang chay tai ws://localhost:8888/ws")
    tornado.ioloop.IOLoop.current().start()