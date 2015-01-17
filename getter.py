# getter.py
# Grabs usernames from reddit
# Owen Monsma darkfire613@icloud.com
# January 16, 2015

import praw
import time

# initializes reddit api stuff
user_agent = ("username getter 0.1 by /u/darkfire613 "
              "https://github.com/darkfire613/username-getter")
r = praw.Reddit(user_agent = user_agent)

# load sublist
sublist = []
with open('sublist') as file:
    for line in file:
        sublist.append(line)
file.close()

# strip newlines
sublist = [x.strip() for x in sublist]

# main loop
while true:
    for subname in sublist:
        subreddit = r.get_subreddit(subname)
        for submission in subreddit.get_new(limit=10):
            username = submission.author
            print username
    time.sleep(1800)
