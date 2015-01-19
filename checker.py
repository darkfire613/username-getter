# checker.py
# Checks grabbed usernames according to rules
# Owen Monsma darkfire613@icloud.com
# January 18, 2015

import enchant

# functions

def HasNumbers (inputstring):
    return any (char.isdigit() for char in inputstring)

def CheckIfWord (inputstring):
    # TODO: check if string is a word
    return False


# load list
userlist = []
with open('userlist') as file:
    for line in file:
        userlist.append(line)
file.close()

# strip newlines from list
userlist = [x.strip() for x in userlist]

print '\nbefore:'
print userlist

# passedusers stores all the usernames that pass the check
passedusers = []

# main loop
for user in userlist:
    print 'checking: ' + user
    if not HasNumbers(user):
        passedusers.append(user)

print '\nafter:'
print passedusers
