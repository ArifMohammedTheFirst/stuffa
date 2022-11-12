import os
def cleanedup(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789_@'
    cleantext = ''
    for character in s.lower():
        if character in alphabet:
            cleantext += character
        else:
            cleantext += ' '
    return cleantext

def findMentions(p):
    mentions = {}
    tz = []
    with open(p) as file:
        for lines in file:
            for word in cleanedup(lines).split():
                if word in mentions:
                    mentions[word] += 1
                else:
                    mentions[word] = 1
    
    for word in mentions:
        if '@' in word:
            tz.append([mentions[word],word])
            
    tz.sort()
    x = -2
    while x < 1:
        y = 1
        while y < 2:
            print('     ',tz[x-1][1],tz[x-1][0])
            y +=1
        x += 1 
    return''

for filename in os.listdir('.'):
    if os.path.isdir('..'):
        if '.tweets' in filename:
            print(filename)
            print(findMentions(filename))
