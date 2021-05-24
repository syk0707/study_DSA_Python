import sys


def rectangles_15232():
    r = int(sys.stdin.readline())
    c = int(sys.stdin.readline())
    for idx in range(r):
        sys.stdout.write(f"{'*' * c}\n")


def freq_num_14912():
    num_arr = list(map(int, sys.stdin.readline().split()))
    tot = 0
    for idx in range(1, num_arr[0] + 1):
        for num_str in str(idx):
            if num_str == str(num_arr[1]):
                tot += 1
    sys.stdout.write(f"{tot}")


def arr_2684():
    tot_case = int(sys.stdin.readline())
    # TTT, TTH, THT, THH, HTT, HTH, HHT, HHH
    for case in range(tot_case):
        dic_case = {
            "TTT": 0,
            "TTH": 0,
            "THT": 0,
            "THH": 0,
            "HTT": 0,
            "HTH": 0,
            "HHT": 0,
            "HHH": 0
        }
        text = sys.stdin.readline()
        for idx in range(len(text) - 3):
            word = text[idx] + text[idx + 1] + text[idx + 2]
            dic_case[word] += 1
        for dic_data in dic_case.values():
            sys.stdout.write(str(dic_data) + " ")


def change_str_15814():
    text = sys.stdin.readline()
    tot_idx = int(sys.stdin.readline())
    for idx in range(tot_idx):
        change_arr = list(map(int, sys.stdin.readline().split()))
        first_idx = 0
        second_idx = 0
        if change_arr[0] < change_arr[1]:
            first_idx = change_arr[0]
            second_idx = change_arr[1]
        elif change_arr[1] < change_arr[0]:
            first_idx = change_arr[1]
            second_idx = change_arr[0]
        else:
            continue
        first_char = text[first_idx]
        second_char = text[second_idx]
        text = text[:first_idx] + second_char + text[first_idx + 1: second_idx] + first_char + text[second_idx + 1:]
    sys.stdout.write(text)


def check_num_14656():
    tot_idx = int(sys.stdin.readline())
    tot_arr = list(map(int, sys.stdin.readline().rstrip().split()))
    ret_val = 0
    for idx in range(tot_idx):
        if tot_arr[idx] != idx + 1:
            ret_val += 1
    sys.stdout.write(str(ret_val))


if __name__ == '__main__':
    # rectangles_15232()
    # freq_num_14912()
    # arr_2684()
    # change_str_15814()
    check_num_14656()
