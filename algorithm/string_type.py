import sys
import math


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
    str_vowel = sys.stdin.readline().rstrip()
    ret_val = 0
    for idx in range(len(str_vowel)):
        if str_vowel[idx] == "a" or str_vowel[idx] == "e" or str_vowel[idx] == "i" or str_vowel[idx] == "o" or str_vowel[idx] == "u":
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


def get_num_10821():
    tot_arr = sys.stdin.readline().split(",")
    sys.stdout.write(str(len(tot_arr)))


def get_str_20114():
    num_arr = list(map(int, sys.stdin.readline().rstrip().split()))
    char_arr = ["?" for i in range(num_arr[0])]
    for idx in range(num_arr[1]):
        sentence = sys.stdin.readline().rstrip()
        for len_sentence in range(len(sentence)):
            if sentence[len_sentence] != "?":
                char_arr[math.ceil((len_sentence + 1) / num_arr[2]) - 1] = sentence[len_sentence]
    sys.stdout.write(f"{''.join(char_arr)}")


def check_sentence_15813():
    num = int(sys.stdin.readline())
    name = sys.stdin.readline().rstrip()
    char_arr = [char for char in name]
    print(char_arr)
    ret_val = 0
    for char in char_arr:
        ret_val += ord(char) - 64
    print(ret_val)


def string_print_15680():
    case_num = int(sys.stdin.readline())
    if case_num == 0:
        sys.stdout.write("YONSEI")
    elif case_num == 1:
        sys.stdout.write("Leading the Way to the Future")


def string_print_13752():
    total_idx = int(sys.stdin.readline())
    for idx in range(total_idx):
        num = int(sys.stdin.readline())
        sys.stdout.write(f"{num * '='}\n")


def print_star_10995():
    tot_idx = int(sys.stdin.readline())
    for idx in range(tot_idx):
        if idx % 2 == 0:
            print_str = '* ' * tot_idx
        else:
            print_str = ' *' * tot_idx
        sys.stdout.write(f"{print_str.rstrip()}\n")


def string_print_16394():
    num = int(sys.stdin.readline())
    sys.stdout.write(f"{num - 1946}\n")


def get_word_count_5586():
    word = sys.stdin.readline()
    joi_cnt = 0
    ioi_cnt = 0
    if len(word) < 3:
        sys.stdout.write(f"{joi_cnt}\n")
        sys.stdout.write(f"{ioi_cnt}")
        return
    for idx in range(len(word) - 2):
        chk_str = f"{word[idx]}{word[idx + 1]}{word[idx + 2]}"
        if chk_str == "JOI":
            joi_cnt += 1
        elif chk_str == "IOI":
            ioi_cnt += 1
    sys.stdout.write(f"{joi_cnt}\n")
    sys.stdout.write(f"{ioi_cnt}")


def change_type_2998():
    num = sys.stdin.readline().rstrip()
    cal_num = int(f"0b{num}", 2)
    sys.stdout.write(f"{oct(cal_num)[2:]}")


def string_print_11721():
    input_sentence = sys.stdin.readline().rstrip()
    tot_len = int(len(input_sentence) / 10) + 1
    for idx in range(tot_len):
        current_idx = idx * 10
        if idx != tot_len - 1:
            sys.stdout.write(f"{input_sentence[current_idx:current_idx+10]}\n")
        else:
            sys.stdout.write(input_sentence[current_idx:len(input_sentence)])


if __name__ == "__main__":
    # chk_palindrome_10988()
    # print_11718()
    # merge_17202()
    # get_vowel_10987()
    # get_char_12778()
    # get_num_10821()
    # get_str_20114()
    # check_sentence_15813()
    # string_print_15680()
    # string_print_13752()
    # print_star_10995()
    # string_print_16394()
    # get_word_count_5586()
    # change_type_2998()
    string_print_11721()
