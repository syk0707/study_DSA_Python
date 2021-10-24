import sys


# sample - use recursive call
# fibonacci(3) = fibonacci(2) + fibonacci(1)
def recursive_fibonacci(num):
    if num <= 1:
        return num
    return recursive_fibonacci(num - 1) + recursive_fibonacci(num - 2)


# sample - use dynamic programming
def dynamic_fibonacci(num):
    cache = [0 for idx in range(num + 1)]
    cache[0] = 0
    cache[1] = 1
    for idx in range(2, num + 1):
        cache[idx] = cache[idx - 1] + cache[idx - 2]
    return cache[num]


def fibonacci_2748():
    num = int(sys.stdin.readline())
    arr = [0 for idx in range(num + 1)]
    arr[0] = 0
    if num != 0:
        arr[1] = 1

    for idx in range(2, num + 1):
        arr[idx] = arr[idx - 1] + arr[idx - 2]
    return arr[num]


def fibonacci_9625():
    num = int(sys.stdin.readline())
    arr = [0 for idx in range(num + 2)]
    arr[0] = 0
    arr[1] = 1
    arr[2] = 1

    for idx in range(2, num + 2):
        arr[idx] = arr[idx - 1] + arr[idx - 2]
    print(f"{arr[num - 1]} {arr[num]}")


def fibonacci_1003():
    tot_num = int(sys.stdin.readline())
    for idx in range(tot_num):
        case_num = int(sys.stdin.readline())
        if case_num == 0:
            sys.stdout.write("1 0\n")
            continue
        elif case_num == 1:
            sys.stdout.write("0 1\n")
            continue
        else:
            sys.stdout.write(f"{dynamic_fibonacci(case_num - 1)} {dynamic_fibonacci(case_num)}\n")


def divide_num_1463():
    case_num = int(sys.stdin.readline())
    dp_list = [0 for _ in range(case_num + 1)]
    for i in range(2, case_num + 1):
        dp_list[i] = dp_list[i - 1] + 1
        two_quotient = i // 2
        three_quotient = i // 3
        if i % 2 == 0 and dp_list[i] > dp_list[two_quotient] + 1:
            dp_list[i] = dp_list[two_quotient] + 1
        if i % 3 == 0 and dp_list[i] > dp_list[three_quotient] + 1:
            dp_list[i] = dp_list[three_quotient] + 1
    else:
        sys.stdout.write(f"{dp_list[case_num]}\n")


def add_num_9095():
    def sum_9095(num):
        if num == 1:
            return 1
        elif num == 2:
            return 2
        elif num == 3:
            return 4
        else:
            return sum_9095(num - 1) + sum_9095(num - 2) + sum_9095(num - 3)
    tot_idx = int(sys.stdin.readline())
    for idx in range(tot_idx):
        chk_num = int(sys.stdin.readline())
        sys.stdout.write(f"{sum_9095(chk_num)}\n")


def fibonacci_2747():
    def add_num(first_num, second_num):
        return first_num + second_num
    case_num = int(sys.stdin.readline())
    first = 1
    second = 1
    total = 0
    if case_num == 0:
        sys.stdout.write("0")
        return
    elif case_num == 1:
        sys.stdout.write("1")
        return
    elif case_num == 2:
        sys.stdout.write("1")
        return
    for idx in range(2, case_num):
        total = add_num(first, second)
        first = second
        second = total
    sys.stdout.write(f"{total}")


def fibonacci_10826():
    def add_num(num_1, num_2):
        return num_1 + num_2
    tot_num = int(sys.stdin.readline())
    add_num_1 = 1
    add_num_2 = 1
    ret_val = 0
    if tot_num == 0:
        sys.stdout.write("0")
        return
    elif tot_num == 1 or tot_num == 2:
        sys.stdout.write("1")
        return
    for idx in range(2, tot_num):
        ret_val = add_num(add_num_1, add_num_2)
        add_num_1 = add_num_2
        add_num_2 = ret_val
    sys.stdout.write(f"{ret_val}")


def fibonacci_4150():
    def add_num(first_num, second_num):
        return first_num + second_num
    case_num = int(sys.stdin.readline())
    first = 1
    second = 1
    total = 0
    if case_num == 0:
        sys.stdout.write("0")
        return
    elif case_num == 1:
        sys.stdout.write("1")
        return
    elif case_num == 2:
        sys.stdout.write("1")
        return
    for idx in range(2, case_num):
        total = add_num(first, second)
        first = second
        second = total
    sys.stdout.write(f"{total}")


if __name__ == "__main__":
    # print(recursive_fibonacci(4))
    # print(dynamic_fibonacci(5))
    # print(fibonacci_2748())
    # fibonacci_9625()
    # fibonacci_1003()
    # divide_num_1463()
    # add_num_9095()
    # fibonacci_2747()
    # fibonacci_10826()
    fibonacci_4150()
