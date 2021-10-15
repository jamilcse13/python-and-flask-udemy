total = 0   #global variable
#Function definition is here
def sum(arg1, arg2):
    "Add both the parameters and return them"
    total = arg1+arg2   #local variable
    print("Inside the function local total :", total)
    return total

#Now you can call sum function
sum(10,20)
print("Outside the function global total :", total)