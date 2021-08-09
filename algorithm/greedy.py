import sys


def cal_2720():
    tot_num = int(sys.stdin.readline())
    for idx in range(tot_num):
        each_num = int(sys.stdin.readline())
        quarter_num = 0
        dime_num = 0
        nickel_num = 0
        penny_num = 0
        quarter_num = each_num // 25
        each_num = each_num - (quarter_num * 25)
        dime_num = each_num // 10
        each_num = each_num - (dime_num * 10)
        nickel_num = each_num // 5
        penny_num = each_num - (nickel_num * 5)
        sys.stdout.write(f"{quarter_num} {dime_num} {nickel_num} {penny_num}\n")


def cal_16435():
    tot_arr = list(map(int, sys.stdin.readline().split()))
    case_arr = list(map(int, sys.stdin.readline().split()))
    case_arr.sort()
    first_num = tot_arr[1]
    for num in case_arr:
        if first_num >= num:
            first_num += 1
    sys.stdout.write(f"{first_num}")


def reverse_1439():
    case_num = sys.stdin.readline().rstrip()
    slice_num = []
    idx_num = 0
    cnt_0 = 0
    cnt_1 = 0
    for idx in range(len(case_num) + 1):
        if int(idx) == len(case_num) - 1:
            slice_num.append(case_num[idx_num:])
            if case_num[idx_num] == '0':
                cnt_0 += 1
            else:
                cnt_1 += 1
            break
        if case_num[idx] != case_num[idx + 1]:
            slice_num.append(case_num[idx_num: idx + 1])
            if case_num[idx_num] == '0':
                cnt_0 += 1
            else:
                cnt_1 += 1
            idx_num = idx + 1
    sys.stdout.write(f"{min(cnt_0, cnt_1)}")


def greedy_11047():
    input_arr = list(map(int, sys.stdin.readline().split()))
    case_arr = []
    for idx in range(input_arr[0]):
        case_arr.append(int(sys.stdin.readline()))
    case_arr.reverse()
    cal_num = input_arr[1]
    ret_num = 0
    for case_num in case_arr:
        if cal_num < case_num:
            continue
        else:
            cal_quotient = cal_num // case_num
            ret_num += cal_quotient
            cal_num = cal_num - (case_num * cal_quotient)
        if cal_num == 0:
            break
    sys.stdout.write(f"{ret_num}")


if __name__ == "__main__":
    # cal_2720()
    # cal_16435()
    # reverse_1439()
    greedy_11047()

