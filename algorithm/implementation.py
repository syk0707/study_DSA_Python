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


if __name__ == '__main__':
    # rectangles_15232()
    # freq_num_14912()
    arr_2684()
