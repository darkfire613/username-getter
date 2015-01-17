Username Getter
===============

This program scans the usernames of new posts to a specified subreddit, then checks the usernames against a set of arbitrary rules. The purpose is to find a given account by the rules provided.

Note you will need to provide a list of subreddits to scan in a file named "sublist", one subreddit per line. Without this, the program will default to scanning /r/all. The program automatically appends /r/ so don't worry about it.

The program comes in two parts: getter.py, which is a bot that continues to grab reddit usernames for as long as it's allowed to run, saving them into userlist. The second, checker.py, runs once, and scans userlist, filtering based on its rules.
