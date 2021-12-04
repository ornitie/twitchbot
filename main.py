from dotenv import load_dotenv
import os
from twitchio.ext import commands

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
        await ctx.send(f'Hello {ctx.author.name}!')

    @commands.command(name='what')
    async def hello(self, ctx: commands.Context):
        """ Create a command as a response to the question fo what we're doing rn """

        print("Someone asked...")
        await ctx.send(f'Hello {ctx.author.name}! Right now I\'m just snooping the Twitch API using twitchio')


bot = Bot()
bot.run()