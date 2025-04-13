# If u see any bugs or errors, dont change the code, 
# just add a comment and i will fix it, also contact me on 
# discord: I am Scoopey <for @Rishies2010>


# ===========================
# SECTION: IMPORTS
# ===========================


import discord
from discord.ext import commands


import sim_driver.input_mod as input_mod

from cogs import Basic
from cogs import Sim


# ===========================
# SECTION: IMPORT CONFIGS
# ===========================

# Import configs for the bot: bot.json and config.json stored as bot_config and config variables respectively
from config import *


# ===========================
# SECTION: BOT SETUP
# ===========================


# Setup bot with intents
intents = discord.Intents.default()
intents.message_content = True



# Define bot class
class LDPBot(commands.Bot):
    """
class LDPBot:
A class that inherits from discord.ext.commands.Bot. 
It mainly packs all the different cogs together.
    """
    def __init__(self):
        # Call super class
        super().__init__(command_prefix=config.PREFIX, intents=intents)


        self.remove_command('help')  # Remove default help command



    async def setup_hook(self):
        # Load Cogs
        await self.add_cog(Basic(self))
        await self.add_cog(Sim(self))

        # Load the "drivers"
        await self.add_cog(input_mod.Input(self, config.CHANNEL_ID))
    


    async def on_ready(self):
        print(f'Bot is ready and logged in as {self.user}.')



# ===========================
# SECTION: RUN BOT  
# ===========================

def main():
    # Create bot instance
    bot = LDPBot()

    # Run bot
    bot.run(bot_config.TOKEN)

if __name__ == "__main__":
    main()