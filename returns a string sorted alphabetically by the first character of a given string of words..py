# Write a Python program that returns a string sorted alphabetically by the first character of a given string of words.
# Sample Data:
# ("Red Green Black White Pink") -> "Black Green Pink Red White"
# ("Calculate the sum of two said numbers given as strings.") -> ("Calculate as given numbers of sum said strings. the two")
# ("The quick brown fox jumps over the lazy dog.") -> ("The brown dog. fox jumps lazy over quick the")

# s=input().lower()
s="Red Green Black White Pink".lower()
#method 1
# print ("".join(sorted(s)))
print(s)
new_str=s.split()

for i in  range(len(new_str)-1):
    if ord(new_str[i][0])>ord(new_str[i+1][0]):
        temp=new_str[i]
        new_str[i]=new_str[i+1]
        new_str[i+1]=temp

print(new_str)

def sort_string(text):
    return ' '.join(sorted(text.split(), key=lambda c: c[0]))
sort_string("Red Green Black White Pink")



