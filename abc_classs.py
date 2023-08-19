from abc import  ABC,abstractmethod

class RBI(ABC):
    @abstractmethod
    def rateOfIntrest(self):
        pass
class PNB(RBI):
    def rateOfIntrest(self):
        print("Rate of intrest is 5.5%")

class SBI (RBI):
    def rateOfIntrest(self):
        print("Rate of intrest is 6.5%")

p1=PNB()
s2=SBI()
p1.rateOfIntrest()
s2.rateOfIntrest()

