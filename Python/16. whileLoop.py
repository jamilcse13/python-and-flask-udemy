count = 0
while count<10:
    count += 1
    print("count=", count)
print("good bye!")


## while loop else statement
count = 0
while count<10:
    print(count, "is less than 10")
    count += 1
else:
    print(count, "is not less than 10")
print("good bye!")


# single statement suits
flag = 1        #it eill be an infinite loop
# while (flag): print('Given flag is really true! ')
print('bye bye!')


## infinite loop: break by pressing ctrl+c
var = 1
while var ==1:      #it generates an infinite loop
    num = int(input("Enter a number: "))
    print("You entered: ", num)
print("Good bye!")