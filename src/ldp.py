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

        # __init__ ends here

    def help(self):
        """Show a help message."""

        print(self.help_text)


    def run(self, exclude_cogs: list[str] = None, configs: Path = None):
        """Starts the Bot."""
        print("This is not completely implemented yet")
        return

        
        # Handle configs
        if configs == None:
            configs = Path('../configs/')

        try:
            configs = Path(configs)
        except TypeError:
            print(f'Unexpected Type. --config only accepts `str`.\n'
                f'Try Entering your argument as \'{configs}\'')
            exit(1)

        except Exception as e:
            print(f'Unexpected Error: {e}')
            exit(1)

        if configs.is_file():
            print(f'The path {str(configs)} is not a directory.')
            exit(1)
        
        if not configs.exists():
            configs.mkdir()
        
    
        
        # Handle exclude cogs
        if exclude_cogs == None:
            exclude_cogs = []

        exclude_cogs = self._try_into_list(exclude_cogs)

        # Validating All the arguments
        if not self._validate_cogslist(exclude_cogs):
            print(f'The specified cogs for the argument `--exclude_cogs` is not right.\n'
                               f'The cogs must be a list containing only the following (case-sensitive):\n'
                               f'1. Basic\n'
                               f'2. Sim\n') 
            exit(1)
        # WARNING: Dont forget to add more

        
        
        
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

    def _try_into_list(self, value):
        """
Tries to convert any value into a list, if it isn't already a list.

Converts single values into a single-item list.
Converts collections into a list if the collection is iterable.

Args:
    value (any): The value to convert into a list.

Returns:
    list: A list containing either the original collection elements
          or a single-item list with the input value.

Note:
    If the input is already a tuple, dict, list, or set, it will be converted to a list.
    Otherwise, the input will be wrapped in a tuple first, then converted to a list.
        """

        if not isinstance(value, (tuple, dict, set, list)):
            value = (value,)
        return list(value)

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