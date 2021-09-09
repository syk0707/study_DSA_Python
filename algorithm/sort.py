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


def merge_2(left, right):
    merge_list = []
    l_num = 0
    r_num = 0
    while len(left) > l_num and len(right) > r_num:
        if left[l_num] < right[r_num]:
            merge_list.append(left[l_num])
            l_num += 1
        else:
            merge_list.append(right[r_num])
            r_num += 1
    merge_list += right[r_num:]
    merge_list += left[l_num:]
    return merge_list


def merge_sort(data):
    if len(data) <= 1:
        return data
    medium = int(len(data) / 2)
    left = merge_sort(data[:medium])
    right = merge_sort(data[medium:])
    return merge_2(left, right)


def merge_sort_2751():
    total_num = int(sys.stdin.readline())
    total_arr = list()
    for idx in range(total_num):
        total_arr.append(int(sys.stdin.readline()))
    ret_arr = merge_sort(total_arr)
    for num in ret_arr:
        sys.stdout.write(f"{num}\n")


def sort_5576():
    w_arr, k_arr = [], []
    for w_idx in range(10):
        w_arr.append(int(sys.stdin.readline()))
    for k_idx in range(10):
        k_arr.append(int(sys.stdin.readline()))
    w_arr.sort(reverse=True)
    k_arr.sort(reverse=True)
    w_score, k_score = 0, 0
    for w_num in range(0, 3):
        w_score += w_arr[w_num]
    for k_num in range(0, 3):
        k_score += k_arr[k_num]
    sys.stdout.write(f"{w_score} {k_score}")


def sort_15720():
    num_arr = list(map(int, sys.stdin.readline().split()))
    first_arr = list(map(int, sys.stdin.readline().split()))
    second_arr = list(map(int, sys.stdin.readline().split()))
    third_arr = list(map(int, sys.stdin.readline().split()))
    num_arr.sort()
    first_arr.sort()
    second_arr.sort()
    third_arr.sort()
    min_num = num_arr[0]
    total_price = 0
    discount_price = 0
    for idx in range(min_num):
        price = first_arr.pop() + second_arr.pop() + third_arr.pop()
        discount_price += int(price * 0.9)
        total_price += price
    for f_remain_num in first_arr:
        total_price += f_remain_num
        discount_price += f_remain_num
    for s_remain_num in second_arr:
        total_price += s_remain_num
        discount_price += s_remain_num
    for t_remain_num in third_arr:
        total_price += t_remain_num
        discount_price += t_remain_num
    print(total_price)
    print(discount_price)


def get_idx_num_2693():
    num = int(sys.stdin.readline())
    for idx in range(num):
        arr = list(map(int, sys.stdin.readline().split()))
        arr.sort(reverse=True)
        print(arr.__getitem__(2))


def sort_10814():
    tot_case = int(sys.stdin.readline())
    case_arr = []
    for idx in range(tot_case):
        each_case = list(map(str, sys.stdin.readline().split()))
        each_case.insert(0, int(each_case[0]))
        each_case.pop(1)
        each_case.insert(1, idx)
        case_arr.append(each_case)
    case_arr.sort()
    for case in case_arr:
        if case is not case_arr[tot_case - 1]:
            sys.stdout.write(f"{case[0]} {case[2]}\n")
        else:
            sys.stdout.write(f"{case[0]} {case[2]}")


def sort_10813():
    tot_arr = list(map(int, sys.stdin.readline().split()))
    case_arr = [i + 1 for i in range(tot_arr[0])]
    for idx in range(tot_arr[1]):
        case_idx_arr = list(map(int, sys.stdin.readline().split()))
        change_first_num = case_arr[case_idx_arr[0] - 1]
        change_second_num = case_arr[case_idx_arr[1] - 1]
        case_arr[case_idx_arr[0] - 1] = change_second_num
        case_arr[case_idx_arr[1] - 1] = change_first_num
    for ret_num in case_arr:
        sys.stdout.write(f"{ret_num} ")


def sort_18766():
    tot_idx = int(sys.stdin.readline())
    for idx in range(tot_idx):
        case_num = int(sys.stdin.readline())
        first_arr = list(map(str, sys.stdin.readline().split()))
        second_arr = list(map(str, sys.stdin.readline().split()))
        first_arr.sort()
        second_arr.sort()
        first_idx = 0
        is_cheater = False
        for first_item in first_arr:
            if first_item != second_arr[first_idx]:
                sys.stdout.write("CHEATER\n")
                is_cheater = True
                break
            first_idx += 1
        if is_cheater is False:
            sys.stdout.write("NOT CHEATER\n")


def sort_15819():
    tot_case = list(map(int, sys.stdin.readline().split()))
    input_arr = []
    for idx in range(tot_case[0]):
        input_arr.append(sys.stdin.readline())
    input_arr.sort()
    sys.stdout.write(f"{input_arr[tot_case[1] - 1]}")


