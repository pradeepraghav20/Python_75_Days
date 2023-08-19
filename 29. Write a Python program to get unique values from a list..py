# 29. Write a Python program to get unique values from a list.
# Click me to see the sample solution


l=[4,4,3,3,3,3,4,6,7,8,8,8]
unique_list=[]
for i in l:
    if i not in unique_list:
        unique_list.append(i)

print(unique_list)


# 30. Write a Python program to get the frequency of elements in a list.
# Click me to see the sample solution

l=[4,4,3,3,3,3,4,6,7,8,8,8]
d={}
for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

print(d)


# 31. Write a Python program to count the number of elements in a list within a specified range.
# Click me to see the sample solution


#
# 32. Write a Python program to check whether a list contains a sublist.
# Click me to see the sample solution

# l=[4,4,3,3,3 [4,4,4,4]]
# for i in l:
#     if i is list:
#         print("Yes")




#
# 33. Write a Python program to generate all sublists of a list.
# Click me to see the sample solution
#
#
# 35. Write a Python program to create a list by concatenating a given list with a range from 1 to n.
# Sample list : ['p', 'q']



# n =5
# Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
# Click me to see the sample solution
#
# 36. Write a Python program to get a variable with an identification number or string.
# Click me to see the sample solution
#
# 37. Write a Python program to find common items in two lists.
# Click me to see the sample solution

new_list=[]
l=[4,45,6,4,4,42]
l2=[52,5,4,33,334]
for i in l:
    if i in l2 and  i not in new_list:
        new_list.append(i)

print("Done")
print(new_list)




#
# 38. Write a Python program to change the position of every n-th value to the (n+1)th in a list.
# Sample list: [0,1,2,3,4,5]
# Expected Output: [1, 0, 3, 2, 5, 4]
# Click me to see the sample solution
#
# 39. Write a Python program to convert a list of multiple integers into a single integer.
# Sample list: [11, 33, 50]
# Expected Output: 113350
l=[11, 33, 50]
new_num=""
for i in l:
    new_num+=str(i)

print(new_num)
