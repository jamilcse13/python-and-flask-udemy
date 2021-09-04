for letter in 'Python':     # First Example
    if letter == 'h':
        continue
    print('Current letter: ', letter)

var = 10       # Second Example
while var > 0:
    var -= 1
    if var == 5:
        continue
    print('Current variable value: ', var)
print('Good bye')

pwd = "@#$"     #Third Example
while (True):
    x = input("password: ")
    if x!= pwd:
        print("enter again")
        continue
    print("password entered correctly")
    break


#The pass statement is used as a placeholder for future code.
#When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed.
#Empty code is not allowed in loops, function definitions, class definitions, or in if statements.

def myfunction():
    pass

# having an empty function definition like this, would raise an error without the pass statement

a = 33
b = 200

if b > a:
    pass