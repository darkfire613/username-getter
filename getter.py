# getter.py
# Grabs usernames from reddit
# Owen Monsma darkfire613@icloud.com
# January 16, 2015

import praw
import time

# initializes reddit api stuff
user_agent = ("username getter 0.2 by /u/darkfire613 "
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

#load placeholder placeholders
placeholders = []
for x in sublist:
    placeholders.append('1bu7ak')

# main loop
while True:
# subcount is an iterator for filling the placeholder
    subcount = 0
    f = open('userlist', 'a')
    for subname in sublist:
        subreddit = r.get_subreddit(subname)
        print placeholders[subcount]
        firstloop = True
        for submission in subreddit.get_new(limit=25, place_holder=placeholders[subcount]):
            if firstloop:
                placeholders[subcount] = submission.id
                firstloop = False
            else:
                username = submission.author
                f.write(str(username) + '\n')
        subcount += 1
    f.close()
    print placeholders
    #break
    time.sleep(5)
