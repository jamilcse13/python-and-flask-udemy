## triple quotes
str = '''
this is a long string 
and here is a tab ( \t ) so what
we use next line? a new 
line [ \n ] is perfect, right?
'''
print(str)

#use of raw string
#first \ will be used for escaping
print('C:\\demo')

#raw string ignores escape char
print(r'C:\\demo')


## string encoding functions
import base64
str = "this is string example...wow!!"
str = base64.b64encode(str.encode('utf-8'))
print("Encoded String: ", str)
str = base64.b64decode(str.decode('utf-8'))
print("Decode String: ", str)