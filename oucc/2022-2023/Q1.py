vowels = set(['a', 'e', 'i', 'o', 'u'])
consonants = set(['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w' ,'x', 'y', 'z'])

string = input('')

vowelcount = 0
consonantcount = 0

for letter in string.lower():
    if letter in vowels:
        vowelcount += 1
    elif letter in consonants:
        consonantcount += 1

print(f'{vowelcount} {consonantcount}')
