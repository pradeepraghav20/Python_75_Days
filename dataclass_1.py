from dataclasses import dataclass
@dataclass
class Person():
    name:str
    age :str
@dataclass
class Employee(Person):
    emp_id:int
    def showDetails(self):
        print(self.emp_id)

p1=Person("pradeep",23)
p1=Employee("pradeep",23,1851898)
p1.showDetails()
