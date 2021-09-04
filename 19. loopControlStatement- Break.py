for letter in 'Python':     # First Example
    if letter == 'h':
        break
    print('Current letter: ', letter)

var = 10       # Second Example
while var > 0:
    print('Current variable value: ', var)
    var -= 1
    if var == 5:
        break
print('Good bye')

id = [1,2,3,4,5]        # Third Example
print(id)
x = int(input('enter a number: '))
for i in range(len(id)):
    if x == id[i]:
        break
    print(id[i])
if i < len(id)-1:
    print(x, 'found at position: ', i+1)
else:
    print(x, 'not found in list')
