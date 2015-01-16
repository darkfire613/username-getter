#username-getter
#Grabs usernames from reddit, checks them by a set of rules
#Owen Monsma darkfire613@icloud.com
#January 15, 2015

import praw


user_agent = ("username skimmer 0.1 by /u/darkfire613")
r = praw.Reddit(user_agent = user_agent)
