list1 = ['bangladesh', 'physics', 1999, 2001]
print(list1[0])

list2 = [1, -2, 3+4j, 4, 6.25]
print("list2 : ", list2)

list3 = ["a", "b", 'c', "d"]
print("list3 : ", list3)

#access
print("list3[2] : ", list3[2])
print("list3[1:4] : ", list3[1:4])

#update
list3[1] = 123
print(list3)

#add
list3.append('acv')
print(list3)

#delete particular element
list3.remove("c")   #using value
print(list3)

del list2[0]   # using index
print(list2)

# delete the entire list
del list1
print(list1)