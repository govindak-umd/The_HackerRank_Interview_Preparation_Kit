#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumBribes function below.
def minimumBribes(q):
    len_a = len(q)
    orig_state = [i for i in range(1, len_a + 1)]
    print(orig_state)
    print(q)
    sum_min = 0
    for k in orig_state:
        print(orig_state.index(k), q.index(k))
        if q.index(k) < orig_state.index(k):
            print(' number that shifts is  : ', k, 'and it shifts by  : ', abs(orig_state.index(k) - q.index(k)))
            if orig_state.index(k) - q.index(k) > 2:
                sum_min = -999999999
                print("Too chaotic")
            else:
                # sum_min += abs(orig_state.index(k) - q.index(k))
                sum_min += 1
    if sum_min > 0:
        print('sum_min is : ', sum_min)
    elif sum_min < -999999:
        pass


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
