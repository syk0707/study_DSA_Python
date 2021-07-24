import time
import sys


def join_arr_11728():
    tot_case = list(map(int, sys.stdin.readline().split()))
    first_arr = list(map(int, sys.stdin.readline().split()))
    second_arr = list(map(int, sys.stdin.readline().split()))
    first_arr += second_arr
    sys.stdout.write(f"{' '.join(str(i) for i in sorted(first_arr))}")


def find_arr_1920():
    tot_n = int(sys.stdin.readline())
    tot_dic = set(sys.stdin.readline().split())
    case_m = int(sys.stdin.readline())
    case_arr = sys.stdin.readline().split()
    for case_num in case_arr:
        if case_num in tot_dic:
            sys.stdout.write("1\n")
        else:
            sys.stdout.write("0\n")


if __name__ == "__main__":
    # join_arr_11728()
    find_arr_1920()
