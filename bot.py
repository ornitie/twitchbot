# import os
# from twitchio.ext import commands
# from twitchio.http import TwitchHTTP
# from twitchio import ChannelInfo
# from twitchio import Client
# import client
# import asyncio


# class Bot(commands.Bot):
#     def __init__(self, spotify_client, obs_client):
#         super().__init__(
#             token=os.environ["OAUTH"], prefix="!", initial_channels=["ornitie"]
#         )
#         self._spotify = spotify_client
#         self.obs_client = obs_client
#         client.TwitchioClient()

#     async def event_ready(self):
#         print(f"Logged in as | {self.nick}")

#     async def event_message(self, message):
#         if message.echo:
#             return

#         print(message.content)
#         await self.handle_commands(message)

#     @commands.command(name="hello")
#     async def hello(self, ctx: commands.Context):
#         print("hellooo")
#         await ctx.send(f"Hello @{ctx.author.name}!")

#     @commands.command(name="what")
#     async def what(self, ctx: commands.Context):
#         """Create a command as a response to the question for what we're doing rn"""

#         print("Someone asked...")
#         await ctx.send(
#             f"@{ctx.author.name} Working on a spaced repetition web app"
#         )

#     @commands.command(name="song")
#     async def song(self, ctx: commands.Context):
#         print("someone is asking for the song")
#         song = self._spotify.get_current_song()
#         print(song)
#         await ctx.send(f"@{ctx.author.name} {song}")

#     @commands.command(name="title")
#     async def title(self, ctx: commands.Context):
#         print("testing the stream title")
#         title = await self.fetch_channel("ornitie")
#         print(title)
