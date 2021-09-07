# creating a empty set
a=set()

# adding values in an empty set
a.add(3)
a.add(1)
a.add(4)
a.add((56,78,89))  #only tuples can be added in the sets as both are unchangable 
                   #whereas dictionary and lists cannot be added
print(a)
# removing values
a.remove(1)
#a.remove(6)#error since 6 is not present in the list

print(len(a)) #rturns the length of set

print(a.pop()) #removes any random value from the set
print(a)

a.clear()#empties the set
print(a)
