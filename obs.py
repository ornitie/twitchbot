import sys
import time
from dotenv import load_dotenv
import os

load_dotenv()


import logging
logging.basicConfig(level=logging.INFO)

sys.path.append('../')
from obswebsocket import obsws, requests, events  # noqa: E402

host = "localhost"
port = 4444
password = os.environ['OBS_PASSWORD']

ws = obsws(host, port, password)
ws.connect()

try:
    scenes = ws.call(requests.GetSceneList())
    for s in scenes.getScenes():
        name = s['name']
        print(u"Switching to {}".format(name))
        ws.call(requests.SetCurrentScene(name))
        time.sleep(2)

    print("End of list")

except KeyboardInterrupt:
    pass


def on_event(message):
    print(u"Got message: {}".format(message))


def on_switch(message):
    print(u"You changed the scene to {}".format(message.getSceneName()))


ws = obsws(host, port, password)
ws.register(on_event)
ws.register(on_switch, events.SwitchScenes)
ws.connect()

try:
    print("OK")
    time.sleep(10)
    print("END")

except KeyboardInterrupt:
    pass

ws.disconnect()