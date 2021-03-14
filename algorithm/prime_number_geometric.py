import math 

# check prime number
def check_prime_number(num):
    if num == 1:
        return False
    for idx in range(num - 1):
        divide_num = idx + 1
        if divide_num == 1:
            continue
        elif num % divide_num == 0:
            return False
    print(num)


# Write a program that finds and prints how many of the given N are.
def find_prime_number():
    check_length = int(input())
    number_array = list(map(int, input().split()))
    prime_num = 0
    for num in number_array:
        is_prime_num = check_prime_number(num)
        if is_prime_num is True:
            prime_num += 1
    print(prime_num)


# When given natural numbers M and N, write a program
# to find the sum and minimum of these few numbers by selecting all the natural numbers above M and below N.
def find_prime_number_array():
    start_num = int(input())
    end_num = int(input()) + 1
    minimum_num = -1
    total_num = 0
    for idx in range(start_num, end_num):
        is_prime_num = check_prime_number(idx)
        if is_prime_num is True and minimum_num == -1: 
            minimum_num = idx
            total_num += idx
        elif is_prime_num is True:
            total_num += idx
    if minimum_num != -1:
        print(total_num)
    print(minimum_num)


def factorization():
    num = int(input())
    divide_num_array = []
    divide_num = 2
    while True:
        if num % divide_num == 0:
            num = num / divide_num
            divide_num_array.append(divide_num)
            divide_num = 2
        else:
            divide_num += 1
        if num == 1:
            break
    for num in divide_num_array:
        print(num)


def short_distance_rectangular():
    input_arr = list(map(int, input().split()))
    x = input_arr[0]
    y = input_arr[1]
    max_w = input_arr[2]
    max_h = input_arr[3]
    short_distance = x
    if y < x:
        short_distance = y
    if short_distance > (max_w - x):
        short_distance = max_w - x
    if short_distance > (max_h - y):
        short_distance = max_h - y
    print(short_distance)


def find_prime_number_range():
    num_input_arr = list(map(int, input().split()))
    ret_arr = []
    num_arr = list(range(num_input_arr[0], num_input_arr[1] + 1))
    for num in range(num_input_arr[0], num_input_arr[1] + 1):
        is_prime_num = check_prime_number(num)
        if is_prime_num:
            ret_arr.append(num)


def find_coordinate_rectangle():
    x_coordinate = {}
    y_coordinate = {}
    for idx in range(3):
        input_arr = list(map(int, input().split()))
        if x_coordinate.get(input_arr[0]) is None:
            x_coordinate[input_arr[0]] = 1
        else:
            x_coordinate[input_arr[0]] += 1
        if y_coordinate.get(input_arr[1]) is None:
            y_coordinate[input_arr[1]] = 1
        else:
            y_coordinate[input_arr[1]] += 1
    x = 0
    y = 0
    for each_x in x_coordinate.keys():
        if(x_coordinate[each_x] == 1):
            x = each_x
    for each_y in y_coordinate.keys():
        if(y_coordinate[each_y] == 1):
            y = each_y
    print(f"{x} {y}")


def check_right_triangle():
    ret_arr = []
    while True:
        input_arr = list(map(int, input().split()))
        if (input_arr[0] == 0 and input_arr[1] == 0 and input_arr[2] == 0):
            break
        large_num = input_arr[0]
        check_num_1 = 0
        check_num_2 = 0
        if(large_num < input_arr[1]):
            check_num_1 = large_num
            large_num = input_arr[1]
        else:
            check_num_1 = input_arr[1]
        if(large_num < input_arr[2]):
            check_num_2 = large_num
            large_num = input_arr[2]
        else:
            check_num_2 = input_arr[2]
        if check_num_1 ** 2 + check_num_2 ** 2 == large_num ** 2:
            ret_arr.append('right')
        else:
            ret_arr.append('wrong')
    for ret_val in ret_arr:
        print(ret_val)


def calculate_circle_area():
    radius = int(input())
    circle_euclidean = radius ** 2 * math.pi 
    circle_taxi = (radius * 2) * radius
    print('%.6f' % circle_euclidean)
    print('%.6f' % circle_taxi)


def find_prime_number_eratosthenes():
    check_obj = {}
    check_prime_num_arr = list(map(int, input().split()))
    for i in range(2, check_prime_num_arr[1] + 1):
        check_obj[i] = True
    max_check_num = int(check_prime_num_arr[1] ** 0.5)
    for j in range(2, max_check_num + 1):
        if check_obj.get(j) is True:
            for k in range(j + j, check_prime_num_arr[1] + 1, j):
                check_obj[k] = False
    minimum_num = check_prime_num_arr[0]
    for key in check_obj:
        if minimum_num > key:
            continue
        check_val = check_obj[key]
        if check_val is True:
            print(key)

if __name__ == "__main__":
    #find_prime_number()
    #find_prime_number_array()
    #factorization()
    #short_distance_rectangular()
    #find_prime_number_range()
    #find_coordinate_rectangle()
    #check_right_triangle()
    #calculate_circle_area()
    find_prime_number_eratosthenes()