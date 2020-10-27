#!/bin/python3

# Complete the minimumSwaps function below.
def minimumSwaps(corr_arr, sorted_arr_input, len_sorted_arr_input):
    result = 0
    sorted_arr_input = sorted(corr_arr)
    i = 0
    while i < len_sorted_arr_input-1:
        # print(i)
        correct_num_index = corr_arr.index(i)
        if corr_arr == sorted_arr_input:
            return result
        elif corr_arr[correct_num_index] == corr_arr[i]:
            i += 1
            pass
        else:
            print(corr_arr)

            result += 1
            corr_arr[i], corr_arr[correct_num_index] = corr_arr[correct_num_index], corr_arr[i]
            i += 1
    return result


# following was the func that was used because of timeout errors

# def minimumSwaps(arr):
#     swaps = 0
#     while arr != [n for n in range(1, n + 1)]:
#         for i in range(len(arr)):
#             if (i + 1) != arr[i]:
#                 ni = arr[i] - 1
#                 arr[i], arr[ni] = arr[ni], arr[i]
#                 swaps += 1
#     return swaps

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    arr = [(i - 1) for i in arr]
    sorted_arr = sorted(arr)
    len_sorted_arr = len(sorted_arr)
    res = minimumSwaps(arr, sorted_arr, len_sorted_arr)
    print(res)
