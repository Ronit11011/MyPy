mydict={"coding":"fun","black":"colour","dict2":{ "num1":"23","num2":"45"} }

# functions
print(mydict.keys())#print the keys of the ditionary
print(list(mydict.keys())) #print the keys in the form of the list
print(mydict.items())#print all the items in the list

# Updating a list
upd={                   #list to be added
"socrates":"philosopher",
"picasso":"painter",
"ronaldo":"footballer",
"black":"dark"   # since it was present  already in th dict hence the value in that particular key will be updated 
}
print(mydict)
mydict.update(upd) #function to update a list
print(mydict)      #updated list
print(mydict['ronaldo'])

print(mydict.get("black"))#will return value associlated with blue key
print(mydict["black"])    #will return value associlated with blue key

#  diiference b/w them :-
print(mydict.get("blue"))#will "return none" as blue is not present in the list
print(mydict["blue"])    #will "throw error" as blue is not present in the list