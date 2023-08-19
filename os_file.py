import  os
if os.path.exists("temp.txt"):
    print("Yess exists")
    os.remove("temp.txt")
else:
    print("Noo")