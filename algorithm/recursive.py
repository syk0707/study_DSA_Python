import random
import sys

def factorial(n):
    fac = 1
    for idx in range(2, n+1):
        fac = fac * idx
    return fac


def factorial2(n):
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1


def sum_item(data):
    if len(data) <= 1:
        return data[0]
    return data[0] + sum_item(data[1:])


def sum_list():
    list_item = random.sample(range(100), 10)
    print(list_item)
    print(sum_item(list_item))


def palindrome(chk_str):
    if len(chk_str) <= 1:
        return True
    if chk_str[0] == chk_str[-1]:
        return palindrome(chk_str[1:-1])
    else:
        return False


def func(n):
    print(n)
    if n == 1:
        return n
    if n % 2 == 1:
        return func((3 * n) + 1)
    else:
        return func(int(n/2))


def func2(data):
    if data == 1:
        return 1
    elif data == 2:
        return 2
    elif data == 3:
        return 4

    return func2(data - 1) + func2(data - 2) + func2(data - 3)


def chk_binary(num, binary_arr):
    if num == 0:
        for binary_num in range(len(binary_arr), 0, -1):
            print(binary_arr[binary_num - 1], end="")
    else:
        binary_arr.append(num % 2)
        chk_binary(num // 2, binary_arr)


def convert_binary():
    num = int(sys.stdin.readline())
    chk_binary(num, [])


def num_1074():
    ret_val = 0
    tot_num, r, c = list(map(int, sys.stdin.readline().split()))
    while tot_num > 0:
        square = (2 ** tot_num) // 2
        if tot_num > 1:
            if r < square <= c:
                ret_val += square ** 2
                c -= square
            elif r >= square > c:
                ret_val += (square ** 2) * 2
                r -= square
            elif square <= r and square <= c:
                ret_val += (square ** 2) * 3
                r -= square
                c -= square
        elif tot_num == 1:
            if r == 0 and c == 1:
                ret_val += 1
            elif r == 1 and c == 0:
                ret_val += 2
            elif r == 1 and c == 1:
                ret_val += 3
        tot_num -= 1
    sys.stdout.write(f"{ret_val}")


if __name__ == "__main__":
    # print(factorial(10))
    # print(factorial2(10))
    # sum_list()
    # print(palindrome("test"))
    # func(3)
    # print(func2(5))
    # convert_binary()
    num_1074()

