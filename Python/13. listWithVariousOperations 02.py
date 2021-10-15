list = ['abcd', 123, 'john doe', 2.25]
tinylist = [789, 'fulan']

print(list, tinylist)   #print complete list
print(list[2:3])
print(list[2:])
print(tinylist*2)
print(list + tinylist)   #prints concatenated lists


## list object methods
# append() clear() copy() count() extend() index() insert() pop() remove() reverse() sort()

#append() method: Adds an element at the end of the list
print("append() method")
list1 = ['C++', 'Java', 'Python']
list1.append('PHP')
print('Updated list: ', list1)

#count() method: Returns the number of elements with the specified value
print('count() method')
list2 = [123, 'abc', 'xyz', 123]
print(list2)
print('Count for 123: ', list2.count(123))
print('Count for abc: ', list2.count('abc'))

#extend() method: Add the elements of a list (or any iterable), to the end of the current list
print('extend() method')
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
print(fruits, cars)
fruits.extend(cars)
print('extended list: ', fruits)

# index() method: Returns the index of the first element with the specified value
print("index() method")
list1 = ['C++', 'Java', 'Python', 'Java']
print(list1)
print('Index of Java: ', list1.index('Java'))
# print('Index of PHP: ', list1.index('PHP'))     #'PHP' is not in list

#insert() method: inserts the specified value at the specified position.
print('insert() method')
fruits = ['apple', 'banana', 'cherry']
print(fruits)
fruits.insert(1, 'grasp')
print('Final list: ', fruits)

#pop() method: Removes the element at the specified position
print('pop() method')
obj = fruits.pop()      # popped last element
print('popped: ', obj)
print('fruits now: ', fruits)
obj = fruits.pop(1)     #popped specified index elemnt
print('popped: ', obj)
print('fruits now: ', fruits)

#remove() method: Removes the first item with the specified value
print('remove() method')
books = ['physics', 'chemistry', 'math', 'biology', 'math']
print(books)
books.remove('math')
print('list now: ', books)

#reverse() method: Reverses the order of the list
print('reverse() method')
books = ['physics', 'chemistry', 'math', 'biology', 'math']
print('initial list: ', books)
books.reverse()
print('reverse list now: ', books)

#sort() method: sorts the order of the list
print('sort() method')
books = ['physics', 'chemistry', 'math', 'biology', 'math']
print('initial list: ', books)
books.sort()
print('sorted list now: ', books)