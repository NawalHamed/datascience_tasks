#Tasks Part3

Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']

'''normal list'''


NewNames = []

for x in Names:
    
    str(x).upper()
    print(x)
    NewNames.append(x)
    
print(NewNames)

'''list comprehension'''

Cap_Names = [name.upper() for name in Names]
print(Cap_Names)


