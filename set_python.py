#set
#how to create set
set1={1,2,3,4,5,6,7,8}
print(type(set1))

set2=set([4,4,4,3,3,31111])
print(set2)


set3=set((3,3,3,3))
print(set3)

#Adding items to the set
print(set1)
set1.add((33))
print(set1)
set1.update(set2)
print(set1)

# discard()
# method and remove()
# m
#Removing items from the set
#set1.remove(330)

set2.discard(330)
print(set1)

#************************************************Set Operation *******************************************************

#union
Days1 = {"Monday","Tuesday","Wednesday","Thursday", "Sunday"}
Days2 = {"Friday","Saturday","Sunday"}
print(Days1|Days2) #printing the union of the sets
print(Days1.union(Days2))

#intersection
print(Days1.intersection(Days2))
#
print(Days1.difference(Days2))


#FrozenSets.

Frozenset1 = frozenset([1,2,3,4,5])
print(Frozenset1)
print(len(Frozenset1))

Frozenset2 = frozenset([112,2,2,25,5,5,2,3,4,5])
print(Frozenset2.union(Frozenset1))


Dictionary = {"Name":"John", "Country":"USA", "ID":101}
fset=frozenset(Dictionary)
print(fset)





