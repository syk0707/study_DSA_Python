import sys


def chk_palindrome_10988():
    txt = sys.stdin.readline().rstrip()
    ret_val = 1
    for idx in range(len(txt)):
        last_idx = len(txt) - idx - 1
        if txt[idx] is not txt[last_idx]:
            ret_val = 0
    sys.stdout.write(f"{ret_val}")


def print_11718():
    ret_arr = sys.stdin.readlines()
    sys.stdout.writelines(ret_arr)


def merge_17202():
    read_num_1 = sys.stdin.readline().rstrip()
    read_num_2 = sys.stdin.readline().rstrip()

    tot_num = ""
    for idx in range(len(read_num_1)):
        tot_num += read_num_1[idx]
        tot_num += read_num_2[idx]

    while True:
        ret_num = ""
        for num_idx in range(len(tot_num) - 1):
            ret_num += str((int(tot_num[num_idx]) + int(tot_num[num_idx + 1])) % 10)
        tot_num = ret_num
        if len(tot_num) <= 2:
            break
    sys.stdout.write(tot_num)


if __name__ == "__main__":
    # chk_palindrome_10988()
    # print_11718()
    merge_17202()
