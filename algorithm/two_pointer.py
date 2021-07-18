import sys


def join_arr_11728():
    tot_case = list(map(int, sys.stdin.readline().split()))
    first_arr = list(map(int, sys.stdin.readline().split()))
    second_arr = list(map(int, sys.stdin.readline().split()))
    first_arr += second_arr
    sys.stdout.write(f"{' '.join(str(i) for i in sorted(first_arr))}")


if __name__ == "__main__":
    join_arr_11728()