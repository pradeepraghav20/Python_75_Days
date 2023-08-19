# 105. Write a Python program to extract and display the name from a given Email address.
# Sample Data:
# ("john@example.com") -> ("john")
# ("john.smith@example.com") -> ("johnsmith")
# ("fully-qualified-domain@example.com") -> ("fullyqualifieddomain")



email="john@example.com"
name=""
for i in email:
    if i not in name:
        if i=="@":
            break
        else:
            name+=i
print(name)