import fire
from pathlib import Path

class Commands:
    """CLI command handler for L-DP bot management.
    Call: python ldp.py help for more information."""

    def __init__(self):
        self.help_text = """
L-DP CLI Tool
============

Commands:
  run     Start the Discord bot
  test    Run test suite

Usage:
  python ldp.py <command> [options]

Available Commands:
  run     Start the Discord bot
    Options:
      --exclude_cogs=['<cog_name>', ...]  List of cog names to exclude
      --configs='path/to/configs/folder' Folder which contains all the configs
                > Configs are located in the same directory level as `src/` by default or one directories above

  test    Run the test suite
    Options:
      --exclude_tests=['<test_name>', ...]  List of tests to exclude

Examples:
  python ldp.py run --exclude_cogs=['basic','sim'] 
  python ldp.py test --exclude_tests=['test_input']
"""

    def help(self):
        """Show a help message."""
        print(self.help_text)
        return 0


    def run(self, exclude_cogs: list = [], configs: Path = Path('../configs/')):
        """Starts the Bot."""
        pass
    
    def test(self, exclude_tests: list = []):
        """Runs the test suite."""
        pass

def main():
    fire.Fire(Commands)

if __name__ == '__main__':
    print("Currently in devolepment please use `python bot.py` instead to run the bot.")
    main()