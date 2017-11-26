import matplotlib.pyplot as plt
import numpy as np
import time


def collatz_conjecture(number):
    """
    Collatz Conjecture
    n = number
    number is even -> n/2
    number is odd -> 3n+1
    """
    travelled_nums = np.array([number], dtype=np.int64)
    steps = 0
    start = time.time()
    while True:
        if number % 2 == 0:
            print(number)
            number //= 2
            travelled_nums = np.append(travelled_nums, int(number))
            steps += 1
            if number == 1:
                break
        if number % 2 != 0:
            print(number)
            number = (3 * number) + 1
            travelled_nums = np.append(travelled_nums, int(number))
            steps += 1
    end = time.time()
    print(f'Total steps taken: {steps}')
    print(f'Total time: {end-start}s')
    plt.plot(travelled_nums)
    plt.xlabel('Numbers travelled')
    plt.show()

num = input('Enter number for collatz conjecture: ')
collatz_conjecture(int(num))
