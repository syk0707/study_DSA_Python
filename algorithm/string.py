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


def get_vowel_10987():
    str = sys.stdin.readline().rstrip()
    ret_val = 0
    for idx in range(len(str)):
        if str[idx] == "a" or str[idx] == "e" or str[idx] == "i" or str[idx] == "o" or str[idx] == "u":
            ret_val += 1
    print(ret_val)


def get_num_to_char_12778(text_arr):
    return_text = ""
    idx = 0
    for text in text_arr:
        num = int(text) + 64
        if len(text_arr) - 1 != idx:
            return_text += chr(num) + " "
        else:
            return_text += chr(num)
        idx += 1
    return return_text


def get_char_to_num_12778(text_arr):
    return_text = ""
    idx = 0
    for text in text_arr:
        num = ord(text) - 64
        if len(text_arr) - 1 != idx:
            return_text += str(num) + " "
        else:
            return_text += str(num)
        idx += 1
    return return_text


def get_char_12778():
    tot_idx = int(sys.stdin.readline())
    print_lines = []
    for idx in range(tot_idx):
        case_arr = list(map(str, sys.stdin.readline().split()))
        question_arr = list(map(str, sys.stdin.readline().split()))
        if case_arr[1] == "C":
            print_lines.append(get_char_to_num_12778(question_arr))
        else:
            print_lines.append(get_num_to_char_12778(question_arr))
    for print_line in print_lines:
        sys.stdout.write(print_line + "\n")


if __name__ == "__main__":
    # chk_palindrome_10988()
    # print_11718()
    # merge_17202()
    # get_vowel_10987()
    get_char_12778()
