# If u see any bugs or errors, dont change the code, 
# just add a comment and i will fix it, also contact me on 
# discord: I am Scoopey <for @Rishies2010>

# ===========================
# SECTION: BASIC COMMANDS COG
# ===========================


from discord.ext import commands


# Basic commands for the bot
class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.PREFIX = self.bot.command_prefix # Get the prefix from the bot



    @commands.command()
    async def hello(self, ctx):
        await ctx.send(f"""Hello, {ctx.author.mention}...
I am {self.bot.user.mention}... to know more about me type `{self.PREFIX}help`""")



    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! Latency: {round(self.bot.latency * 1000)}ms')


    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__class__.__name__} Cog has been loaded!')



    @commands.command()
    async def help(self, ctx): 
        help_text = f"""
## I am a bot that simulates Linux. L-DP! 
"""
    
        await ctx.send(help_text)
        await self.commands(ctx)
    
    @commands.command()
    async def commands(self, ctx):
        
        commands_text = f"""
**Available Commands:**
1. Basic Commands
  - `{self.PREFIX}hello`: Greets you
  - `{self.PREFIX}ping`: Checks bot latency
  - `{self.PREFIX}commands`: Shows this message
"""

        await ctx.send(commands_text)