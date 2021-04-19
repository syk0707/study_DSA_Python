import sys


def black_jack_2798():
    cnt_list = list(map(int, sys.stdin.readline().split()))
    card_list = list(map(int, sys.stdin.readline().split()))
    card_list.sort()
    max_num = card_list[0] + card_list[1] + card_list[2]
    for num in range(len(card_list) - 2):
        for num_2 in range(num, len(card_list) - 1):
            for num_3 in range(num_2, len(card_list)):
                if num == num_2 or num == num_3 or num_2 == num_3:
                    continue
                cal_num = card_list[num] + card_list[num_2] + card_list[num_3]
                if max_num < cal_num <= cnt_list[1]:
                    max_num = cal_num
    sys.stdout.write(f"{max_num}\n")


if __name__ == "__main__":
    black_jack_2798()