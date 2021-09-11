tuple1, tuple2 = (122, 'abc', 'xyz'), (456, 'mno')
#len() function
print('len() function')
print(tuple1, tuple2)
print('First tuple length: ', len(tuple1))
print('Second tuple length: ', len(tuple2))
input()

#max() function
tuple1, tuple2 = ('math', 'abc', 'xyz'), (456, 222, 756, 125)
print('max() function')
print(tuple1, tuple2)
print('Max value of tuple1: ', max(tuple1))
print('Max value of tuple2: ', max(tuple2))
input()

#min() function
tuple1, tuple2 = ('math', 'abc', 'xyz'), (456, 222, 756, 125)
print('min() function')
print(tuple1, tuple2)
print('Min value of tuple1: ', min(tuple1))
print('Min value of tuple2: ', min(tuple2))
input()

#tuple() function
list1 = ['maths', 'che', 'phy', 'bio']
print('tuple() function')
print(list1)
tuple1 = tuple(list1)
print('Tuple from list1: ', tuple1)
print('Tuple from string: ', tuple('Hello'))