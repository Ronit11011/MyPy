# write a funtion to return greatest of three numbers
def gr8(a,b,c):
    if(a>b  and  a>c):
        return a
    elif(b>a and b>c):
        return b    
    else:
        return c  

a=int(input())         
b=int(input())         
c=int(input())  
print(gr8(a,b,c))   

# printing patterns
def pattern(n):
    for i in range(1,n+1):
        print("*" * (n+1-i) )

n=int(input())
pattern(n)        
