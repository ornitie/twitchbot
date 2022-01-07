from bot import Bot
from dotenv import load_dotenv
from spotify import Spotify

def main():
    spotify_client = Spotify()
    load_dotenv()
    bot = Bot(spotify_client)
    bot.run()

main()