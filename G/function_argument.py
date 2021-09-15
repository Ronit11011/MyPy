# functions as arguments
def add(a,b):
    return a+b

def calc(func,a,b):
     result=func(a,b)
     return result

print(calc(add,23,45))
