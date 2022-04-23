import threading
import commands.windows

from flask import Flask
from bot import Bot
from dotenv import load_dotenv
from spotify import Spotify
from obs import OBS
from router import router

app = Flask(__name__)

app.register_blueprint(router)


def main(obs_client):
    spotify_client = Spotify()
    load_dotenv()
    bot = Bot(spotify_client, obs_client)
    bot.run()


def start_server():
    app.run(port=5000, host="0.0.0.0", debug=False, use_reloader=False)


if __name__ == "__main__":
    load_dotenv()
    obs_client = OBS()
    threading.Thread(target=start_server, args=(), daemon=True).start()
    threading.Thread(
        target=commands.windows.start, args=([obs_client]), daemon=True
    ).start()
    print("started server...")
    main(obs_client)
