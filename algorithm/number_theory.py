import math
import sys


def get_lcm_1934():
    tot_case = int(sys.stdin.readline())
    for idx in range(tot_case):
        case_arr = list(map(int, sys.stdin.readline().split()))
        sys.stdout.write(f"{math.lcm(case_arr[0], case_arr[1])}\n")


if __name__ == "__main__":
    get_lcm_1934()
