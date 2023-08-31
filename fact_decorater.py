import math
import time
def calculate_time(func):
    def fact_caltime(*args,**kwargs):
        start_time=time.time()
        func(*args,**kwargs)
        end_time=time.time()
        print("Total execaution time",end_time-start_time)
    return fact_caltime


@calculate_time
def fact(num):
    time.sleep(3)
    print(math.factorial(num))

    
# fact=calculate_time(fact)
# fact(5)