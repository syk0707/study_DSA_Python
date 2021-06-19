import sys

hash_table = list([0 for i in range(8)])


def get_key(data):
    return hash(data)


def hash_function(key):
    return key % 8


def save_data(data, value):
    hash_address = hash_function(get_key(data))
    hash_table[hash_address] = value


def read_data(data):
    hash_address = hash_function(get_key(data))
    return hash_table[hash_address]


save_data('Kim', '00000000')
save_data('Lee', '10000000')
print(read_data('Kim'))

# Hash Collision Algorithm
hash_table = list([0 for i in range(8)])


def get_key(data):
    return hash(data)


def hash_function(key):
    return key % 8


def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                hash_table[hash_address][index][1] = value
                return
        hash_table[hash_address].append([index_key, value])
    else:
        hash_table[hash_address] = [[index_key, value]]


def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)

    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                return hash_table[hash_address][index][1]
        return None
    else:
        return None


def find_str_17219():
    case_arr = list(map(int, sys.stdin.readline().split()))
    pass_dict = {}
    for idx in range(case_arr[0]):
        each_pass = sys.stdin.readline().split()
        pass_dict[each_pass[0]] = each_pass[1]
    for print_idx in range(case_arr[1]):
        each_key = sys.stdin.readline().rstrip()
        sys.stdout.write(f"{pass_dict[each_key]}\n")


if __name__ == "__main__":
    # print(hash('Dave') % 8)
    # print(hash('Dd') % 8)
    # print(hash('Data') % 8)
    # save_data('Dd', '1201023010')
    # save_data('Data', '3301023010')
    # read_data('Dd')
    find_str_17219()
