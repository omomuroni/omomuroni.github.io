import multiprocessing
import time
import os

cpu_count = os.cpu_count()
print(cpu_count)

def parafunc (param):
    print ("param {0} is being processed".format(param))
    time.sleep (1)
    return param * param

if __name__ == '__main__':
    with multiprocessing.Pool() as pool:
        results = pool.map(parafunc, range(21))
    
    print (results)