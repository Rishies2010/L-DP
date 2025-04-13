import fire

# We must be able to use the cli like this:
# ```bash
# python ldp.py <command>
# ```

# Commands are:
# run 
# test
# help

# `run` Commands arguments:
# --exclude_cogs=['<cog_name>', ...]
# --env='/path/to/.env' (defaults to root/.env)
# --config='/path/to/config.json/'

# `test` Command arguments:
# --exclude_tests=['<test_name>' , ...]

class Commands(object):
    pass

def main():
    fire.Fire(Commands)

if __name__ == '__main__':
    print("Currently in devolepment please use `python bot.py` instead to run the bot.")
    main()