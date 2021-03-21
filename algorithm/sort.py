import random
import sys


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


def merge_sort():
    print('merge')


if __name__ == "__main__":
    # array_num()
    # bubble_sort()
    # insertion_sort()
    random_list = random.sample(range(100), 10)
    # print(quick_sort_example(random_list))
    # quick_sort_2752()
    # quick_sort_1427()
    split(random_list)
