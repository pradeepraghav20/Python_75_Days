class Vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    def __str__(self):
        return  f" {self.i}i+{self.j}j+{self.k}k"

    def __add__(self, x):
        return Vector(self.i+x.i,self.j+x.j,self.k+x.k)

v1=Vector(1,2,3)
v2=Vector(4,5,6)
print(v1+v2)







list1 = []
list2 = []
list3 = list1
# case 1
if (list1 == list2):
	print("True")
else:
	print("False")
# case 2
if (list1 is list2):
	print("True")
else:
	print("False")
# case 3
if (list1 is list3):
	print("True")
else:
	print("False")
# case 4
list3 = list3 + list2
if (list1 is list3):
	print("True")
else:
	print("False")





