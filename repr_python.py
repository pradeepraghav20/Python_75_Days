# class Test:
#
#     def __int__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def __str__(self):
#         return (self.name)
#
#
#
# t1=Test("pradeep",12)

class Dog:
    def __init__(self):

        print("ggg")

class cat:
    def __init__(self):
        print('cat...')
c1=cat()

class Ocean:

    def __init__(self, sea_creature_name, sea_creature_age):
        self.name = sea_creature_name
        self.age = sea_creature_age

    def __str__(self):
        return f'The creature type is {self.name} and the age is {self.age}'

    def __repr__(self):
        return f'Ocean(\'{self.name}\', {self.age})'


c = Ocean('Jellyfish', 5)

print(str(c))
print(repr(c))
