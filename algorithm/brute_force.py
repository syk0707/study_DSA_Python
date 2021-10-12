import sys
import copy
import itertools


def black_jack_2798():
    cnt_list = list(map(int, sys.stdin.readline().split()))
    card_list = list(map(int, sys.stdin.readline().split()))
    card_list.sort()
    max_num = card_list[0] + card_list[1] + card_list[2]
    for num in range(len(card_list) - 2):
        for num_2 in range(num, len(card_list) - 1):
            for num_3 in range(num_2, len(card_list)):
                if num == num_2 or num == num_3 or num_2 == num_3:
                    continue
                cal_num = card_list[num] + card_list[num_2] + card_list[num_3]
                if max_num < cal_num <= cnt_list[1]:
                    max_num = cal_num
    sys.stdout.write(f"{max_num}\n")


def get_num_14914():
    num_list = list(map(int, sys.stdin.readline().split()))
    divide_arr = []
    for idx in range(1, num_list[0] + 1):
        if num_list[1] < idx:
            break
        if num_list[0] % idx == 0 and num_list[1] % idx == 0:
            divide_arr.append(idx)
    for divide_num in divide_arr:
        sys.stdout.write(f"{divide_num} {int(num_list[0] / divide_num)} {int(num_list[1] / divide_num)}\n")


def get_num_2501():
    ans_arr = []
    case_arr = list(map(int, sys.stdin.readline().split()))
    for num in range(1, case_arr[0] + 1):
        if case_arr[0] % num == 0:
            ans_arr.append(num)
        if len(ans_arr) > case_arr[1]:
            break
    if len(ans_arr) <= case_arr[1] - 1:
        sys.stdout.write(f"{0}")
    else:
        sys.stdout.write(f"{ans_arr[case_arr[1] - 1]}")


def cal_zero_7490():
    tot_idx = int(sys.stdin.readline())
    tot_list = []

    def recursive_cal(arr, n):
        if len(arr) == n:
            tot_list.append(copy.deepcopy(arr))
            return
        arr.append(' ')
        recursive_cal(arr, n)
        arr.pop()

        arr.append('+')
        recursive_cal(arr, n)
        arr.pop()

        arr.append('-')
        recursive_cal(arr, n)
        arr.pop()

    for idx in range(tot_idx):
        tot_list = []
        num = int(sys.stdin.readline())
        recursive_cal([], num - 1)

        num_list = [i for i in range(1, num + 1)]

        for each_case in tot_list:
            print_str = ""
            for i in range(num - 1):
                print_str += str(num_list[i]) + each_case[i]
            print_str += str(num_list[-1])
            if eval(print_str.replace(" ", "")) == 0:
                sys.stdout.write(f"{print_str}\n")
            sys.stdout.write(f"\n")


def get_sum_2309():
    tot_arr = []
    idx_arr = list(itertools.combinations([i for i in range(9)], 7))
    is_get_case = False
    for idx in range(9):
        tot_arr.append(int(sys.stdin.readline()))
    for each_case in idx_arr:
        sum_num = 0
        case_arr = []
        for idx in each_case:
            sum_num += tot_arr[idx]
            case_arr.append(tot_arr[idx])
        if sum_num == 100:
            break
    case_arr.sort()
    for each_num in case_arr:
        sys.stdout.write(f"{each_num}\n")


def get_sum_3040():
    tot_arr = []
    idx_arr = list(itertools.combinations([i for i in range(9)], 7))
    for idx in range(9):
        tot_arr.append(int(sys.stdin.readline()))
    for each_case in idx_arr:
        sum_num = 0
        case_arr = []
        for idx in each_case:
            sum_num += tot_arr[idx]
            case_arr.append(tot_arr[idx])
        if sum_num == 100:
            break
    for each_num in case_arr:
        sys.stdout.write(f"{each_num}\n")


def get_view_1668():
    tot_idx = int(sys.stdin.readline())
    case_arr = []
    left_num = 1
    right_num = 1
    for idx in range(tot_idx):
        case_arr.append(int(sys.stdin.readline()))
        if idx == 0:
            first_num = case_arr[0]
        if idx >= 1 and case_arr[idx] > first_num:
            left_num += 1
            first_num = case_arr[idx]
    case_arr.reverse()
    first_num = case_arr[0]
    for case_idx in range(tot_idx):
        if case_idx >= 1 and case_arr[case_idx] > first_num:
            right_num += 1
            first_num = case_arr[case_idx]
    sys.stdout.write(f"{left_num}\n{right_num}")


if __name__ == "__main__":
    # black_jack_2798()
    # get_num_14914()
    # get_num_2501()
    # cal_zero_7490()
    # get_sum_2309()
    # get_sum_3040()
    get_view_1668()
