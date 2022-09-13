#Tasks Part3

Names = ['mhmoud','farida','ali','hassan','mohamed','khaled','taha']

#1

'''normal list'''

NewNames = []

for x in Names:
    
    NewNames.append(x.upper())
    
print('normal list to uppercase: ' , NewNames)

'''list comprehension'''

print('\n')
Cap_Names = [name.upper() for name in Names]
print('list comprehension to uppercase: ', Cap_Names)

print('\n')
'''functional'''
#map, execute condition or func in loop (copy of object)-->list
Names2 = list(map(str.upper, Names)) 
print ('functional uppercase: ' , Names2)

print('\n')

#2
'''normal list'''
Names_with_a = []

for z in Names:
    if 'a' in z:
       Names_with_a.append(z)
    
print('normal list contains a: ' , Names_with_a)

print('\n')
'''list comprehension'''
a_Names = []
[a_Names.append(n) for n in Names if 'a' in n]
print('list comprehension contains a: ', a_Names)

print('\n')
'''functional'''
#map, execute condition or func in loop (copy of object)-->list
Names_contain_a =[]

def contain_a(z):
    if 'a' in z:
        return z
    
Names_contain_a = list(map(contain_a, Names)) 
print ("functional contains a: ", Names_contain_a)
print('\n')

#3
'''normal list'''
Names_startwith_t = []

for t in Names:
    if t.startswith('t'):
      Names_startwith_t.append(t)
    
print('normal list start with t: ' , Names_startwith_t)
print('\n')

'''list comprehension'''
t_Names = []
[t_Names.append(q) for q in Names if q.startswith('t') ]
print('list comprehension start with t: ' , t_Names)

print('\n')
'''functional'''
def start_t(t):
    if t.startswith('t'):
        return t
    
Names_t = list(map(start_t, Names)) 
print ("functional start with t: ", Names_t)
print('\n')
#4

'''normal list'''
Names_count_a = []
for w in Names:

     if w.count('a') == 2:
         Names_count_a.append(w)  
    
print("normal list contains 2 or more a: ", Names_count_a)
print('\n')

'''list comprehension'''
a2_Names = []
[a2_Names.append(p) for p in Names if p.count('a') >= 2 ]
print('list comprehension contains 2 or more a: ' , a2_Names)
print('\n')

'''functional'''
def count_a(w):
    if w.count('a') == 2:
        return w
Names2a = list(map(count_a, Names)) 
print ('functional contains 2 or more a: ', Names2a)
print('\n')

#5

a , * b = Names
print('first index: ' , a)
print('the rest of the list: ' , b)
print('\n')

a ,*_, b = Names
print('first index: ' ,a)
print('last index: ', b)
print('\n')

a , b ,*_= Names
print('first index: ', a)
print('second index: ' , b)
print('\n')
