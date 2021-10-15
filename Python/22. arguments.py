#required arguments
#Function definition is here
def printme(str):
    "This prints a passed string into this function"
    print(str)
    return

# Now you can call the function
printme("a")
input()


#keyword arguments
def printinfo(name, age):
    "This prints a passed string into this function"
    print("Name: ", name)
    print("Age: ", age)
    return

# Now you can call the function
printinfo("xyz", 20)
printinfo(age=50, name="miki")
input()


#default arguments
def printinfo(name, age=35):
    "This prints a passed string into this function"
    print("Name: ", name)
    print("Age: ", age)
    return

# Now you can call the function
printinfo("xyz")
printinfo(age=50, name="miki")