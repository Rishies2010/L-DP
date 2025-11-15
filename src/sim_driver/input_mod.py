# If u see any bugs or errors, dont change the code, 
# just add a comment and i will fix it, also contact me on 
# discord: I am Scoopey <for @Rishies2010>



from discord.ext import commands
import discord

# ===========================
# SECTION: INPUT BUFFER
# ===========================

# An implementation of a simple InputBuffer to store input until the "kernel" calls get_input()
class InputBuffer:
    """
class InputBuffer:
A class that stores input until the "kernel" calls get_input()
    """
    def __init__(self):
        self.buffer = []



    def write(self, item):
        """
fn write:
A function that writes an item to the input buffer.
        """
        self.buffer.append(item)



    def read(self):
        """
fn read:
A function that reads an item from the input buffer.
This function will remove the last item and then return it.
        """
        if self.buffer:
            return self.buffer.pop(0)
        else:
            return None

    def read_all(self):
        """
fn read_all:
A function that reads all items from the input buffer.
This function will remove all items and then return them.
        """
        all_items = self.buffer.copy()
        self.buffer.clear()
        return all_items


    # For printing the class
    def __str__(self):
        return f"InputBuffer(items={self.buffer})"

    def __repr__(self):
        return f"InputBuffer(buffer={self.buffer})"



# Initialize the InputBuffer
input_list = InputBuffer()

# ===========================
# SECTION: INPUT COG
# ===========================

class Input(commands.Cog):
    """
class Input:
A class that inherits from `discord.ext.commands.Cog`.
It is a cog that listens for messages in a specific channel and stores them in the input buffer.
After the message is sent it is deleted.
    """

    # Initialize the cog
    def __init__(self, bot, target_channel_id):
        self.bot = bot
        self.target_channel_id = target_channel_id



    # Listens for messages and stores them in the buffer
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        if str(message.channel.id) != str(self.target_channel_id):
            print(f'Invalid Channel: {message.channel.id}, Expected: {self.target_channel_id}')
            return
                
        input_list.write(message.content)

        print(f"Input: {input_list}")

    

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Input Listener has been loaded for channel with id: {self.target_channel_id}!')



# The "kernel" should call this and get the input
async def get_input():
    """
fn get_input:
A function that gets the input from the input buffer.
    """
    pass
