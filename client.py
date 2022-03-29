from twitchio import Client
import os


class TwitchioClient(Client):
    def __init__(self):
        super().__init__(token=os.environ["OAUTH"])
