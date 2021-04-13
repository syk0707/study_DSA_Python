import math
import sys


# It costs a fixed cost of A dollars, and it is said that producing a single product costs a total of B dollars,
# including material costs and labor costs.
# If the price of the item is set at C dollars, find a break-even point.
def break_even_point():
    num_arr = list(map(int, input().split()))
    n = 0
    if num_arr[1] >= num_arr[2]:
        n = -1
    else:
        n = (num_arr[0] / (num_arr[2] - num_arr[1])) + 1
    print(int(n))


# 1, 7, 19, 37... There are whiskers that increase in order.
# Find out which order a particular number is placed in that sequence.
def check_num():
    num = int(input())
    sum = 1
    cnt = 0
    while sum <= num:
        sum += (6 * cnt)
        cnt += 1
        if sum == num:
            break
    print(cnt)


# 1/1 -> 1/2 -> 2/1 -> 3/1 -> 2/2 -> … In the order of zigzags as shown in , number 1, 2, 3, 4, 5, … fraction.
# When given an X, write a program to find the X-th fraction.
def find_fractional_numbers():
    check_num = int(input())
    increase_num = 1
    total = 0
    count = 0
    while True:
        if check_num <= total:
            break
        total += increase_num
        increase_num += 1
        count += 1
    last_num = total
    # 1 - numerator is larger than denominator, 2 - denominator is larger than numerator
    numerator = 0
    denominator = 0
    diff_num = last_num - check_num
    if count % 2 == 0:
        # is_big_numerator = False
        numerator = increase_num - diff_num - 1
        denominator = 1 + diff_num
    else:
        numerator = 1 + diff_num
        denominator = increase_num - diff_num - 1
    # above python 3
    print('{numerator}/{denominator}'.format(numerator=numerator, denominator=denominator))
    # above python 3.6
    print(f'{numerator}/{denominator}')


# I can go up A meter during the day. However, it slips B meters while sleeping at night.
# Also, it does not slip after climbing to the top. How many days will it take to get up?
def cal_climb():
    input_arr = list(map(int, input().split()))
    up_meter = input_arr[0]
    down_meter = input_arr[1]
    up_day_meter = up_meter - down_meter
    total_meter = input_arr[2] - down_meter
    total_day = total_meter / up_day_meter
    # math.ceil : Round up, math.floor : Round down, math.round
    print(math.ceil(total_day))


def find_floor():
    total_length = int(input())
    str_array = []
    for idx in range(total_length):
        hotel_arr = list(map(int, input().split()))
        height = hotel_arr[0]
        arrival_number = hotel_arr[2]
        # top floor
        if arrival_number % height == 0:
            room_num = int(arrival_number / height)
            str_array.append(f'{height}{room_num if room_num >= 10 else "0" + str(room_num)}')
        else:
            room_num = int(arrival_number / height) + 1
            str_array.append(f'{arrival_number % height}{room_num if room_num >= 10 else "0" + str(room_num)}')
    for string in str_array:
        print(string)


def print_resident():
    total_items = int(input())
    input_arr = []
    for idx in range(total_items * 2):
        num = int(input())
        input_arr.append(num)
    for arr_idx in range(0, int(len(input_arr) / 2)):
        total_floor = input_arr[arr_idx * 2]
        total_arc = input_arr[arr_idx * 2 + 1]
        floor_list = [floor for floor in range(1, total_arc + 1)]
        for floor in range(total_floor):
            for arc in range(1, total_arc):
                floor_list[arc] += floor_list[arc - 1]
        print(floor_list[total_arc - 1])


def cal_large_num():
    cal_arr = list(map(int, input().split()))
    print(cal_arr[0] + cal_arr[1])


def cal_reminder():
    total = int(input())
    cnt = 0
    while True:
        if total % 5 == 0:
            cnt = cnt + total // 5
            break
        total -= 3
        cnt += 1
        if total < 0:
            cnt = -1
            break
    print(cnt)


def cal_distance_move():
    total_cnt = int(input())
    ans = 0
    diff = 1
    cnt = 0
    result_obj = {}
    while True:
        ans += diff
        diff += 1
        cnt += 1
        result_obj[ans] = cnt
        if ans > 2 ** 31:
            break
    print(result_obj)
    for cnt in range(total_cnt):
        ret_val = 0
        dist_coordinates = list(map(int, input()))
        total_dist = dist_coordinates[0] - dist_coordinates[1] - 1
        print(result_obj[total_dist] + 1)


