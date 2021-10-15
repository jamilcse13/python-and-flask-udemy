print("C:\\User\\user\\mydata.txt")
print("this is having a new line \ncharacter")
print("this is having a tab \tcharacter")
print("ABC written in \x41\x42\x43 (HEX) representation")


## format() method

# default(implicit) order
default_order = "{} {} and {}".format('Today', 'is', 'Sunday')
print(default_order)

#order using positional argument
positional_order = "{1} {0} and {2}".format('is', 'Today', 'SUnday')
print(positional_order)

#order using keyword argument
keyword_order = "{j} {i} and {k}".format(i='is', j='Today', k='SUnday')
print(keyword_order)


# formatting numbers
print("Required binary representation of {0} is {0:b}".format(20))

# formatting floats
print("Exponent representation: {0:e}".format(1566.345))

# round off
print('One third is: {0:.3f}'.format(1/3))


## string methods
print("gOOd moRniNg tO alL".lower())
print("gOOd moRniNg tO alL".upper())
print("gOOd moRniNg tO alL".find('tO'))
print("gOOd moRniNg tO alL".find('to'))
print("gOOd moRniNg tO alL".replace('alL', 'everybody'))
print("gOOd moRniNg tO alL".replace('all', 'everybody'))