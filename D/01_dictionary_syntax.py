# Dictionary syntax;-Collection of key vlaue pairs(it's mutable likelist and unlike tuples)
# eg.
# syntax- dictname={"key":"value"}
myDict={"coding":"fun","black":"colour","dict2":{ "num1":"23","num2":"45"} }

print(myDict["coding"])
print(myDict["black"])
print(myDict["dict2"])# nested dictionary(dict inside a dict)

# using loop
a=[{"item":"phone"},{"item":"laptop"},{"item":"charger"}]
x=(i['item'] for i in a)
print(*x)
