count = 100

def addCount():
    # Uncomment the following line to fix the code
    global count
    count = count+1

print(count)
addCount()
print(count)

#error: 
# UnboundLocalError: local variable 'count' referenced before assignment