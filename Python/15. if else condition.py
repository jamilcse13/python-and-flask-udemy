# if
discount = 0
amount = int(input('enter amount: '))

if amount>1000:
    discount = amount*0.1
print('Discount=', discount)
print('Net amount=', amount-discount)


# if else
discount = 0
amount = int(input('enter amount: '))

if amount>1000:
    discount = amount*0.1
else:
    discount = amount*0.05
print('Discount=', discount)
print('Net amount=', amount-discount)


# if elif else
discount = 0
amount = int(input('enter amount: '))

if amount>1000:
    discount = amount*0.1
elif amount>500:
    discount = amount*0.05
else:
    discount = 0
print('Discount=', discount)
print('Net amount=', amount-discount)

# single statement suits
marks = int(input('enter marks: '))
if marks >= 50: print("pass")
else: print("fail")