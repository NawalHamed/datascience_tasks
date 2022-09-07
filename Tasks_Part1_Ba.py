#Python Tasks, Part1

m = True #Boolean variable
y = 5 #integer variable
z = 2.5 #float variable
s = 'Nawal' #string variable
s1 = '10'

#----------------------------

A = float(y)
print(type(A))

#----------------------------
# Can we convert the str to int ?
B1 = int(s1) #can not convert any string it should be of base 10
#B = int(s)
print(B1)
#print(B)

#----------------------------

L = [1,2,3,4,5]
T = (10,11,12,13,14,15)

print(tuple(L))

#---------------------------

Dict = {'Nawal' : 25 , 'Manal' : 47 , 'Eman' : 17}

#----------------------------
x = 3
#; used only in splitting statements and to write loops in 1 line
print('I') ; print('Love') ; print('Data')

#using for loop
for i in range (2): print ('Hi') ; print('Python Class')

#----------------------------
#Python is interpreted or compiled ?
'''Python is a “COMPILED INTERPRETED” language. Compiles and converts it to bytecode,
and directly bytecode is loaded in system memory. Then compiled bytecode interpreted from memory to execute it.'''

#----------------------------
#what is the difference between low level & high levelv
'''High-level language and low-level language are the types of programming languages. The prior difference between high level and
low-level language is that the high-level language is easily interpreted by programmers but
not machines whereas low-level language can be easily understood by machines but not by humans.'''
#and more
'''Python is a very high-level programming language because
its syntax so closely resembles the English language. Higher-level means it’s more readable to humans and less readable to computers.'''

#----------------------------
# What is the differences between =  ==
'''= is an assignment operator
== is an equality operator'''
#----------------------------
#What do we mean by using != ?
'''not equal'''
#----------------------------
# What is the operator precedence?

'''When we have more than one operator, the one with higher precedence will be evaluated first.
for example: 12+6*4. How do we evaluate it? First, we do multiplication of 6 and 4, which gives 24. Then we add 12 to 24 and the answer is 36.'''

#----------------------------
x= 10
x  =+ 15
print(x)

x = x / 5
print(x)
x = x * 10
print(x)
x = x % 3
print(x)
print(11%4)
#exponent
print(2**3)
print(11/3) #return float
print(11//3) #return int yes we can

#---------------------------------
if 10 > 15:
    print('yes')
else:
    print('x is smaller than 15')

#---------------------------------
#In which cases we will use all
#when we want to check more than one condition
x =10
a = 10
b =  12
c= 4
if all([a ==10 , b == 12 , c==4]): # same as and and,  or --> any
    print('Done')

if any([a ==10 , b == 12 , c==5]): # same as and and,  or --> any
    print('Done')

#If we need all the conditions to be true we will use …
'''all'''

#----------------------------------
# What is the differences between if , elif?
# What is the differences between elif else?
'''elif is just a fancy way of expressing else: if, Multiple ifs execute multiple branches after testing, while the elifs are mutually exclusivly,
execute acutally one branch after testing.
- elif used to include multiple conditional expressions'''

# Can we use more than one elif?
'''yes'''

#Can we use more than one else

'''No'''

#write s simple ternary operator
print(1) if a > b else print(-1)

#in elif , python will check all the conditions no matter what
'''the elif conditions are applied after the if condition. Python will evalute the if condition and if it
evaluates to False then it will evalute the elif blocks and execute the elif block whose expression evaluates to True.
If multiple elif conditions become True, then the first elif block will be executed.'''

#in elif we use else for
'''
the else condition can be optionally used to define an alternate block of statements to be
executed if the boolean expression in the if condition evaluates to False'''

List = [2,4,6,8,10]

print("4 is exist in the list") if 4 in List else print("4 is missing")
    
    
print("4 & 6 are exist in the list") if 4 and 6 in List else print("some are missing")
    

print("3 or 6 are exist in the list") if 3 or 6 in List else print("3 or 6 are missing")
    

print("2 and 4 and 5 are exist in the list") if all([2, 4 ,5]) in List else print("some are missing")
    


