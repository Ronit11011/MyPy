# Indexing:-
# string = r  o  n  i  t
# index =  0  1  2  3  4
# neg.in= -5 -4 -3 -2 -1 (used if we have to access elemnt from last if we 
#                         does not know the size of the string)
# ----------------------------------------
# Adding strings
first="Good morning "
second="Buddy"
c=first +second
print(c)
# accesing elements known as slicing 
name="Light"
print(name[0],name[4])
print(name[0:3])#print from 0 to 2
print(name[:5]) #it will automatically take lower limit as minimum possible
print(name[0:])#same as above  

# slicing with skipping values
name="Howareyou"  
d=name[0::2]#every 2nd element will be printed
print(d)

# string functions
x="hello this is python string functions"
print(len(x))#will print total char.
print(x.endswith("functions"))#true if yes or false
print(x.count("f"))#total no.of that characters!
print(x.count("on"))
print(x.capitalize())#Capitalize the first letter of the first word
print(x.find("python"))#print the position of that word or -1 if not present
print(x.replace("python","C++"))#for replacing a word with another word
