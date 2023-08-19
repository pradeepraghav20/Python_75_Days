#
# # . Write a Python program to remove repeated consecutive characters and replace them with single letters and print a updated string.
#
# ("Red Green White") -> "Red Gren White"
# ("aabbbcdeffff") -> "abcdef"
# ("Yellowwooddoor") -> "Yelowodor"

s="Red Green White"
new_str=""
for i in s:
    if i not in new_str:
        new_str+=i
        
print(new_str)

