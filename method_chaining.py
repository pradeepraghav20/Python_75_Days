class Method_Chain:
    def __int__(self,email,password):
        print("Init method")


    def login(self):
        print("this is login")
        return self

    def logout(self):
        print("logout...")
        return self




# m1=Method_Chain()
# m1.login().logout()


class CalculatorFunctions():
   def sum(self):
      print("Sum called")
      return self
   def difference(self):
      print("Difference called")
      return self
   def product(self):
      print("Product called")
      return self
   def quotient(self):
      print("Quotient called")
      return self
if __name__ == "__main__":
   calculator = CalculatorFunctions()
   # Chaining all methods of CalculatorFunctions
   calculator.sum().difference().product().quotient()