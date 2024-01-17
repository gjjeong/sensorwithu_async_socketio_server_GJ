from django.shortcuts import render

# Create your views here.
#GJ
# python_socket_socketserver/views.py
# iohttp, socketio
#socket_server5.py

from aiohttp import web
import socketio

## creates a new Async Socket IO Server
#sio = socketio.AsyncServer()

#GJ to evade CORS origin error
#sio = socketio.Server(cors_allowed_origins='*')
sio = socketio.AsyncServer(cors_allowed_origins='*')

#GJ
# #@cross_origin()
# socketio = SocketIO(app, cors_allowed_origins="*")

## Creates a new Aiohttp Web Application
app = web.Application()
# Binds our Socket.IO server to our Web App instance
sio.attach(app)

#sio.attach(app, cors_allowed_origins="*")

## If we wanted to create a new websocket endpoint,
## use this decorator, passing in the name of the
## event we wish to listen out for
@sio.event
async def user_msg(sid, data):
    print("sid: ", sid)
    print("data: ", data)
#    await sio.emit('message', data)   # broadcase transmit
    await sio.emit('message', data, sid)   # client only transmit

@sio.event
async def all_msg(sid, data):
    print("sid: ", sid)
    print("data: ", data)
    await sio.emit('message', data)   # broadcase transmit

@sio.event
async def connect(sid, environ, auth):
    print('connect ', sid)

@sio.event
async def disconnect(sid):
    print('disconnect ', sid)

## we can define aiohttp endpoints just as we normally would with no change
async def index(request):
    #with open('index.html') as f:
    with open('python_socketio_server/templates/python_socketio_server/index.html') as f:
    #with open('socket_client51_index_multiple_self_once_and_all_return_socketio.html') as f:
        return web.Response(text=f.read(), content_type='text/html')

## We bind our aiohttp endpoint to our app router
app.router.add_get('/', index)
#app.router.add_get('python_socketio_server/', index)

## We kick off our server
#if __name__ == '__main__':
#    web.run_app(app, host='localhost', port=18000)
web.run_app(app, host='localhost', port=18000)
