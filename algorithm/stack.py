import sys


def get_stack():
    total_command = int(sys.stdin.readline())
    stack_list = []
    command_list = list(sys.stdin.readline().split() for i in range(total_command))
    for each_command_list in command_list:
        command = each_command_list[0]
        if command == "push":
            num = each_command_list[1]
            stack_list.append(num)
        elif command == "pop":
            if stack_list:
                print(stack_list.pop())
            else:
                print(-1)
        elif command == "size":
            print(len(stack_list))
        elif command == "empty":
            if stack_list:
                print(0)
            else:
                print(1)
        elif command == "top":
            if stack_list:
                print(stack_list[len(stack_list) - 1])
            else:
                print(-1)


def stack_important_1966():
    total_case_idx = int(sys.stdin.readline())
    for idx in range(total_case_idx):
        case_arr = list(map(int, sys.stdin.readline().split()))
        important_arr = list(map(int, sys.stdin.readline().split()))
        print(case_arr)
        print(important_arr)


def get_last_stop_14645():
    total_arr = list(map(int, sys.stdin.readline().split()))
    for idx in range(total_arr[0]):
        each_arr = list(map(int, sys.stdin.readline().split()))
    sys.stdout.write('비와이\n')


def check_possible_stack_1874():
    total_num = int(sys.stdin.readline())
    count = 1
    ret_arr = []
    stack_arr = []
    for idx in range(total_num):
        input_num = int(sys.stdin.readline())
        while count <= input_num:
            stack_arr.append(count)
            count += 1
            ret_arr.append('+')
        if stack_arr[-1] == input_num:
            stack_arr.pop()
            ret_arr.append('-')
        else:
            sys.stdout.write('NO')
            return
    sys.stdout.write('\n'.join(ret_arr))


def check_stack_10773():
    tot_num = int(sys.stdin.readline())
    stack_arr = []
    for idx in range(tot_num):
        case_num = int(sys.stdin.readline())
        if case_num == 0 and len(stack_arr) > 0:
            stack_arr.pop(len(stack_arr) - 1)
        elif case_num != 0:
            stack_arr.append(case_num)
    sys.stdout.write(f"{sum(stack_arr)}")


if __name__ == "__main__":
    # get_stack()
    # get_last_stop_14645()
    # stack_important_1966()
    # check_possible_stack_1874()
    check_stack_10773()
