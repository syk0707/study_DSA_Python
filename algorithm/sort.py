import sys
from collections import deque
import random


def array_num():
    total_num = int(input())
    total_obj = {}
    total_arr = []
    for idx in range(total_num):
        num = int(input())
        if total_obj.get(num) is None:
            total_obj[num] = 1
            total_arr.append(num)
    total_arr.sort()
    for print_num in total_arr:
        print(print_num)


def bubble_sort():
    data_list = random.sample(range(100), 50)
    print(data_list)
    for idx in range(len(data_list) - 1):
        swap = False
        for idx2 in range(len(data_list) - idx - 1):
            if data_list[idx2] > data_list[idx2 + 1]:
                data_list[idx2], data_list[idx2 + 1] = data_list[idx2 + 1], data_list[idx2]
                swap = True
        if swap is False:
            break
    print(data_list)


def array_num_2():
    total_arr = []
    total_num = int(sys.stdin.readline())
    for total_idx in range(total_num):
        num = int(sys.stdin.readline())
        total_arr.append(num)
    nl = "\n"
    total_deque = deque(total_arr)
    while total_deque:
        sys.stdout.write(f"{total_deque}{nl}")
        total_deque.pop()


def insertion_sort():
    data_list = random.sample(range(100), 50)
    print(data_list)
    for idx in range(len(data_list) - 1):
        for idx2 in range(idx + 1, 0, -1):
            if data_list[idx2] < data_list[idx2 - 1]:
                data_list[idx2], data_list[idx2 - 1] = data_list[idx2 - 1], data_list[idx2]
            else:
                break
    print(data_list)


def quick_sort_example(data):
    if len(data) <= 1:
        return data

    pivot = data[0]

    # left, right = [], []
    #
    # for idx in range(1, len(data)):
    #     if pivot > data[idx]:
    #         left.append(data[idx])
    #     else:
    #         right.append(data[idx])

    left = [item for item in data[1:] if pivot > item]
    right = [item for item in data[1:] if pivot <= item]

    return quick_sort_example(left) + [pivot] + quick_sort_example(right)


# def quick_sort_recursive(sort_arr):
#     if len(sort_arr) <= 1:
#         return sort_arr
#     pivot = sort_arr[0]
#
#     left_arr, right_arr = [], []
#
#     for idx in range(1, len(sort_arr)):
#         if pivot > sort_arr[idx]:
#             left_arr.append(sort_arr[idx])
#         else:
#             right_arr.append(sort_arr[idx])
#
#     return quick_sort_recursive(left_arr) + [pivot] + quick_sort_recursive(right_arr)
def quick_sort_recursive(sort_arr):
    if len(sort_arr) <= 1:
        return sort_arr
    pivot = sort_arr[0]
    left_arr = [item for item in sort_arr[1:] if pivot > item]
    right_arr = [item for item in sort_arr[1:] if pivot <= item]

    return quick_sort_recursive(left_arr) + [pivot] + quick_sort_recursive(right_arr)


def quick_sort_2752():
    total_arr = list(map(int, sys.stdin.readline().split()))
    ret_arr = quick_sort_recursive(total_arr)
    for ret_idx in ret_arr:
        sys.stdout.write(str(ret_idx) + " ")


def quick_sort_1427():
    total_num = sys.stdin.readline().rstrip('\n')
    list_arr = [int(num) for num in total_num]
    ret_arr = quick_sort_recursive(list_arr)
    for ret_idx in range(len(ret_arr) - 1, -1, -1):
        sys.stdout.write(str(ret_arr[ret_idx]))


def split(data):
    medium = int(len(data) / 2)
    left = data[:medium]
    right = data[medium:]
    print(left, right)


def merge(left, right):
    merged = list()
    left_point, right_point = 0, 0
    # case 1 - left, right remain
    while len(left) > left_point and len(right) > right_point:
        if left[left_point] > right[right_point]:
            merged.append(right[right_point])
            right_point += 1
        else:
            merged.append(left[left_point])
            left_point += 1
    # case 2 - only left remain
    while len(left) > left_point:
        merged.append(left[left_point])
        left_point += 1
    # case 3 - only right remain
    while len(right) > right_point:
        merged.append(right[right_point])
        right_point += 1

    return merged


def merge_sort(data):
    if len(data) <= 1:
        return data
    medium = int(len(data) / 2)
    left = merge_sort(data[:medium])
    right = merge_sort(data[medium:])
    return merge(left, right)


if __name__ == "__main__":
    random_list = random.sample(range(100), 10)
    # array_num()
    # bubble_sort()
    # insertion_sort()
    # print(quick_sort_example(random_list))
    # array_num_2()
    # quick_sort_2752()
    # quick_sort_1427()
    # split(random_list)
    # insertion_sort()
    print(random_list)
    print(merge_sort(random_list))
