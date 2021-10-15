#Function definition is here
sum = lambda arg1, arg2 : arg1 + arg2

# Now you can call sum as a function
print("Value of total: ", sum(10,20))
print("Value of total: ", sum(20,20))
input()


# Return Argument
def sum(arg1, arg2):
    "Add both the parameters and return them"
    total = arg1+arg2
    print("Inside the function: ", total)
    return total

# Now you can call the sum function
total = sum(10,20)
print("Outside the function : ", total)

# Inside the function:  30
#Outside the function :  30

#without return total
#Inside the function:  30
#Outside the function :  None