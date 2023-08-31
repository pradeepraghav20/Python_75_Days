import monk

def funC(self):
    print('FunC is being called')
    
monk.A.funA=funC
a=monk.A()
a.funA()