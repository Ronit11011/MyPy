# check whether number is prime or not
num=int(input("enter the no. : "))
prime=True
for i in range(2,num):
    if(num%i==0):
      prime=False
    
if(prime==True):
    print("number is prime")
else: 
    print("number is not prime")
    
