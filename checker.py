# checker.py
# Checks grabbed usernames according to rules
# Owen Monsma darkfire613@icloud.com
# January 18, 2015

import enchant

# load list
userlist = []
with open('userlist') as file:
    for line in file:
        userlist.append(line)
file.close()

# strip newlines from list
userlist = [x.strip() for x in userlist]
