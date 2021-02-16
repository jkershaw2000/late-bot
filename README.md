# late-bot
---

A bot that gets people to hurry up.

## Set Up
- Requires
    - `texttable`
    - `discord.py`
- Create file called `creds.py` in root directory. Add discord bot token as variable called `token`
    - e.g. `token = <TOKEN>`
## Usage

`>late name1...nameN` - begins a lateness counter for the specified user(s)

`>here name1...nameN` - the users that were late have now arrived

`>stats [name1...nameN]` - show how often  and total lateness of users. If no user specified show all.
