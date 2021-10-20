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


def cal_num_1629():
    def recursive_1629(num, n, c):
        if n == 1:
            return num % c
        if n % 2 == 0:
            cal_n = recursive_1629(num, n // 2, c)
            return cal_n * cal_n % c
        else:
            cal_n = recursive_1629(num, n // 2, c)
            return cal_n * cal_n * num % c
        return res
    cal_list = list(map(int, sys.stdin.readline().split()))
    sys.stdout.write(f"{recursive_1629(cal_list[0], cal_list[1], cal_list[2])}")


def prog_add_num_278():
    def solution(n):
        answer = 0
        for each_num in str(n):
            answer += int(each_num)
        print(answer)
        return answer


def cal_num_13706():
    input_num = int(sys.stdin.readline())
    sys.stdout.write(f"{math.isqrt(input_num)}")


def cal_num_1292():
    input_arr = list(map(int, sys.stdin.readline().split()))
    tot_arr = []
    ret_num = 0
    for i in range(101):
        for num in range(0, i):
            tot_arr.append(i)
    for tot_idx in range(input_arr[0] - 1, input_arr[1]):
        ret_num += tot_arr[tot_idx]
    sys.stdout.write(f"{ret_num}")


def cal_num_2745():
    case_arr = list(map(str, sys.stdin.readline().split()))
    sys.stdout.write(f"{int(case_arr[0], int(case_arr[1]))}")


def cal_num_1373():
    num = int(sys.stdin.readline().rstrip(), 2)
    sys.stdout.write(f"{oct(num)[2:]}")


def cal_num_2420():
    num_arr = list(map(int, sys.stdin.readline().split()))
    sys.stdout.write(f"{abs(num_arr[0] - num_arr[1])}")


if __name__ == "__main__":
    # strange_multiplication_1225()
    # get_number_1037()
    # get_number_2417()
    # cal_num_1629()
    # cal_num_13706()
    # cal_num_1292()
    # cal_num_2745()
    # cal_num_1373()
    cal_num_2420()
