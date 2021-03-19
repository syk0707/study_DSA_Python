import sys
import collections

def array_num():
    total_num = int(input())
    total_obj = {}
    total_arr = []
    for idx in range(total_num):
        num = int(input())
        if total_obj.get(num) is None:
            total_obj[num] = 1
            total_arr.append(num)
    total_arr.sort()
    for print_num in total_arr:
        print(print_num)

def array_num_2():
    total_num = int(sys.stdin.readline())
    total_deque = deque()
    for total_idx in range(total_num):
        num = int(sys.stdin.readline())
        total_arr.append(num)
    nl = "\n"
    while total_deque:
        sys.stdout.write(f"{total_arr[reverse_idx]}{nl}")

if __name__ == "__main__":
    #array_num()
    #array_num_2()
    print(chr(74))
    print(ord("C"))