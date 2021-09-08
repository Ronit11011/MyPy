# printing the simplest pattern
# *
# **
# ***
n=int(input())
# for i in range(1,n+1):
#     print("*"*(i))

# moving one-step ahead:-Pyramid pattern
for i in range(1,2*n):
    if(i%2==0):
        continue
    f=1
    while(f<=(n-1-(i-1)/2)):
        print("",end=" ")
        f+=1
    print("*"*(i))

    # hollow square pattern
for i in range(1,n+1):
    if(i==1 or i==n):
        print("* " * n)
    else:
        print(" * "," " * (n-2)," * ",sep=" ")    

            