def sort_15969():
    tot_num = int(sys.stdin.readline())
    tot_score = list(map(int, sys.stdin.readline().split()))
    tot_score.sort()
    sys.stdout.write(f"{tot_score[-1] - tot_score[0]}")


def sort_check_11536():
    is_increase = True
    is_decrease = True
    tot_case = int(sys.stdin.readline())
    tot_arr = []
    for idx in range(tot_case):
        tot_arr.append(sys.stdin.readline().rstrip())
    for each_idx in range(1, len(tot_arr)):
        if tot_arr[each_idx] >= tot_arr[each_idx - 1]:
            is_decrease = False
        elif tot_arr[each_idx] <= tot_arr[each_idx - 1]:
            is_increase = False
    if not is_increase and not is_decrease:
        sys.stdout.write("NEITHER")
    elif is_increase:
        sys.stdout.write("INCREASING")
    elif is_decrease:
        sys.stdout.write("DECREASING")


def sort_16212():
    tot_case = int(sys.stdin.readline())
    each_arr = list(map(int, sys.stdin.readline().split()))
    each_arr.sort()
    sys.stdout.write(f"{' '.join(str(i) for i in each_arr)}")


def sort_10867():
    tot_case = int(sys.stdin.readline())
    tot_arr = list(map(int, sys.stdin.readline().split()))
    tot_dic = {}
    for num in tot_arr:
        if tot_dic.get(num) is None:
            tot_dic[num] = 1
    sys.stdout.write(f"{' '.join(str(i) for i in sorted(tot_dic.keys()))}")


def sort_reverse_11931():
    tot_case = int(sys.stdin.readline())
    tot_arr = []
    for idx in range(tot_case):
        tot_arr.append(int(sys.stdin.readline()))
    tot_arr.sort(reverse=True)
    sys.stdout.write("\n".join(str(i) for i in tot_arr))


def sort_10989():
    tot_val = {}
    tot_idx = int(sys.stdin.readline())
    for idx in range(tot_idx):
        each_num = int(sys.stdin.readline())
        if tot_val.get(each_num) is None:
            tot_val[each_num] = 1
        else:
            tot_val[each_num] += 1
    for key in sorted(tot_val):
        for val in range(tot_val[key]):
            sys.stdout.write(f"{key}\n")


def sort_1181():
    tot_idx = int(sys.stdin.readline())
    input_dic = {}
    for idx in range(tot_idx):
        input_word = sys.stdin.readline()
        len_word = len(input_word)
        if input_dic.get(len_word) is None:
            input_dic[len_word] = {}
        input_dic[len_word][input_word] = 1
    for key_dic in sorted(input_dic.keys()):
        for output_word in sorted(input_dic[key_dic].keys()):
            sys.stdout.write(f"{output_word}")


def prog_sort_2540(people, limit):
    answer = 0
    people.sort()
    start, end = 0, len(people) - 1

    while start <= end:
        answer += 1
        if people[start] + people[end] <= limit:
            start += 1
        end -= 1
    return answer


def sort_15688():
    tot_idx = int(sys.stdin.readline())
    input_arr = []
    for idx in range(tot_idx):
        input_arr.append(int(sys.stdin.readline()))
    input_arr.sort()
    print("\n".join(map(str, input_arr)))


def sort_11650():
    tot_idx = int(sys.stdin.readline())
    input_dic = {}
    for idx in range(tot_idx):
        each_num = list(map(int, sys.stdin.readline().split()))
        if input_dic.get(each_num[0]) is None:
            input_dic[each_num[0]] = [each_num[1]]
        else:
            input_dic[each_num[0]].append(each_num[1])
    for each_key in sorted(input_dic):
        for each_val in sorted(input_dic[each_key]):
            sys.stdout.write(f"{each_key} {each_val}\n")


if __name__ == "__main__":
    # random_list = random.sample(range(100), 10)
    # array_num()
    # bubble_sort()
    # insertion_sort()
    # print(quick_sort_example(random_list))
    # array_num_2()
    # quick_sort_2752()
    # quick_sort_1427()
    # split(random_list)
    # insertion_sort()
    # print(random_list)
    # print(merge_sort(random_list))
    # merge_sort_2751()
    # sort_5576()
    # sort_15720()
    # get_idx_num_2693()
    # sort_10814()
    # sort_10813()
    # sort_18766()
    # sort_15819()
    # sort_15969()
    # sort_check_11536()
    # sort_16212()
    # sort_10867()
    # sort_reverse_11931()
    # sort_10989()
    # sort_1181()
    # prog_sort_2540([70, 80, 50], 100)
    # sort_15688()
    sort_11650()
