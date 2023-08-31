class Test:
    college_name="ABS"
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def disp_details(self):
        print(f'{self.name}{self.age}')

    @classmethod

    def update_college_name(cls,c_name):
        cls.college_name=c_name

    @staticmethod
    def check_age(age):
        if age>18:
            return  True
        else:
            return  False






t1=Test("pradeep",'raghav')
t2=Test("amit","raghav")
# t1.college_name
print(t1.college_name)
print(t2.college_name)
Test.update_college_name("GLA")

print(t1.college_name)
print(t2.college_name)

print(Test.check_age(22))