#BREAK:-for breaking the loop
for i in range(10):
    print(i)
    if(i==4):
        break   

# CONTINUE :-for skipping some values
# for example:-if only odd values are to be printed
for i in range(1,20):
    if(i%2==0):
        continue    #when i will be even it will skip the print function an move to the next value.
    print(i)

    # PASS:- instructs to  "do nothing"
    # eg:to print odd int
    for i in range(1,20):
        if(i%2==0):
            pass
        else:
            print(i)
