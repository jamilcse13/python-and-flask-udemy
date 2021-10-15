#structure of a function
# def functionName(parameters):
#     "function_docstring"
#     function_suite
#     return [expression]
# fuctionName(parameters)

# Function Definition is here:
def printme(str):
    "This prints a passed string into this funstion"
    print(str)
    return

#Now we can call printme function
printme("This is the first call to the user defined function")
printme("Again second call to the same function")
printme("Third call from ")
input()

#Pass by reference
def changeme(mylist):
    "This changes a passed list into this function"
    print(id(mylist))
    print("values inside the function before change: ", mylist)
    mylist[2] = 50
    print("values inside the function before change: ", mylist)
    print("Id after change: ", id(mylist))
    return

# Now you call the changeme function
mylist = [10,20,30]
print(id(mylist))
changeme(mylist)
print("Values outside the function: ", mylist)
input()

#example 2
def changeme(mylist):
    "This changes a passed list into this function"
    mylist = [1,2,3,4]      #this would assign a new reference in mylist
    print(id(mylist))
    print("values inside the function: ", mylist)
    return

# Now you call the changeme function
mylist = [10,20,30]
print(id(mylist))
changeme(mylist)
print("Values outside the function: ", mylist)