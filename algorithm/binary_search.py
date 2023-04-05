import sys


def search_2110():
    input_arr = list(map(int, sys.stdin.readline().split()))
    case_arr = []
    for idx in range(input_arr[0]):
        case_arr.append(int(sys.stdin.readline()))
    case_arr.sort()

    start_num = 1
    end_num = case_arr[-1] - case_arr[0]
    ret_val = 0

    while True:
        mid_num = (start_num + end_num) // 2
        val = case_arr[0]
        cnt = 1
        for idx in range(1, len(case_arr)):
            if case_arr[idx] >= val + mid_num:
                val = case_arr[idx]
                cnt += 1
        if cnt >= input_arr[1]:
            start_num = mid_num + 1
            ret_val = mid_num
        else:
            end_num = mid_num - 1
        if start_num > end_num:
            break
    sys.stdout.write(f"{ret_val}")


if __name__ == "__main__":
    search_2110()