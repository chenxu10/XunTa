import random
import numpy as np
import time
import random
import multiprocessing
import datetime

def simulationpi():
    # initialize circle points, square points amd interbal
    INTERVAL = 2000
    circle_points = 0
    rect_points = 0

    for _ in range(INTERVAL):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        dist = x ** 2 + y ** 2
        if dist <= 1:
            circle_points += 1
        rect_points += 1

        res = 4 * (circle_points/rect_points)

    return res


def simulationvect(n=20000):
    x = np.random.random(n)
    y = np.random.random(n)
    print(x*x + y*y <= 1)
    return (x*x + y*y <= 1).sum() / 20000 * 4



if __name__ == "__main__":
    begin = time.time()
    print(simulationpi())
    time.sleep(1)
    end = time.time()
    print("Time cost is {}",format(end - begin))

    begin = time.time()
    print(simulationvect())
    time.sleep(1)
    end = time.time()
    print("Time cost is {}",format(end - begin))


