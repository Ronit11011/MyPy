from decimal import *
a=0.1
b=0.2
c=a+b
print(c)#This will print a ans with no acurate precision
y=Decimal('0.1')  # for accurate precision
x=Decimal('0.2')
z=x+y
print(z)
