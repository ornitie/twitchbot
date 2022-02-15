from flask import Flask
from bot import Bot
import threading
from dotenv import load_dotenv
from spotify import Spotify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Twitch, I\'m a flask server!'

@app.route('/json')
def json_hello():
    return {
        "name": "ornitie",
        "message": "Hello, World!"
    }

def main():
    spotify_client = Spotify()
    load_dotenv()
    bot = Bot(spotify_client)
    bot.run()

def start():
    app.run(port=5000, host='0.0.0.0', debug=False, use_reloader=False)

if __name__ == "__main__":
    load_dotenv()
    threading.Thread(target = start, args = (), daemon=True).start()
    print("started server...")
    main()