from dotenv import load_dotenv
import os
from twitchio.ext import commands

from requestor import Requestor

load_dotenv()

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token= os.environ['OAUTH'], prefix='!', initial_channels=['ornitie'])

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')

    async def event_message(self, message):
        if message.echo:
            return

        print(message.content)
        await self.handle_commands(message)

    @commands.command(name='hello')
    async def hello(self, ctx: commands.Context):
        print("hellooo")
        await ctx.send(f'Hello @{ctx.author.name}!')

    @commands.command(name='what')
    async def hello(self, ctx: commands.Context):
        """ Create a command as a response to the question for what we're doing rn """

        print("Someone asked...")
        await ctx.send(f'@{ctx.author.name} Right now I\'m just checking the Twitch API using twitchio to create a bot, and also the Spotify API')

    @commands.command(name='song')
    async def hello(self, ctx: commands.Context):
        print("someone is asking for the song")
        requestor = Requestor()
        song = await requestor.request()
        print(song)
        await ctx.send(f'@{ctx.author.name} {song}')

def main():
    bot = Bot()
    bot.run()

main()