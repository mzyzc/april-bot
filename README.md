# April

A Discord bot that randomizes the nicknames of everyone on a server. Originally created as an April Fools' joke.

## Instructions

### On the host machine

Create a `.env` file in the project directory and populate it like so:

`DISCORD_TOKEN='{token-name-here}'`
`DISCORD_GUILD='{guild-name-here}'`

Then, simply run the bot from the terminal:

`./april-bot.py`

### On Discord

The bot is controlled with these commands:

- `~generate` assigns every member a name
- `~rename` sets everybody to their assigned name
- `~restore` resets everybody to their original name

Note that if `~generate` is used after running `~rename`, the original names will be lost. Make sure to always run `~restore` before generating new names.
