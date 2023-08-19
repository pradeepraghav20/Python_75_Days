def outerfun():
    def innerfun():
        print("Inner Function")
    return innerfun
a=outerfun()
del outerfun
a()