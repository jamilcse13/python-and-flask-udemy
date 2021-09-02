# logical
a = 5
print('AND operation of a>3 and a<10:', a>3 and a<10)

print('OR operation of a<5 or a<4:', a<5 or a<4)

print('NOT operation of not(a<5 and a<10):', not(a<5 or a<4))


# membership
a = 10
b = 20
list = [1,2,3,4,5,6]
print(list)
print("a=",a,"b=",b)

if (a in list):
    print("Line 1 - a is vailable in the given list")
else:
    print("Line 1 - a is not vailable in the given list")

if (b not in list):
    print("Line 2 - b is vailable in the given list")
else:
    print("Line 2 - b is not vailable in the given list")