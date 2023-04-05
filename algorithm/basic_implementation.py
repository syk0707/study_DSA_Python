import sys


def compare_10817():
    num_arr = list(map(int, sys.stdin.readline().split()))
    num_arr.sort()
    sys.stdout.write(f"{num_arr[1]}")


def input_1076():
    def get_color_add_num(color_str):
        if color_str == "black":
            return 0
        elif color_str == "brown":
            return 1
        elif color_str == "red":
            return 2
        elif color_str == "orange":
            return 3
        elif color_str == "yellow":
            return 4
        elif color_str == "green":
            return 5
        elif color_str == "blue":
            return 6
        elif color_str == "violet":
            return 7
        elif color_str == "grey":
            return 8
        elif color_str == "white":
            return 9
    ret_val = 0
    for idx in range(3):
        color_input = sys.stdin.readline().rstrip()
        num = get_color_add_num(color_input)
        if idx < 2:
            ret_val = f"{ret_val}{num}"
        else:
            ret_val = int(ret_val) * (10 ** num)
            sys.stdout.write(f"{ret_val}")


if __name__ == "__main__":
    # compare_10817()
    input_1076()
