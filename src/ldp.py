import fire
from pathlib import Path
import cogs

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
      --exclude_cogs='<cog_name>', ...  List of cog names to exclude
      --configs='path/to/configs/folder' Folder which contains all the configs
                > Configs are located in the same directory level as `src/` by default or one directories above

  test    Run the test suite
    Options:
      --exclude_tests='<test_name>', ...  List of tests to exclude

Examples:
  python ldp.py run --exclude_cogs='Basic','Sim' 
  python ldp.py test --exclude_tests='test_input'
"""

        # Stores the cogs to be used for the bot
        self.cogs_list = [
            cogs.Basic,
            cogs.Sim
        ] 
        # WARNING: Dont forget to add more

        # __init__ ends here

    def help(self):
        """Show a help message."""

        print(self.help_text)
        return 0


    def run(self, exclude_cogs: list[str] = None, configs: Path = Path('../configs/')):
        """Starts the Bot."""
        print("This is not completely implemented yet")
        return

        if exclude_cogs == None:
            exclude_cogs = []

        # Make sure that all the inputs are of needed type
        if not isinstance(exclude_cogs, list):
            exclude_cogs = [exclude_cogs]
        
        try:
            configs = Path(configs)
        except TypeError:
            raise TypeError(f'Unexpected Type. --config only accepts `str`.\n'
                            f'Try Entering your argument as \'{configs}\'')
        except Exception as e:
            print(f'Unexpected Error: {e}')
            raise
    
        
        # Validating All the arguments
        if not self._validate_cogslist(exclude_cogs):
            raise RuntimeError(f'The specified cogs for the argument `--exclude_cogs` is not right.\n'
                               f'The cogs must be a list containing only the following (case-sensitive):\n'
                               f'1. Basic\n'
                               f'2. Sim\n') 
        # WARNING: Dont forget to add more
        
        if not configs.exists():
            configs.mkdir()

        if not configs.is_dir():
            return 1
        
        # Other logic once Refactoring of LDPBot is done
        # let bot = LDPBot() or maybe a builder
        # bot.exclude_cogs(exclude_cogs)
        # bot.set_configs_path(configs)
        # let bot = bot.build() if its a builder
        # bot.run()
    
    # TODO: Implement this once tests become a thing
    def test(self, exclude_tests: list[str] = []):
        """Runs the test suite."""
        pass


    # Internal methods

    def _validate_cogslist(self, cogslist: list[str]) -> bool:
        """Validates Whether a list of cogs is healthy or not"""
        cogs_namespace = vars(cogs)
        for cog in cogslist:
            if not cog in cogs_namespace and not isinstance(cogs_namespace.get(cog), type):
                return False
        
        return True
            

def main():
    fire.Fire(Commands)

if __name__ == '__main__':
    print("Currently in devolepment please use `python bot.py` instead to run the bot.")
    main()