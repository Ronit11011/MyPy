  # find max of 4 numbers entered by the user
num1=int(input("First"))
num2=int(input("second"))
num3=int(input("third"))
num4=int(input("Fourth"))
if(num1>num2 and num1>num3 and num1>num4):
    print("Num1 is largest")
elif(num2>num1 and num2 >num3 and num2 >num4):
    print("Num2 is largest")
elif(num3>num1 and num3>num2 and num3>num4):
    print("num3 is largest")
else:
    print("num4 is largest")            
    
    
    
    # find whether th entered name is present in th slist or not
a=["Ronit","ab","cd","alpha","gamma","beta"]
enter=input("enter the name : ")
if(enter in a):
    print("name is present")
else:
    print(" name is not present")
