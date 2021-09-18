import sys


def compare_10817():
    num_arr = list(map(int, sys.stdin.readline().split()))
    num_arr.sort()
    sys.stdout.write(f"{num_arr[1]}")


if __name__ == "__main__":
    compare_10817()