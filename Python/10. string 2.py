## concatenation of strings
mystr1 = 'welcome'
mystr2 = ' to all'

# using +
print('mystr1 + mystr2 = ', mystr1 + mystr2)

# using *
print('mystr1 * 3 = ', mystr1 * 3)


## iterating through a string
letter_count = 0
for letter in 'Hello World':
    if (letter == 'l'):
        letter_count += 1
print(letter_count,'times l letter has been found')

## string membership
print('l' in 'hello')
print('l'  not in 'hello')
print('a' in 'hello')
print('a'  not in 'hello')

## built-in function
mystr = 'university'

# using u= enumerate()
my_list_enumerate = list(enumerate(mystr))
print('list(enumerate(mystr))', my_list_enumerate)

print('len(mystr) = ', len(mystr))


## string formatting using escape sequence
# print("tell me "What's your name?"")

#using triple quotes
print('''tell me "What's your name?"''')

#escaping single quotes
print('tell me "What\'s your name?"')

#escaping single quotes
print("tell me 'What\'s your name?'")

#eacaping double quotes
print("tell me \"What's your name?\"")