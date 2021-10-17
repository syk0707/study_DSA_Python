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


def greedy_11399():
    tot_idx = int(sys.stdin.readline())
    tot_arr = list(map(int, sys.stdin.readline().split()))
    tot_arr.sort()
    ret_val = 0
    cnt_num = 0
    for idx in range(tot_idx):
        idx_arr = 0
        while idx_arr <= cnt_num:
            ret_val += tot_arr[idx_arr]
            idx_arr += 1
        cnt_num += 1
    sys.stdout.write(f"{ret_val}")


def greedy_5585():
    minus_num = int(sys.stdin.readline())
    cal_num = 1000 - minus_num
    tot_num = 0
    if cal_num // 500 > 0:
        share_num = cal_num // 500
        tot_num += share_num
        cal_num = cal_num - (500 * share_num)
    if cal_num // 100 > 0:
        share_num = cal_num // 100
        tot_num += share_num
        cal_num = cal_num - (100 * share_num)
    if cal_num // 50 > 0:
        share_num = cal_num // 50
        tot_num += share_num
        cal_num = cal_num - (50 * share_num)
    if cal_num // 10 > 0:
        share_num = cal_num // 10
        tot_num += share_num
        cal_num = cal_num - (10 * share_num)
    if cal_num // 5 > 0:
        share_num = cal_num // 5
        tot_num += share_num
        cal_num = cal_num - (5 * share_num)
    if cal_num // 1 > 0:
        share_num = cal_num // 1
        tot_num += share_num
        cal_num = cal_num - (1 * share_num)
    sys.stdout.write(f"{tot_num}")


def search_1543():
    total_str = sys.stdin.readline().rstrip()
    search_str = sys.stdin.readline().rstrip()
    idx = 0
    ret_val = 0
    while True:
        search_len = len(search_str)
        if total_str[idx:idx + search_len] == search_str:
            ret_val += 1
            idx += search_len
        else:
            idx += 1
        if len(total_str) - idx < len(search_str):
            break
    sys.stdout.write(f"{ret_val}\n")


def prog_42883():
    number = "1294"
    k = 2
    arr = []
    for num in number:
        while arr and num > arr[-1]:
            if k > 0:
                arr.pop()
                k -= 1
            else:
                break
        arr.append(num)
    if k > 0:
        for num in range(k):
            arr.pop()
    return "".join(arr)


if __name__ == "__main__":
    # cal_2720()
    # cal_16435()
    # reverse_1439()
    # greedy_11047()
    # greedy_11399()
    # greedy_5585()
    # search_1543()
    prog_42883()
