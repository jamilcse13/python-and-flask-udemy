## different ways to define a string
mystr1 = 'Hello'
print(mystr1)

mystr2 = "Helloow"
print(mystr2)

mystr3 = '''heyyy'''
print(mystr3)

mystr3 = '''Hello
man, how are
you?'''
print(mystr3)

## accessing characters in string
mystr = 'language'
print('mystr = ', mystr)
print("mystr[0] = ",mystr[0])
print("mystr[-1] = ",mystr[-1])
print("mystr[1:5] = ",mystr[1:5])
print("mystr[5:-2] = ",mystr[5:-2])
print("mystr[:2] = ",mystr[:2])
# print("mystr[10] = ",mystr[10])

##strings are immutable
## but different strings can be assigned
mystr = 'language'
print(mystr)

mystr = 'programming'
print(mystr)

mystr[3] = 'a'