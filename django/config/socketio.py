import socketio

mgr = socketio.AsyncRedisManager('redis://redis')
sio = socketio.AsyncServer(
    client_manager=mgr, async_mode='asgi', cors_allowed_origins='*')


@sio.event
async def subscribe(sid, _):
    sio.enter_room(sid, 'flash')
