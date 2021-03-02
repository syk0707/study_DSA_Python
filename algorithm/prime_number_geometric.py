# check prime number
def check_prime_number(num):
    if num == 1:
        return False
    for idx in range(num - 1):
        divide_num = idx + 1
        if divide_num == 1:
            continue
        else:
            if num % divide_num == 0:
                return False
    return True

# Write a program that finds and prints how many of the given N are.
def find_prime_number():
    check_length = int(input())
    number_array = list(map(int, input().split()))
    prime_num = 0
    for num in number_array:
        is_prime_num = check_prime_number(num)
        if is_prime_num is True:
            prime_num += 1
    print(prime_num)

# When given natural numbers M and N, write a program to find the sum and minimum of these few numbers by selecting all the natural numbers above M and below N.
def find_prime_number_array():
    start_num = int(input())
    end_num = int(input()) + 1
    minimum_num = -1
    total_num = 0
    for idx in range(start_num, end_num):
        is_prime_num = check_prime_number(idx)
        if is_prime_num is True and minimum_num == -1: 
            minimum_num = idx
            total_num += idx
        elif is_prime_num is True:
            total_num += idx
    if minimum_num != -1:
        print(total_num)
    print(minimum_num)

if __name__ == "__main__":
    #find_prime_number()
    find_prime_number_array()