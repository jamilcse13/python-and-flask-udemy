tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1,2,3,4,5)
print(tup1, tup2)
print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])
input("continue")

#updating
print("update example")
tup1 = (12,34,56)
tup2 = ('abc', 'xyz')
print(tup2, tup1)
# tup1[0] = 100
input("continue")

# let's create a new tuple as follows
tup3 = tup1 + tup2
print('new tuple:', tup3)

#delete
print("delete example")
tup = ('physics', 'chemistry', 1997, 2000)
print('before deleting:', tup)
del tup
print('After deleting tup:')
# print(tup)

#indexing and slicing
tup = ('C++', 'Python', 'Java')
print(tup)
print('tup[2]', tup[2])
print('tup[-2]', tup[-2])
print('tup[1:]', tup[1:])