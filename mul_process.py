import  multiprocessing
import threading
import time
def cal_cube(num):
    for i in range(num):
        print(f"Cube of {i} is",{i**3})
        time.sleep(1)

def cal_square(num):
    for i in range(num):
        print(f"square of {i} is", {i ** 2})
        time.sleep(1)


if __name__=='__main__':
    print("main function")
    start_time=time.time()
    p1 = multiprocessing.Process(target=cal_cube, args=(10,))
    p2 = multiprocessing.Process(target=cal_square, args=(10,))
    p1.start()
    p1.join()

    p2.start()
    p2.join()
    print(time.time()-start_time)
