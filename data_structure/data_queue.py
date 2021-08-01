import collections
import sys


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


if __name__ == "__main__":
    #queue_10845()
    dequeue_10866()
