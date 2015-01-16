# getter.py
# Grabs usernames from reddit
# Owen Monsma darkfire613@icloud.com
# January 16, 2015

import praw

#initializes reddit api stuff
user_agent = ("username skimmer 0.1 by /u/darkfire613 "
              "https://github.com/darkfire613/username-getter")
r = praw.Reddit(user_agent = user_agent)

#load sublist
sublist = []
with open('sublist') as file:
    for line in file:
        sublist.append('/r/' + line)
file.close()

#strip newlines
sublist = [x.strip() for x in sublist]

print sublist
