import time
import os

print(os.getcwd())


def printout(num):
    for x in range(num):
        x**2


start_time = time.time()


printout(34331434)
end_time = time.time()

elapsed_time = end_time-start_time


print(elapsed_time)