# Creating a list using [ ]
a=[1,2,3,4,5,6]

# printing a list using print() funcntion
print(a) #printing in original format i.e using [ ] and ,
print(*a) #printing just the element in the list

# accesing the elements in the list
print(a[0],a[4])

# elements can be change in the list also
a[0]=30
a[1]=20
print(a)

# diferent types of the elements can be stored in the sam list!
b=[12,"",12.34,True]
print(b)
print(*b)
