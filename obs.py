import sys
import time
from dotenv import load_dotenv
import os

load_dotenv()
os.system('cmd /c "notepad"') 

import logging
logging.basicConfig(level=logging.INFO)

sys.path.append('../')
from obswebsocket import obsws, requests, events

host = "localhost"
port = 4444
password = os.environ['OBS_PASSWORD']

ws = obsws(host, port, password)
ws.connect()

def change_to_scene(scene_name):
    try:
        scenes = ws.call(requests.GetSceneList())
        scene_names = [s['name'] for s in scenes]

        for s in scenes.getScenes():
            name = s['name']
            if name == scene_name:
                print(u"Switching to {}".format(name))
                ws.call(requests.SetCurrentScene(name))
                return
            #time.sleep(2)

        print("scene not found")
        #TODO: return error

    except KeyboardInterrupt:
        pass

try:
    scenes = ws.call(requests.GetSceneList())
    outputs = ws.call(requests.GetSourcesList())
    print(outputs)
    for s in scenes.getScenes():
        name = s['name']
        print(u"Switching to {}".format(name))
        #ws.call(requests.SetCurrentScene(name))
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