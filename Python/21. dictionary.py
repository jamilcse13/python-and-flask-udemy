dict = {'Name': 'Zara', 'Age': '7', 'Class': 'First'}
print(dict)
print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])
# print("dict['key']: ", dict['key'])       #error
input()

#update
print("Update dictionary")
dict['Age'] = 8     #update existing entry
dict['School'] = 'DPS School'    #Add new entry
print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])
print("after update: ", dict)
input()

#delete
print("deleting from Dictionary")
dict = {'Name': 'Zara', 'Age': '7', 'Class': 'First'}
print("initial dictionay: ", dict)
del(dict['Name'])   #remove entry with key 'Name'
print("dictionay after removing elements: ", dict)
dict.clear()    #remove all entries in dict
print("dictionay after clear: ", dict)
del dict    #delete entire dictionay

print("dict['Age']: ", dict['Age'])     #error as dict is empty