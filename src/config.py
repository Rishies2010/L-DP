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
                self.config = json.load(f)


                try:
                    # Get the bot token 
                    self.TOKEN = self.config["BOT_TOKEN"]
                except:
                    print("Error: Expected BOT_TOKEN to be specified in ldp-meta/bot.json")

        except FileNotFoundError:
            print("Please ensure both ldp-meta/bot.json and ldp-meta/config.json exist!")
            exit()



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
                self.config = json.load(f)


                try:
                    # Get the bot token
                    self.PREFIX = self.config["PREFIX"]
                    self.CHANNEL_ID = self.config["CHANNEL_ID"]
                except KeyError:
                    print("Error: Expected PREFIX and CHANNEL_ID to be specified in ldp-meta/config.json")
        except FileNotFoundError:
            print("Please ensure both ldp-meta/bot.json and ldp-meta/config.json exist!")
            exit()




# Load bot configurations from JSON files
bot_config = BotConfig()
config = Config()
