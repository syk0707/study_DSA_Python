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


if __name__ == '__main__':
    # rectangles_15232()
    freq_num_14912()
