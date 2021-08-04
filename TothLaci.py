import os
from init_dc import client
from VideoStream import VideoStream

TOKEN = os.getenv("DISCORD_TOKEN", "ide kell az api kulcs")
streamer = VideoStream

client.run(TOKEN)
