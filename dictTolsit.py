# # How to convert Python Dictionary to a list?
#
# Using list & items() Method
#
# Using keys() Method
#
# Using values() Method
#
# Using List Comprehension
#
# Using Zip() Function
#
# Using map() Function
#
# Using for loop & items() Method


d={1:2,3:44,444:444,5:444}

#method 1
res=list(zip(d.keys(),d.values()))
print(res)

#method 2
l=list([i for i in d.items()])
print(l)

#method 3

print(([(k,v) for k,v in d.items()]))



