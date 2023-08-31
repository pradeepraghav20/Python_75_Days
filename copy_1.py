from copy import  deepcopy
import copy

l=[[3],3,3,3]
l3=copy.deepcopy(l)
l3[0].append(33)
print(l3)
print(l3)
print(l)


l2=copy.copy(l)
l3=copy.copy(l)
l3[0].append(33)
print(l3)
print(l2)

# print(l3)

# print(l2)