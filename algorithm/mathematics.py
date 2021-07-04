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


if __name__ == "__main__":
    strange_multiplication_1225()
