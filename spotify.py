from requestor import Requestor
import os
import base64

API_TOKEN_URL = "https://accounts.spotify.com/api/token"
CURRENT_SONG_URL = "https://api.spotify.com/v1/me/player/currently-playing"


class Spotify:
    def __init__(self):
        self._refresh_token = os.environ["SPOTIFY_REFRESH_TOKEN"]
        self._client_id = os.environ["SPOTIFY_CLIENT_ID"]
        self._client_secret = os.environ["SPOTIFY_CLIENT_SECRET"]
        self._token = None
        self._requestor = Requestor()

    def _get_new_token(self):
        message = f"{self._client_id}:{self._client_secret}"
        message_bytes = message.encode("ascii")
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = "Basic " + base64_bytes.decode("ascii")

        headers = {"Authorization": base64_message}

        token = self._refresh_token
        data = {"grant_type": "refresh_token", "refresh_token": token}

        response = self._requestor.post_with_url_encoded(API_TOKEN_URL, data, headers)

        return response.json()["access_token"]

    def get_current_song(self):
        if not self._token:
            token = self._get_new_token()
            self._token = token

        try:
            token = self._token
            headers = {"Authorization": f"Bearer {token}"}
            r = self._requestor.simple_get(CURRENT_SONG_URL, headers=headers)

            if r.status_code != 200:
                token = self._get_new_token()
                self._token = token
                r = self._requestor.simple_get(CURRENT_SONG_URL, headers=headers)

            song_name = r.json()["item"]["name"]
            song_authors = [author["name"] for author in r.json()["item"]["artists"]]
            song = f'{", ".join(song_authors)} - {song_name}'

            return song
        except:
            return "Unhandled Error"
