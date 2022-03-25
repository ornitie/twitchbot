import time
from dotenv import load_dotenv
import os
import logging

from obswebsocket import obsws, requests, events

load_dotenv()
logging.basicConfig(level=logging.INFO)


class OBS:
    def __init__(self):
        host = "localhost"
        port = 4444
        password = os.environ["OBS_PASSWORD"]
        ws = obsws(host, port, password)
        ws.connect()

        self.ws = ws

    def test(self):
        try:
            scenes = self.ws.call(requests.GetSceneList())
            outputs = self.ws.call(requests.GetSourcesList())
            print(outputs)
            for s in scenes.getScenes():
                name = s["name"]
                print("Switching to {}".format(name))
                # ws.call(requests.SetCurrentScene(name))
                time.sleep(2)

            print("End of list")

        except KeyboardInterrupt:
            pass

        self.ws.register(on_event)
        self.ws.register(on_switch, events.SwitchScenes)
        self.ws.connect()

        try:
            print("OK")
            time.sleep(10)
            print("END")

        except KeyboardInterrupt:
            self.ws.disconnect()

    def change_to_scene(self, scene_name):
        try:
            scenes = self.ws.call(requests.GetSceneList())
            scene_names = [s["name"] for s in scenes]

            for s in scenes.getScenes():
                name = s["name"]
                if name == scene_name:
                    print("Switching to {}".format(name))
                    self.ws.call(requests.SetCurrentScene(name))
                    return
                # time.sleep(2)

            print("scene not found")
            # TODO: return error

        except KeyboardInterrupt:
            pass


def on_event(message):
    print("Got message: {}".format(message))


def on_switch(message):
    print("You changed the scene to {}".format(message.getSceneName()))
