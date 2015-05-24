# checker.py
# Checks grabbed usernames according to rules
# Owen Monsma darkfire613@icloud.com
# January 18, 2015

import enchant

# functions

def HasNumbers (inputstring):
    return any (char.isdigit() for char in inputstring)

def IsWord (inputstring):
    isWord = False
    languagelist = []
    with open ('languagelist') as file:
        for line in file:
            languagelist.append(line)
    file.close()
    languagelist = [x.strip() for x in languagelist]

    for language in languagelist:
        d = enchant.Dict(language)
        if d.check(inputstring):
            print language
            isWord = Truee 
    return isWord

def FlipWord (word):
    # string slicing is stupid. python is stupid
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

# passedusers stores all the usernames that pass the check
passedusers = []

# main loop

# removes if it has a number
for user in userlist:
    print 'checking: ' + user
    checkname = user.capitalize()
    backword = FlipWord(user)
    backword = backword.capitalize()
    if IsWord(checkname) or IsWord(backword) and not HasNumbers(checkname):
        passedusers.append(user)

with open('passedusers', 'a') as file:
    for name in passedusers:
        file.write(name + '\n')
