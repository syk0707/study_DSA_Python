import sys
import collections
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


if __name__ == "__main__":
    # array_num()
    # bubble_sort()
    insertion_sort()
    insertion_sort()
def array_num_2():
    total_num = int(sys.stdin.readline())
    total_deque = deque()
    for total_idx in range(total_num):
        num = int(sys.stdin.readline())
        total_arr.append(num)
    nl = "\n"
    while total_deque:
        sys.stdout.write(f"{total_arr[reverse_idx]}{nl}")

if __name__ == "__main__":
    #array_num()
    #array_num_2()
    print(chr(74))
    print(ord("C"))
    print(ord("C"))
