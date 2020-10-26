#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    rows_len = len(arr)
    columns_len = 6
    sum_new_l = -9999999
    for i in range(rows_len - 2):
        for j in range(columns_len - 2):
            new_l = []
            new_l += arr[i][j:j + 3]
            print('new_l is 1 : ',new_l)
            new_l += [arr[i + 1][j + 1]]
            print('new_l is 1 : ', new_l)
            new_l += arr[i + 2][j:j + 3]
            print('new_l is 1 : ', new_l)
            print('new_l sum is', sum(new_l))
            if sum_new_l < sum(new_l):
                sum_new_l = sum(new_l)
    return sum_new_l

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
