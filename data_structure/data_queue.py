import collections
import numpy
import sys
import heapq


def queue_10845():
    tot_idx = int(sys.stdin.readline())
    queue_arr = []
    for idx in range(tot_idx):
        case_str = sys.stdin.readline().split()
        category_str = case_str[0]
        if category_str == "push":
            queue_arr.append(case_str[1])
        elif category_str == "pop" and len(queue_arr) > 0:
            sys.stdout.write(f"{queue_arr.pop(0)}\n")
        elif category_str == "pop" and len(queue_arr) == 0:
            sys.stdout.write(f"{-1}\n")
        elif category_str == "size":
            sys.stdout.write(f"{len(queue_arr)}\n")
        elif category_str == "empty" and len(queue_arr) > 0:
            sys.stdout.write(f"{0}\n")
        elif category_str == "empty" and len(queue_arr) == 0:
            sys.stdout.write(f"{1}\n")
        elif category_str == "front" and len(queue_arr) > 0:
            sys.stdout.write(f"{queue_arr[0]}\n")
        elif category_str == "front" and len(queue_arr) == 0:
            sys.stdout.write(f"{-1}\n")
        elif category_str == "back" and len(queue_arr) > 0:
            sys.stdout.write(f"{queue_arr[len(queue_arr) - 1]}\n")
        elif category_str == "back" and len(queue_arr) == 0:
            sys.stdout.write(f"{-1}\n")


def dequeue_10866():
    tot_idx = int(sys.stdin.readline())
    dequeue_arr = collections.deque()
    for idx in range(tot_idx):
        case_str = sys.stdin.readline().split()
        category_str = case_str[0]
        if category_str == "push_front":
            dequeue_arr.appendleft(case_str[1])
        elif category_str == "push_back":
            dequeue_arr.append(case_str[1])
        elif category_str == "pop_front" and len(dequeue_arr) > 0:
            sys.stdout.write(f"{dequeue_arr.popleft()}\n")
        elif category_str == "pop_back" and len(dequeue_arr) > 0:
            sys.stdout.write(f"{dequeue_arr.pop()}\n")
        elif (category_str == "pop_front" or category_str == "pop_back") and len(dequeue_arr) == 0:
            sys.stdout.write(f"{-1}\n")
        elif category_str == "size":
            sys.stdout.write(f"{len(dequeue_arr)}\n")
        elif category_str == "empty" and len(dequeue_arr) > 0:
            sys.stdout.write(f"{0}\n")
        elif category_str == "empty" and len(dequeue_arr) == 0:
            sys.stdout.write(f"{1}\n")
        elif category_str == "front" and len(dequeue_arr) > 0:
            sys.stdout.write(f"{dequeue_arr[0]}\n")
        elif category_str == "front" and len(dequeue_arr) == 0:
            sys.stdout.write(f"{-1}\n")
        elif category_str == "back" and len(dequeue_arr) > 0:
            sys.stdout.write(f"{dequeue_arr[len(dequeue_arr) - 1]}\n")
        elif category_str == "back" and len(dequeue_arr) == 0:
            sys.stdout.write(f"{-1}\n")


def heap_11279():
    tot_idx = int(sys.stdin.readline())
    heap_dic = {}
    heap_arr = []
    max_num = 0
    for idx in range(tot_idx):
        num = int(sys.stdin.readline())
        if num != 0 and heap_dic.get(num) is None:
            heap_dic[num] = 1
            heapq.heappush(heap_arr, num * -1)
            max_num = heap_arr[0] * -1
        elif num != 0 and heap_dic.get(num) is not None:
            heap_dic[num] += 1
        elif len(heap_dic) == 0:
            sys.stdout.write(f"0\n")
        else:
            heap_dic[max_num] -= 1
            sys.stdout.write(f"{max_num}\n")
            if heap_dic[max_num] == 0:
                heap_dic.pop(max_num, None)
                heapq.heappop(heap_arr)
                if len(heap_arr) > 0:
                    max_num = heap_arr[0] * -1
                else:
                    max_num = 0


def queue_16466():
    tot_num = int(sys.stdin.readline())
    tot_arr = [i + 1 for i in range(tot_num + 1)]
    tot_dic = {key: 1 for key in tot_arr}
    case_arr = list(map(int, sys.stdin.readline().split()))
    for case_num in case_arr:
        if tot_dic.get(case_num):
            tot_dic.pop(case_num)
    sys.stdout.write(f"{next(iter(tot_dic))}")


if __name__ == "__main__":
    # queue_10845()
    # dequeue_10866()
    # heap_11279()
    queue_16466()