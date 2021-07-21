import math
import sys


def strange_multiplication_1225():
    case_arr = list(map(int, sys.stdin.readline().split()))
    case_1_val = 0
    case_2_val = 0
    for num1 in str(case_arr[0]):
        case_1_val += int(num1)
    for num2 in str(case_arr[1]):
        case_2_val += int(num2)
    sys.stdout.write(f"{case_1_val * case_2_val}")


def get_number_1037():
    case_num = int(sys.stdin.readline())
    tot_arr = list(map(int, sys.stdin.readline().split()))
    tot_arr.sort()
    small_num = tot_arr[0]
    large_num = tot_arr[case_num - 1]
    sys.stdout.write(f"{small_num * large_num}")


def get_number_2417():
    num = int(sys.stdin.readline())
    sys.stdout.write(f"{math.ceil(num ** 0.5)}")


if __name__ == "__main__":
    # strange_multiplication_1225()
    # get_number_1037()
    get_number_2417()
