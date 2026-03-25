import tornado.ioloop
import tornado.websocket
from tornado.httpclient import HTTPRequest

async def start_client():
    url = "ws://localhost:8888/ws"
    try:
        conn = await tornado.websocket.websocket_connect(url)
        print("Da ket noi den Websocket Server!")
        
        message = "Hello Tornado Server"
        await conn.write_message(message)
        
        response = await conn.read_message()
        print(f"Phan hoi tu Server: {response}")
        
        conn.close()
    except Exception as e:
        print(f"Loi ket noi: {e}")

if __name__ == "__main__":
    tornado.ioloop.IOLoop.current().run_sync(start_client)