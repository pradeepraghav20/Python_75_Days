# . Write a Python program that takes a string and replaces all the characters with their respective numbers.
# Sample Data:
# ("Python") -> "16 25 20 8 15 14"
# ("Java") -> "10 1 22 1"
# ("Python Tutorial") -> "16 25 20 8 15 14 20 21 20 15 18 9 1 12"

s='Java'.lower()
new_str=""
for i in s:
    new_str+=str(ord(i)-96)+ " "

print(new_str)



def test(text):
    return ' '.join(str(ord(i)-96) for i in text.lower() if i.isalpha())



