# election_info_bot #
* The bot searches a list of political and local subreddits for mentions of lists of search terms and provides information about relevant elections.
* Much remains to be done.
* Version 0.1

## Set up ##

This post can get you up and running: http://pythonforengineers.com/build-a-reddit-bot-part-1/

## Running a bot ##

To run an individual bot, `python 2018-11-06-ca.py`

To run all the bots sequentially, `./ei.sh`

## "Structure" ##

I err perhaps too heavily on the side of code that works over code that is good, and this is my first Python project. Feel free to tell me how awful this code is if it's in the form of a pull request.

Scripts are currently per state, per general election. That is, a special election on May 6, 2018 in West Virginia has its search terms in 2018-05-06-wv.py.

Each state has a file containing state-specific sub-reddits to search, for example, wv.dat for West Virginia. I'm moving toward two-letter abbreviations for the state filenames but haven't completed that yet.

Subs that get searched by every election are in standardsubs.dat.

## Developing ##

I'd rather people didn't run this with their own accounts, as duplicate content will likely get us both banned. I actually can't think of how to test the code you write, but if you submit a PR, I'm happy to give it a try on my account.

## Contributing ##

Please create a new branch and pull request for changes you'd like to make.

Some things I'd love to do:
1. Check if a given script is already running before starting it.
2. Use a template instead of 50+ very similar election files.
3. Move state files to a states folder and election files to an elections folder (and fix all the relevant paths).
4. Use stream watching rather than searching.
5. Build and use an API.
6. Figure out how to make this work for multiple contributors.
