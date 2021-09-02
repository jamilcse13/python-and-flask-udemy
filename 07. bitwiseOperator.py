a = 60          # 60 = 00111100
b = 13          # 13 = 00001101
print('a=',a,':',bin(a),'b=',b,':',bin(b))
c = 0

c = a & b
print('result of a & b is', c, ':',bin(c))

c = a | b
print('result of a | b is', c, ':',bin(c))

c = ~a          # -61 : -0b111101
print('result of COMPLEMENT ~a is', c, ':',bin(c))

c = a<<2        # 240 : 0011110000
print('result of LEFT SHIFT a<<2 is', c, ':',bin(c))

c = a>>2        # 15 : 00001111
print('result of RIGHT SHIFT a>>2 is', c, ':',bin(c))