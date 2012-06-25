def do(thing):
    return str(thing) + str(1)
do(5)
print do(5)


def do(one,two=5):
    return one+two
do(5)
print do(5)



def do(a,b):
    a=5
    b=5
    return a*b
inp = 8
do(inp,5)
print inp



def try_to_change_list_contents(the_list):
    the_list.append('four')
outer_list = ['one','two','three']
try_to_change_list_contents(outer_list)
print outer_list


def do(a,f):
    return a*f(a)
def inp(a):
    return a*2
print do(6,inp)


#problem 2
x = input("enter a number:")

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)
print factorial(x)

#problem 3

def fib(n):
    if fib



    
    
    









