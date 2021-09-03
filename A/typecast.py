# converting the type
a=20
b="1234"
str(a)
int(b)
print(type(a))
print(type(b))
# IMPLICIT TYPE CONVERSION :- it automatically converts one data type to another ithout any user involve ment needed
a=int(90.5) #data loss will take place(lower to higher dt conversion)
print(a)
# python avoids data loss in implicit type conversion

# EXPLICIT TYPE CONVERSION
# user convert the dat type of an object to required dat type
b=int('90')
print(b)
