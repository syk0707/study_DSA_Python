import math
# It costs a fixed cost of A dollars, and it is said that producing a single product costs a total of B dollars, including material costs and labor costs. 
# If the price of the item is set at C dollars, find a break-even point.
def break_even_point():
    num_arr = list(map(int, input().split()))
    n = 0
    if num_arr[1] >= num_arr[2]:
        n = -1
    else:
        n = (num_arr[0] / (num_arr[2] - num_arr[1])) + 1
    print(int(n))

#1, 7, 19, 37... There are whiskers that increase in order. Find out which order a particular number is placed in that sequence.
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

#1/1 -> 1/2 -> 2/1 -> 3/1 -> 2/2 -> … In the order of zigzags as shown in , number 1, 2, 3, 4, 5, … fraction.
#When given an X, write a program to find the X-th fraction.
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
    #1 - numerator is larger than denominator, 2 - denominator is larger than numerator
    numerator = 0
    denominator = 0
    diff_num = last_num - check_num
    if(count % 2 == 0):
        #is_big_numerator = False
        numerator = increase_num - diff_num - 1
        denominator = 1 + diff_num
    else:
        numerator = 1 + diff_num
        denominator = increase_num - diff_num - 1
    #above python 3
    print('{numerator}/{denominator}'.format(numerator=numerator, denominator=denominator))
    #above python 3.6
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
    #math.ceil : Round up, math.floor : Round down, math.round
    print(math.ceil(total_day))

def find_floor():
    total_length = int(input())
    str_array = []
    for idx in range(total_length):
        hotel_arr = list(map(int, input().split()))
        height = hotel_arr[0]
        arrival_number = hotel_arr[2]          
        # top floor
        if(arrival_number % height == 0):
            room_num = int(arrival_number / height)
            str_array.append(f'{height}{room_num if room_num >= 10 else "0" + str(room_num)}')
        else:
            room_num = int(arrival_number / height) + 1
            str_array.append(f'{arrival_number % height}{room_num if room_num >= 10 else "0" + str(room_num)}')
    for string in str_array:
        print(string)

if __name__ == "__main__":
    #break_even_point()
    #check_num()
    #find_fractional_numbers()
    #cal_climb()
    find_floor()