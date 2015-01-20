# checker.py
# Checks grabbed usernames according to rules
# Owen Monsma darkfire613@icloud.com
# January 18, 2015

# import enchant

# functions

def HasNumbers (inputstring):
    return any (char.isdigit() for char in inputstring)

def CheckIfWord (inputstring):
    # TODO: check if string is a word using enchant
    return False

def FlipWord (word):
    # why does this flip a string? I dont know. I hate python.
    word = word[::-1]
    return word

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

with open('passedusers', 'a') as file:
    for name in passedusers:
        file.write(name + '\n')

print '\nafter:'
print passedusers
