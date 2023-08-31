#decorater 1
def hello_deco(func):
    def inner_functio():
        print ("Before execution")
        func()
        print("after execuation")
    return inner_functio



def function_to_be_used():
    print ("this is main inside function")


# function_to_be_used()

function_to_be_used=hello_deco(function_to_be_used)
function_to_be_used()

#before
#this is inside
#after
