import requests as req
from dotenv import load_dotenv
import os

load_dotenv()


class Requestor:
    async def request(ctx):

        AUTH_URL = "https://accounts.spotify.com/api/token"
        CLIENT_ID = os.environ["SPOTIFY_CLIENT"]
        CLIENT_SECRET = os.environ["SPOTIFY_SECRET"]
        # POST
        auth_response = req.post(
            AUTH_URL,
            {
                "grant_type": "client_credentials",
                #'client_id': CLIENT_ID,
                #'client_secret': CLIENT_SECRET,
            },
        )

        # convert the response to JSON
        auth_response_data = auth_response.json()

        # save the access token
        # access_token = auth_response_data['access_token']
        token = os.environ["SPOTIFY_TOKEN"]
        current_url = "https://api.spotify.com/v1/me/player/currently-playing"
        headers = {"Authorization": f"Bearer {token}"}
        r = req.get(current_url, headers=headers)
        song_name = r.json()["item"]["name"]
        song_authors = [author["name"] for author in r.json()["item"]["artists"]]

        song = f'{", ".join(song_authors)} - {song_name}'

        return song

    def post_with_url_encoded(ctx, url, data, headers):
        return req.post(url, data=data, headers=headers)

    def simple_get(ctx, url, headers):
        return req.get(url, headers=headers)
