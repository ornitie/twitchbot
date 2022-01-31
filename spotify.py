from requestor import Requestor
import asyncio
import os
from dotenv import load_dotenv
import base64

load_dotenv()

API_TOKEN_URL = "https://accounts.spotify.com/api/token"

async def get_new_token():
    requestor = Requestor()

    message = os.environ['SPOTIFY_CLIENT_ID']+':'+os.environ['SPOTIFY_CLIENT_SECRET']
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = 'Basic '+ base64_bytes.decode('ascii')
    
    headers = {'Authorization': base64_message}
    token = os.environ['SPOTIFY_REFRESH_TOKEN']
    data = {'grant_type':'refresh_token', 'refresh_token': token}

    response = await requestor.post_with_url_encoded(API_TOKEN_URL, data, headers)

    return response.json()['access_token']


asyncio.run(get_new_token())