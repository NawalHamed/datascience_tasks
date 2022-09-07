#Python Tasks, part2

#1
def Print(x = 0,y = 0):
    print("The given 2 numbers are: ", "x: " , x, "y: " , y)
   

def Print2(x = 0,y = 0):
    return (x,y)

Print(1,2)

z = Print2(2,3)
print("print the stored returned values x, y:" , z)
#2
Print(x =9)
Print(y =5)
#3

Print()


#4
print("---using def function---")
def Sum(*numbers):
    s = 0
    for n in numbers:
        s+=n
        if numbers.index(n) == (len(numbers)-1):
            print(s)
Sum(4,5)
Sum(1,2,7)

'''lambda function is an anonymous function (i.e., defined without a name) that can take any number of arguments but,
unlike normal functions, evaluates and returns only one expression'''

#5,6
print("---using lambda function---")

c = (lambda a,b: a+b)(1,2)
print("the result of lambda is:" , c)
#7
'''Local variables can only be reached within their scope(like func() above).
A global variable can be used anywhere in the program as its scope is the entire program.'''
