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
    sum_min = 0
    print(orig_state)
    print(q)
    for k in orig_state:
        if q.index(k) > orig_state.index(k):
            print(q)
            print(' number that shifts is  : ', k, 'and it shifts by  : ', abs(orig_state.index(k) - q.index(k)))
            if abs(orig_state.index(k) - q.index(k)) == 1:
                q[q.index(k) - 1], q[q.index(k)] = q[q.index(k)], q[q.index(k) - 1]
            elif abs(orig_state.index(k) - q.index(k)) == 2:
                q[q.index(k) - 2], q[q.index(k) - 1] = q[q.index(k) - 1], q[q.index(k) - 2]
                q[q.index(k) - 1], q[q.index(k)] = q[q.index(k)], q[q.index(k) - 1]
            elif orig_state.index(k) - q.index(k) > 2:
                sum_min = -999999999
                print("Too chaotic")
            else:
                sum_min += abs(orig_state.index(k) - q.index(k))
            print(q)
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
