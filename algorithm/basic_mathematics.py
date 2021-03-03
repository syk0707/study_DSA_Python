# It costs a fixed cost of A dollars, and it is said that producing a single product costs a total of B dollars, including material costs and labor costs. 
# If the price of the item is set at C dollars, find a break-even point.
def break_even_point():
    num_arr = list(map(int, input().split()))
    n = 0
    if num_arr[1] >= num_arr[2]:
        n = -1
    else:
        n = (num_arr[0] / (num_arr[2] - num_arr[1])) + 1
    print(int(n))

#1, 7, 19, 37... There are whiskers that increase in order. Find out which order a particular number is placed in that sequence.
def check_num():
    num = int(input())
    sum = 1
    cnt = 0
    while sum <= num:
        sum += (6 * cnt)
        cnt += 1
        if sum == num:
            break
    print(cnt)

#1/1 -> 1/2 -> 2/1 -> 3/1 -> 2/2 -> … In the order of zigzags as shown in , number 1, 2, 3, 4, 5, … fraction.
#When given an X, write a program to find the X-th fraction.
def find_fractional_numbers():
    check_num = int(input())
    increase_num = 1
    total = 0
    count = 0
    while True:
        if check_num <= total:
            break        
        total += increase_num
        increase_num += 1
        count += 1
    last_num = total
    #1 - 분자 우선, 2 - 분모가 분자보다 큼, 3 - 분자가 분모보다 큼
    numerator = 0
    denominator = 0
    diff_num = last_num - check_num
    if(count % 2 == 0):
        #is_big_numerator = False
        numerator = increase_num - diff_num - 1
        denominator = 1 + diff_num
    else:
        numerator = 1 + diff_num
        denominator = increase_num - diff_num - 1
    #above python 3
    print('{numerator}/{denominator}'.format(numerator=numerator, denominator=denominator))
    #above python 3.6
    print(f'{numerator}/{denominator}')

if __name__ == "__main__":
    #break_even_point()
    #check_num()
    find_fractional_numbers()