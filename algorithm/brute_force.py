import sys


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


if __name__ == "__main__":
    # black_jack_2798()
    # get_num_14914()
    get_num_2501()
