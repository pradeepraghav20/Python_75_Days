import  os
if os.path.exists("temp.txt"):
    print("Yess exists")
    os.remove("temp.txt")
else:
    print("Noo")



# p=1
# q=2
#
# r=p
# s=(p,q)
# print(type(r))
# print(r,s)