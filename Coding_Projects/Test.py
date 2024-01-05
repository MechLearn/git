# a = range ( 5,10, 2)
# for i in a : 
#     print(i)
    
    
b = range (0,15,3)
for i in b : 
    print(i)
    
    
#     c = range (5)
# for i in c : 
#     print(i)


## Examples to tuples and list

## Tuple Examples

T= (1,2,True, "Hey")
print(T[0:3])
print(T[::-1])
print(T[2:])

## Enumerate example in list

l = ['blue', 'yellow', 'green', 'red']

for i, v in enumerate(l):
   print(i,v)
   
## Reversed example 

for i in  reversed(l):
    print(i)
    
## zip example

T= (1,2,True, "Hey")
l = ['blue', 'yellow', 'green', 'red', 'purple']

for v1,v2 in zip(T,l):
    print(v1,v2)