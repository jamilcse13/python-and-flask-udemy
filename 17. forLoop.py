for letter in 'Python':
    print('Current letter: ', letter)

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:
    print('Current fruit: ', fruit)
print('Good bye!')


# for loop using range()
for num in range(5):
    print(num)

print("range(start, stop)")
for num in range(1,5):
    print(num)

print("range(start, stop, step)")
for num in range(1,6,2):
    print(num)
else:
    print('good bye!')


## iterating by sequesnce index
dict = {'011':'Dhaka', '022':'Chattogram', '033':'Rangpur'}
print(dict)
for key in dict:
    print(dict[key])        #get the value using key

for key,value in dict.items():
    print(key, ':', value)

for val in dict.values():
    print(val)

for key in dict.keys():
    print(key)