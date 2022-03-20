import sys


def bitmask_11723():
    tot_idx = int(sys.stdin.readline())
    case_dic = {i + 1: 0 for i in range(20)}
    case_all_dic = {i + 1: 1 for i in range(20)}
    case_empty_dic = case_dic.copy()
    for idx in range(tot_idx):
        input_arr = list(map(str, sys.stdin.readline().split()))
        case_str = input_arr[0]
        input_num = -1
        if len(input_arr) > 1:
            input_num = int(input_arr[1])
        if case_str == "add":
            case_dic[input_num] = 1
        elif case_str == "check":
            if case_dic.get(input_num) == 1:
                sys.stdout.write("1\n")
            else:
                sys.stdout.write("0\n")
        elif case_str == "remove":
            case_dic[input_num] = 0
        elif case_str == "toggle":
            if case_dic.get(input_num) == 1:
                case_dic[input_num] = 0
            else:
                case_dic[input_num] = 1
        elif case_str == "all":
            case_dic = case_all_dic.copy()
        elif case_str == "empty":
            case_dic = case_empty_dic.copy()


if __name__ == "__main__":
    bitmask_11723()
