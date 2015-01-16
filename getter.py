# getter.py
# Grabs usernames from reddit
# Owen Monsma darkfire613@icloud.com
# January 15, 2015

import praw

user_agent = ("username skimmer 0.1 by /u/darkfire613 "
              "https://github.com/darkfire613/username-getter")
r = praw.Reddit(user_agent = user_agent)

sublist = ('sublist', r)
