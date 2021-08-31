# print("Hello World")

# print('''hello
# people''')

# print('hello \
# world')

import sys
print('Number of argument:', len(sys.argv), 'arguments')
print('Argument list:', str(sys.argv))
x= int(sys.argv[1])
y= int(sys.argv[2])

z = x+y
print("X=",x,"Y=",y,"Z=",z)