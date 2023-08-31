l=list(range(0,10))
from functools import reduce


print (list(filter(lambda x:x%2==0,l)))
print (list(map(lambda x:x**2,l)))
print(reduce(lambda x,b:x+b,l))

