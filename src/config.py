# If u see any bugs or errors, dont change the code, 
# just add a comment and i will fix it, also contact me on 
# discord: I am Scoopey <for @Rishies2010>


import json

# ===========================
# SECTION: LOADING CONFIGS
# ===========================


# A class to store bot configurations
class BotConfig:
    """
class BotConfig:
A class that stores the bot configurations.
They describe the bot's behavior for different commands.
    """
    def __init__(self, path="ldp-meta/bot.json"):
        try:
            # Open the json file
            with open(path) as f:
                try:
                    self.config = json.load(f)
                except json.decoder.JSONDecodeError as e:
                    raise RuntimeError(f"Invalid JSON in {path}.\n{e}")

                try:
                    # Get the bot token 
                    self.TOKEN = self.config["BOT_TOKEN"]
                except:
                    preferred_syntax = r"""
{
    "BOT_TOKEN": "[YOUR_BOT_TOKEN]"
}
"""
                    raise RuntimeError(f"Expected BOT_TOKEN to be specified in {path}.\nThe file should look like this:\n{preferred_syntax}")
            

        except FileNotFoundError:
            raise RuntimeError(f"Please ensure {path} exists!")



# A class to store configurations (Configs relating to the simulation)
class Config:
    """
class Config:
A class that stores the simulation configurations.
They describe the bot's behavior for different starting simulations.
    """
    def __init__(self, path="ldp-meta/config.json"):
        try:
            # Open the json file
            with open(path) as f:
                try:
                    self.config = json.load(f)
                except json.decoder.JSONDecodeError as e:
                    raise RuntimeError(f"Invalid JSON in {path}.\n{e}")


                try:
                    # Get the bot token
                    self.PREFIX = self.config["PREFIX"]
                    self.CHANNEL_ID = self.config["CHANNEL_ID"]
                except KeyError:
                    preferred_syntax = r"""
{
    "PREFIX": "! (Your Desired Prefix)", 
    "CHANNEL_ID": "[CHANNEL_ID_FOR_AUTODELETE]"
}"""
                    raise RuntimeError(f"Expected PREFIX and CHANNEL_ID to be specified in {path}\nThe file should look like this:\n{preferred_syntax}")
        except FileNotFoundError:
            raise RuntimeError(f"Please ensure {path} exists!")




# Load bot configurations from JSON files
bot_config = BotConfig()
config = Config()
