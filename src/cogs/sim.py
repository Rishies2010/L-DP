# If u see any bugs or errors, dont change the code, 
# just add a comment and i will fix it, also contact me on 
# discord: I am Scoopey <for @Rishies2010>

# ===========================
# SECTION: SIMULATION COMMANDS COG
# ===========================

from discord.ext import commands


# Simulation commands for the bot
class Sim(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # TODO: Make these commands: v1.1.0
    @commands.command()
    async def boot(self, ctx):
        await ctx.send("Work in progress... (Multi-simulations not supported yet 😭)")
        

    @commands.command()
    async def stop(self, ctx):
        await ctx.send("Work in progress... (Multi-simulations not supported yet 😭)")


    @commands.command()
    async def reboot(self, ctx):
        await ctx.send("Work in progress... (Multi-simulations not supported yet 😭)") 
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__class__.__name__} Cog has been loaded!')
        
