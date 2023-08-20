class Animal():
    def fly(self):
        print("Fly...")
class Cat():
    def fly(self):
        print("Fly...")

class Dog():
    def fly(self):
        print("Not Fly...")

for obj in Animal(),Cat(),Dog() :
    obj.fly()