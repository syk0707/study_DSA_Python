import sys
import math
import string
import calendar
import hashlib
from collections import Counter


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


def num_check_10797():
    case_num = int(sys.stdin.readline())
    case_arr = list(map(int, sys.stdin.readline().split()))
    ret_num = 0
    for each_num in case_arr:
        if each_num % 10 == case_num:
            ret_num += 1
    sys.stdout.write(f"{ret_num}")


def round_2033():
    check_num = int(sys.stdin.readline())
    divide_num = 10
    while check_num > divide_num:
        if check_num % divide_num >= divide_num // 2:
            check_num += divide_num
        check_num -= (check_num % divide_num)
        divide_num *= 10
    sys.stdout.write(f"{check_num}")


def add_1357():
    case_arr = list(map(int, sys.stdin.readline().split()))
    first_reverse_num = int(str(case_arr[0])[::-1])
    second_reverse_num = int(str(case_arr[1])[::-1])
    sys.stdout.write(f"{int(str(first_reverse_num + second_reverse_num)[::-1])}")


def print_11586():
    total_num = int(sys.stdin.readline())
    tot_arr = []
    for idx in range(total_num):
        tot_arr.append(sys.stdin.readline().rstrip())
    case_num = int(sys.stdin.readline())
    if case_num == 3:
        for sentence in reversed(tot_arr):
            sys.stdout.write(f"{sentence}\n")
    elif case_num == 1:
        for sentence in tot_arr:
            sys.stdout.write(f"{sentence}\n")
    elif case_num == 2:
        for sentence in tot_arr:
            sys.stdout.write(f"{''.join(reversed(sentence))}\n")


def add_2729():
    tot_case = int(sys.stdin.readline())
    for idx in range(tot_case):
        case_arr = list(map(int, sys.stdin.readline().split()))
        first_num = "0b" + str(case_arr[0])
        second_num = "0b" + str(case_arr[1])
        sys.stdout.write(f"{'{0:b}'.format(int(first_num, 2) + int(second_num, 2))}\n")


def change_num(number, notation):
    notation_array = string.digits + string.ascii_uppercase
    ret_val = ''
    while number > 0:
        number, mod = divmod(number, notation)
        str_mod = notation_array[mod]
        ret_val += str_mod
    return ret_val[::-1]


def change_11005():
    case_arr = list(map(int, sys.stdin.readline().split()))
    sys.stdout.write(f"{change_num(case_arr[0], case_arr[1])}")


def cal_1924():
    check_day = list(map(int, sys.stdin.readline().split()))
    day_num = calendar.weekday(2007, check_day[0], check_day[1])
    if day_num == 6:
        sys.stdout.write("SUN")
    elif day_num == 0:
        sys.stdout.write("MON")
    elif day_num == 1:
        sys.stdout.write("TUE")
    elif day_num == 2:
        sys.stdout.write("WED")
    elif day_num == 3:
        sys.stdout.write("THU")
    elif day_num == 4:
        sys.stdout.write("FRI")
    elif day_num == 5:
        sys.stdout.write("SAT")


def string_11655():
    sentence = sys.stdin.readline()
    ret_sentence = ''
    for character in sentence:
        ascii_num = ord(character)
        if 65 <= ascii_num <= 77 or 97 <= ascii_num <= 109:
            ret_sentence += chr(ascii_num + 13)
        elif 78 <= ascii_num <= 90:
            ret_sentence += chr(65 + (13 - (90 - ascii_num) - 1))
        elif 110 <= ascii_num <= 122:
            ret_sentence += chr(97 + (13 - (122 - ascii_num) - 1))
        else:
            ret_sentence += character
    sys.stdout.write(f"{ret_sentence}")


def string_10808():
    input_word = sys.stdin.readline().rstrip()
    input_dict = {}
    for each_num in range(97, 123):
        input_dict[each_num] = 0
    for each_word in input_word:
        ascii_num = ord(each_word)
        input_dict[ascii_num] += 1
    for each_val in input_dict.values():
        sys.stdout.write(f"{each_val} ")


def string_encode_10930():
    input_str = sys.stdin.readline().rstrip()
    ret_hash = hashlib.sha256(input_str.encode())
    sys.stdout.write(f"{ret_hash.hexdigest()}")


def count_1568():
    input_num = int(sys.stdin.readline())
    add_num = 0
    tot_num = 0
    tot_sec = 0
    while True:
        if input_num <= tot_num:
            break
        add_num += 1
        tot_sec += 1
        if add_num > input_num - tot_num:
            add_num = 1
        tot_num += add_num
    sys.stdout.write(f"{tot_sec}\n")


def get_num_1236():
    input_arr = list(map(int, sys.stdin.readline().split()))
    ret_num = 0
    vertical_dic = {i + 1: 0 for i in range(input_arr[1])}
    for idx in range(input_arr[0]):
        line_str = sys.stdin.readline()
        # 가로
        if line_str.find("X") == -1:
            ret_num += 1
        v_idx = 0
        # 세로
        while v_idx > -1:
            v_idx = line_str.find('X', v_idx)
            if vertical_dic.get(v_idx + 1) is not None:
                del vertical_dic[v_idx + 1]
            if v_idx > -1:
                v_idx += 1
    sys.stdout.write(f"{max(ret_num, len(vertical_dic.keys()))}")


def cal_num_1453():
    input_num = int(sys.stdin.readline())
    input_arr = list(map(int, sys.stdin.readline().split()))
    input_dic = {}
    except_num = 0
    for num in input_arr:
        if input_dic.get(num) is None:
            input_dic[num] = 1
        else:
            except_num += 1
    sys.stdout.write(f"{except_num}")


def get_num_10807():
    tot_num = int(sys.stdin.readline())
    tot_arr = list(map(int, sys.stdin.readline().split()))
    tot_dic = Counter(tot_arr)
    print_num = tot_dic.get(int(sys.stdin.readline()))
    if print_num is None:
        sys.stdout.write(f"0")
    else:
        sys.stdout.write(f"{print_num}")


def arrange_3047():
    tot_arr = list(map(int, sys.stdin.readline().split()))
    tot_dic = {}
    tot_arr.sort()
    tot_dic["A"] = tot_arr[0]
    tot_dic["B"] = tot_arr[1]
    tot_dic["C"] = tot_arr[2]
    print_case = sys.stdin.readline().rstrip()
    for case_char in print_case:
        sys.stdout.write(f"{tot_dic[case_char]} ")


def check_num_5597():
    tot_dic = {}
    for idx in range(30):
        tot_dic[idx + 1] = 1
    for case_idx in range(28):
        tot_dic.pop(int(sys.stdin.readline()))
    for each_key in tot_dic.keys():
        sys.stdout.write(f"{each_key}\n")


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
    # large_num_check_10570()
    # num_check_10797()
    # round_2033()
    # add_1357()
    # print_11586()
    # add_2729()
    # change_11005()
    # cal_1924()
    # string_11655()
    # string_10808()
    # string_encode_10930()
    # count_1568()
    # get_num_1236()
    # cal_num_1453()
    # get_num_10807()
    # arrange_3047()
    check_num_5597()
