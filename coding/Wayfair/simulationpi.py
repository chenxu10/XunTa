import random
import numpy as np
import time
import random
import multiprocessing
import datetime

def simulationpi():
    # initialize circle points, square points amd interbal
    pass


def simulationvect(n=20000):
    pass



if __name__ == "__main__":
    begin = time.time()
    print(simulationpi())
    time.sleep(1)
    end = time.time()
    print("Time cost is {}",format(end - begin))

    begin = time.time()
    simulationvect()
    time.sleep(1)
    end = time.time()
    print("Time cost is {}",format(end - begin))