def divide_num_1312():
    divide_arr = list(map(int, sys.stdin.readline().split()))
    divide_arr[0] = divide_arr[0] % divide_arr[1]
    for idx in range(divide_arr[2] - 1):
        divide_arr[0] = (divide_arr[0] * 10) % divide_arr[1]
    print((divide_arr[0] * 10) // divide_arr[1])


def divide_num_1271():
    divide_arr = list(map(int, sys.stdin.readline().split()))
    print(divide_arr[0] // divide_arr[1])
    print(divide_arr[0] % divide_arr[1])


# After receiving two integers A and B, write a program that outputs A+B.
def addition_2558():
    add_num_1 = int(sys.stdin.readline())
    add_num_2 = int(sys.stdin.readline())
    print(add_num_1 + add_num_2)


# Output the average score of 5 students
def cal_average_10039():
    total_score = 0
    for idx in range(5):
        chk_num = int(sys.stdin.readline())
        if chk_num < 40:
            chk_num = 40
        total_score += chk_num
    print(int(total_score / 5))


def cal_num_1009():
    total_num = int(sys.stdin.readline())
    total_arr = []
    for idx in range(total_num):
        total_arr.append(list(map(int, sys.stdin.readline().split())))
    for item in total_arr:
        # item[0]의 item[1] 제곱을 10으로 나눈 나머지
        # cf) pow(item[0], item[1]) item[0]의 item[1] 제곱
        num = pow(item[0], item[1], 10)
        if num == 0:
            print(10)
        else:
            print(num)


def cal_num_2338():
    first_num = int(sys.stdin.readline())
    second_num = int(sys.stdin.readline())
    sys.stdout.write(f"{first_num + second_num}\n")
    sys.stdout.write(f"{first_num - second_num}\n")
    sys.stdout.write(f"{first_num * second_num}\n")


def get_num_11170():
    total_idx = int(sys.stdin.readline())
    for idx in range(total_idx):
        input_arr = list(map(int, sys.stdin.readline().split()))
        zero_num = 0
        for num in range(input_arr[0], input_arr[1] + 1):
            for str_num in str(num):
                if str_num == "0":
                    zero_num += 1
        sys.stdout.write(f"{zero_num} \n")


def get_max_num_11557():
    total_case = int(sys.stdin.readline())
    for idx in range(total_case):
        each_case = int(sys.stdin.readline())
        max_num = 0
        max_university = ""
        for each_idx in range(each_case):
            each_arr = list(map(str, sys.stdin.readline().split()))
            if each_idx == 0:
                max_university = each_arr[0]
                max_num = int(each_arr[1])
            else:
                if max_num < int(each_arr[1]):
                    max_university = each_arr[0]
                    max_num = int(each_arr[1])
        sys.stdout.write(f"{max_university}\n")


def get_max_num_2822():
    total_dic = {}
    for idx in range(8):
        num = int(sys.stdin.readline())
        if idx < 5:
            total_dic[num] = idx+1
        else:
            minimum_num = sorted(total_dic)[0]
            if minimum_num < num:
                total_dic.pop(minimum_num)
                total_dic[num] = idx+1
    total_score = 0
    total_idx = ""
    for key, value in total_dic.items():
        total_score += key
        total_idx += f"{value} "
    print(total_score)
    print(total_idx)


def numeral_11179():
    input_val = int(sys.stdin.readline())
    binary_num = format(input_val, 'b')
    num_str = ''
    for binary_str in str(binary_num):
        num_str = f"{binary_str}{num_str}"
    sys.stdout.write(f"{int(num_str, 2)}")


def numeral_1550():
    input_val = sys.stdin.readline()
    sys.stdout.write(f"{int(input_val, 16)}")


def add_num_10953():
    total_len = int(sys.stdin.readline())
    for idx in range(total_len):
        num_arr = list(map(int, sys.stdin.readline().split(",")))
        sys.stdout.write(f"{num_arr[0] + num_arr[1]}\n")


if __name__ == "__main__":
    # break_even_point()
    # check_num()
    # find_fractional_numbers()
    # cal_climb()
    # find_floor()
    # cal_large_num()
    # cal_reminder()
    # print_resident()
    # cal_distance_move()
    # divide_num_1312()
    # divide_num_1271()
    # addition_2558()
    # cal_average_10039()
    # cal_num_1009()
    # cal_num_2338()
    # get_num_11170()
    # get_max_num_11557()
    # get_max_num_2822()
    # numeral_11179()
    # numeral_1550()
    add_num_10953()
