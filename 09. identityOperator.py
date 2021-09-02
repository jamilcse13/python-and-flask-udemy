a = 20
b = a
print('a=',a,':',id(a), 'b=',b,':',id(b))

if (a is b):
    print("a and b have same identity")
else:
    print("a and b do not have same identity")

if ( id(a) == id(b) ):
    print("a and b have same identity")
else:
    print("a and b do not have same identity")

b = 30
if (a is not b):
    print("a and b do not have same identity")
else:
    print("a and b have same identity")


x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
# returns True because z is the same object as x

print(x is y)
# returns False because x is not the same object as y, even if they have the same content

print(x == y)
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y
