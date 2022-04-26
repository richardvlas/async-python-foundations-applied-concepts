import asyncio

from quart import Quart, websocket, render_template
from quart import g


app = Quart(__name__)

connections = set()

@app.websocket("/ws")
async def ws():
    # when you connection, we are going to add the websocket connections 
    # to the connections pool - connections
    connections.add(websocket._get_current_object())
    try:
        # Runs for as long as you are connected
        while True:
            # It grabs the next message
            message = await websocket.receive()
            # Create a bunch of coroutines with that message
            send_coroutines = [connection.send(message) for connection in connections]
            await asyncio.gather(*send_coroutines)
    # once you disconect from the websocket -> remove the websocket 
    # from the connections pool
    finally:
        connections.remove(websocket._get_current_object())


@app.route("/")
async def chat():
    return await render_template("chat.html")


app.run(use_reloader=True, port=3000)