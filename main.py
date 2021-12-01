from dotenv import load_dotenv #import environment lib
load_dotenv()
import os

from twitchio.ext import commands

class Bot(commands.Bot):

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        super().__init__(token= os.environ['OAUTH'], prefix='!', initial_channels=['ornitie'])

    async def event_ready(self):
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')

    """ async def event_message(self, message):
        print(message.content)
        await self.handle_commands(message) """

    @commands.command(name='hello')
    async def hello(self, ctx: commands.Context):
        # Send a hello back!
        print("hellooo")
        await ctx.send(f'Hello {ctx.author.name}!')


bot = Bot()
bot.run()