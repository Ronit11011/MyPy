# Q.1 create a dictionary of hindi to english word return the english
# meaning of th hindiword nteed by the user

a={
    "balla":"bat",
    "gadi":"Vehicle",
    "tasveer":"photo"
}

print("Options ar as follows :",a.keys())
word=input("enter the hindi word :\n ")
print("Meaning is : ",a[word])
print("Meaning is : ",a.get(word)) #to avoid error if entered word is invalid

# Q.2 Take 8 numbers from user and display all the unique numbers.
a=input()
b=input()
c=input()
d=input()
e=input()
f=input()
g=input()

cet={a,b,c,d,e,f,g}
print(cet)

# ---->Imp:- If in a set two values are same but there type are diiferent
#  i.e  int(6) and str(6) then they can be present in aset since there type are different
s={10,"10",10.1}
print(set) 

# Q.3 create a dict of indexes and their value are entered by user
dict={}
a=input()
b=input()
c=input()
d=input()
dict['a enters']=a
dict['b enters']=b
dict['c enters']=c
dict['d enters']=d
print(dict)



