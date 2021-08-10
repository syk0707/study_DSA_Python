import sys


def direction_11758():
    first_arr = list(map(int, sys.stdin.readline().split()))
    second_arr = list(map(int, sys.stdin.readline().split()))
    third_arr = list(map(int, sys.stdin.readline().split()))
    area = (second_arr[0] - first_arr[0]) * (third_arr[1] - first_arr[1]) - (second_arr[1] - first_arr[1]) * (third_arr[0] - first_arr[0])
    if area == 0:
        sys.stdout.write("0")
    elif area > 0:
        sys.stdout.write("1")
    elif area < 0:
        sys.stdout.write("-1")


if __name__ == "__main__":
    direction_11758()
