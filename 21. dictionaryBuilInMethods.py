#clear() method: Removes all the elements from the dictionary
print("clear() method")
dict = {'Name': 'Zara', 'Age': 7}
print("Start len: %d" %len(dict))
dict.clear()
print("End len: %d" %len(dict))

#copy() method: Returns a copy of the dictionary
print("copy() method")
dict1 = {'subjects':['phy', 'che']}
print("dict1: ", dict1)
dict2 = dict1.copy()
print("New Dictionary: ", dict2)
dict2['subjects'].append('maths')
print("dict1: ", dict1)
print("dict2: ", dict2)
input()

#fromkeys() method: Returns a dictionary with the specified keys and value
print("fromkeys() method")
seq = ('name', 'age', 'sex')
dict = dict.fromkeys(seq)       #value optional
print("New Dictionay: ", dict)
dict = dict.fromkeys(seq, 10)
print("New Dictionay: ", dict)
input()

#get() method: Returns the value of the specified key
print("get() method")
dict = {'Name': 'Zara', 'Age': 7}
print("get('Age'): ", dict.get('Age'))
print("get('Sex'): ", dict.get('Sex'))
input()

#items() method: 	Returns a list containing a tuple for each key value pair
print("items() method")
print("k-v pairs: ", dict.items())

#keys() method: Returns a list containing the dictionary's keys
print("keys() method")
dict = {'Name': 'Sara', 'Age': 8}
print("list of keys: ", dict.keys())

#values() method: Returns a list containing the dictionary's values
print("values() method")
print("list of values: ", dict.values())

#setdefault() method: Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
print("setdefault() method")
dict.setdefault("Class", None)
dict.setdefault("Age", 12)
print(dict)
input()

#update() method: Updates the dictionary with the specified key-value pairs
print("update() method")
dict = {'Name': 'Zara', 'Age': 7}
dict2 = {'Sex': 'Male'}
print(dict, dict2)
dict.update(dict2)
print("updated dict: ", dict)
input()

#pop() method: Removes the element with the specified key
print("pop() method")
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print("car: ", car)
car.pop("model")
print("updated car: ", car)

#popitem() method: Removes the last inserted key-value pair
print("popitem() method")
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print("car", car)
car.popitem()
print(car)