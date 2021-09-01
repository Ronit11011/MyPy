a=[10,20,30,40,50]
a.append(200)#it will add in the end of the list
# for adding in specific index
a.insert(3,400)
# for removing specific value
a.remove(30)
# removing:- by index
a.pop(0)
# -----------------------
print(*a)#for printing a whole list it is wriiten like this "*list"
b=[1,2,3,4,5] 
b.append(6)
c=(a,b)
print(*c)
print(c[0][2])