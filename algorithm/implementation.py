import sys
import math


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


def arr_2684():
    tot_case = int(sys.stdin.readline())
    # TTT, TTH, THT, THH, HTT, HTH, HHT, HHH
    for case in range(tot_case):
        dic_case = {
            "TTT": 0,
            "TTH": 0,
            "THT": 0,
            "THH": 0,
            "HTT": 0,
            "HTH": 0,
            "HHT": 0,
            "HHH": 0
        }
        text = sys.stdin.readline()
        for idx in range(len(text) - 3):
            word = text[idx] + text[idx + 1] + text[idx + 2]
            dic_case[word] += 1
        for dic_data in dic_case.values():
            sys.stdout.write(str(dic_data) + " ")


def change_str_15814():
    text = sys.stdin.readline()
    tot_idx = int(sys.stdin.readline())
    for idx in range(tot_idx):
        change_arr = list(map(int, sys.stdin.readline().split()))
        first_idx = 0
        second_idx = 0
        if change_arr[0] < change_arr[1]:
            first_idx = change_arr[0]
            second_idx = change_arr[1]
        elif change_arr[1] < change_arr[0]:
            first_idx = change_arr[1]
            second_idx = change_arr[0]
        else:
            continue
        first_char = text[first_idx]
        second_char = text[second_idx]
        text = text[:first_idx] + second_char + text[first_idx + 1: second_idx] + first_char + text[second_idx + 1:]
    sys.stdout.write(text)


def check_num_14656():
    tot_idx = int(sys.stdin.readline())
    tot_arr = list(map(int, sys.stdin.readline().rstrip().split()))
    ret_val = 0
    for idx in range(tot_idx):
        if tot_arr[idx] != idx + 1:
            ret_val += 1
    sys.stdout.write(str(ret_val))


def check_20362():
    tot_case = list(map(str, sys.stdin.readline().split()))
    early_num = 0
    dict_case = {}
    check_word = ''
    for idx in range(int(tot_case[0])):
        each_case = list(map(str, sys.stdin.readline().split()))
        if each_case[0] == tot_case[1]:
            check_word = each_case[1]
            break
        dict_case[each_case[0]] = each_case[1]
    for each_word in dict_case.values():
        if check_word == each_word:
            early_num += 1
    sys.stdout.write(f"{early_num}")


def check_14382():
    tot_idx = int(sys.stdin.readline())
    for idx in range(tot_idx):
        dict_num = {}
        first_num = int(sys.stdin.readline())
        if first_num == 0:
            sys.stdout.write(f"Case #{idx + 1}: INSOMNIA\n")
            continue
        multiple_num = 1
        while True:
            cal_num = multiple_num * first_num
            for each_num in str(cal_num):
                dict_num[int(each_num)] = 1
            if len(dict_num.keys()) == 10:
                sys.stdout.write(f"Case #{idx + 1}: {cal_num}\n")
                break
            multiple_num += 1


def compare_20112():
    tot_num = int(sys.stdin.readline())
    check_arr = []
    is_sator = True
    for tot_idx in range(tot_num):
        check_arr.append(sys.stdin.readline())

    for chk_1_idx in range(len(check_arr)):
        for chk_2_idx in range(len(check_arr)):
            if chk_1_idx == chk_2_idx:
                continue
            check_char_1 = check_arr[chk_1_idx][chk_2_idx]
            check_char_2 = check_arr[chk_2_idx][chk_1_idx]
            if check_char_1 != check_char_2:
                is_sator = False
                break

    if is_sator:
        sys.stdout.write("YES")
    else:
        sys.stdout.write("NO")


def check_1259():
    while True:
        num = int(sys.stdin.readline())
        if num == 0:
            break
        reverse_num = ""
        for char_num in str(num):
            reverse_num = char_num + reverse_num
        reverse_num = int(reverse_num)
        if num == reverse_num:
            sys.stdout.write("yes\n")
        else:
            sys.stdout.write("no\n")


def read_vertical_10798():
    tot_arr = []
    max_len = 0
    print_str = "";
    for idx in range(5):
        input_str = sys.stdin.readline().rstrip()
        tot_arr.append(input_str)
        if max_len < len(input_str):
            max_len = len(input_str)
    for len_idx in range(max_len):
        for arr_idx in range(5):
            each_word = tot_arr[arr_idx]
            if len(each_word) < len_idx + 1:
                continue
            print_str += each_word[len_idx]
    sys.stdout.write(print_str)


def bi_num_11050():
    num_arr = list(map(int, sys.stdin.readline().split()))
    numerator_num = 1
    denominator_num = 1
    for numerator_each_num in range(0, num_arr[1]):
        numerator_num *= (num_arr[0] - numerator_each_num)
    for denominator_each_num in range(1, num_arr[1] + 1):
        denominator_num *= denominator_each_num
    sys.stdout.write(f"{int(numerator_num / denominator_num)}\n")


def capital_sentence_4458():
    tot_idx = int(sys.stdin.readline())
    tot_arr = []
    for idx in range(tot_idx):
        tot_arr.append(sys.stdin.readline())
    for each_item in tot_arr:
        sys.stdout.write(f"{each_item[0].capitalize()}{each_item[1:]}")


def perfect_square_1977():
    start_num = int(sys.stdin.readline())
    end_num = int(sys.stdin.readline())
    tot_num = 0
    min_num = 0
    first_num = math.ceil(math.sqrt(start_num))
    min_num = first_num
    while first_num ** 2 <= end_num:
        if start_num <= first_num ** 2 <= end_num:
            tot_num += first_num ** 2
        first_num += 1
    if tot_num == 0:
        sys.stdout.write(f"{-1}\n")
        return
    sys.stdout.write(f"{tot_num}\n")
    sys.stdout.write(f"{min_num ** 2}")


def type_check_10820():
    while True:
        check_sentence = sys.stdin.readline().rstrip("\n")
        if not check_sentence:
            break
        lower_num = 0
        upper_num = 0
        figure_num = 0
        empty_num = 0
        for char_sentence in check_sentence:
            if char_sentence.islower():
                lower_num += 1
            elif char_sentence.isupper():
                upper_num += 1
            elif char_sentence.isdigit():
                figure_num += 1
            elif char_sentence.isspace():
                empty_num += 1
        sys.stdout.write(f"{lower_num} {upper_num} {figure_num} {empty_num}\n")


def large_num_check_10570():
    tot_num = int(sys.stdin.readline())
    for each_num in range(tot_num):
        case_num = int(sys.stdin.readline())
        case_dic = {}
        for each_case_num in range(case_num):
            input_num = int(sys.stdin.readline())
            if case_dic.get(input_num) is None:
                case_dic[input_num] = 1
            else:
                case_dic[input_num] += 1
        sys.stdout.write(f"{sorted(case_dic.items(), key=lambda x: (-x[1], x[0]))[0][0]}\n")


if __name__ == '__main__':
    # rectangles_15232()
    # freq_num_14912()
    # arr_2684()
    # change_str_15814()
    # check_num_14656()
    # check_20362()
    # check_14382()
    # compare_20112()
    # check_1259()
    # read_vertical_10798()
    # bi_num_11050()
    # capital_sentence_4458()
    # perfect_square_1977()
    # type_check_10820()
    large_num_check_10570()
