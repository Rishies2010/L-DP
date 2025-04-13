# L-DP
**The Linux-Discord Port Collaboration Repository**

Welcome to the **L-DP Project**, a repository dedicated to managing and maintaining the development of a bot that simulates a Linux environment on Discord. 

> **Note:** This is not a full Linux port but rather a simulation designed for Discord users. Please refrain from modifying any files unless you have explicit permission to do so.

## Installation
To set up the project locally, follow these steps:

### For Windows

#### Using PowerShell
```powershell
# Clone and setup
git clone https://github.com/Rishies2010/L-DP.git
cd L-DP
python -m venv env
.\env\Scripts\Activate.ps1
pip install -r requirements.txt
```

#### Using Command Prompt (CMD)
```batch
:: Clone and setup
git clone https://github.com/Rishies2010/L-DP.git
cd L-DP
python -m venv env
.\env\Scripts\activate.bat
pip install -r requirements.txt
```

> **Note:** Make sure you have Python and Git installed. For PowerShell, you may need to run `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` first to allow script execution.

### For macOS/Linux
1. **Clone the Repository**  
   ```bash
   git clone https://github.com/Rishies2010/L-DP.git
   cd L-DP
   ```

2. **Set Up Environment**  
   ```bash
   python3 -m venv env
   source env/bin/activate
   pip3 install -r requirements.txt
   ```

3. **Run the Bot**  
   ```bash
   python3 bot.py
   ```

## Prerequisites
You'll need to create two configuration files before running the bot:

### 1. src/ldp-meta/config.json
```json
{
    "PREFIX": "!",  // Your desired command prefix
    "CHANNEL_ID": "YOUR_CHANNEL_ID"  // Channel ID for auto-delete functionality
}
```

### 2. src/ldp-meta/bot.json
```json
{
    "BOT_TOKEN": "YOUR_BOT_TOKEN"  // Your Discord bot token from Discord Developer Portal
}
```

> **Note:** If you miss creating these files, the script will guide you through making them. You can get your bot token from the [Discord Developer Portal](https://discord.com/developers/applications) and channel ID by enabling Developer Mode in Discord and right-clicking the channel.


## Running the Bot

### Windows
Navigate to the src directory and run:
```bash
cd src
python bot.py
```

### macOS/Linux
Navigate to the src directory and run:
```bash
cd src
python3 bot.py
```

> **Note:** Make sure you have activated your virtual environment and installed all dependencies before running the bot. The bot will automatically load configurations from the `ldp-meta` directory.

If you encounter any issues:
1. Verify your configuration files are properly set up
2. Ensure your bot token is valid
3. Check that your virtual environment is activated (`env` should appear in your terminal prompt)

## Join Us
Connect with the community and contribute to the project by joining the [L-DP Discord Server](https://discord.gg/amvWU5gV).