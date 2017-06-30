from builtins import range
from queue import Queue
from _collections import deque

from math import pi
print([str(round(pi, i)) for i in range(1, 6)])


lis1 = ['a','b','c','d','e'];
print(lis1)
lis11 = ['ab','bd','f','nd','pe'];
print(lis11)
lis111 = lis1 + lis11;
lis1.extend(lis11)
print(lis111)
print(lis1)
#then = set(lis111)
#print("SETS : " + then)


listTry = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana','orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana'];
print(listTry);

list2 = ['Preeti','Sharad','Aditi','Madhura','Shaunak', 'Tanvi'];
listTry.sort(key=None, reverse=False); #SORTING
print(listTry);

listTry.append('Preetis Fruits') #APPEND
print(listTry);

listTry.extend(list2); #EXTEND

print(listTry.index('kiwi')) #INDEX
print(listTry.pop())
print(listTry.pop(5))
print(listTry);

listCompe1=[]
listCompe1 = list(map(lambda x : x**2 , range(10)))  #map lambda x with provided value in specified range.
print(listCompe1)

listCompe = [];
for x in range(20): 
    listCompe.append(x*2);
    
print(listCompe)

print([(x,y) for x in listCompe for y in listCompe1 if x!=y])

queue = deque(['Preeti','Sharad','Aditi']);
queue.append('Shaunak');
print(queue)
