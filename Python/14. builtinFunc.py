#len() function: Returns the length of an object
list1 = ['physics', 'chemsitry', 'math', 'physics']
print(list1)
print('length=', len(list1))
list2 = list(range(5))
print(list2)
print('length=', len(list2))

#max() function: Returns the largest item in an iterable
list1, list2 = ['C++', 'Python', 'Java'], [125, 20, 200]
print(list1, list2)
print("max value element of list1: ", max(list1))
print("max value element of list2: ", max(list2))

#min() function: Returns the smallest item in an iterable
list1, list2 = ['C++', 'Python', 'Java'], [125, 20, 200]
print(list1, list2)
print("min value element of list1: ", min(list1))
print("min value element of list2: ", min(list2))

#list() function: Returns a list
aTuple = (123, 'abc', 'Python', -5)
print(aTuple)
list1 = list(aTuple)
print('List elements: ', list1)

str = 'Hello World'
list2 = list(str)
print("List elements: ", list2)