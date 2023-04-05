import sys


def get_key(data):
    test = sys.stdin.readline()
    return hash(data)


def hash_function(key):
    return key % 8


def save_data(data, value):
    hash_address = hash_function(get_key(data))
    hash_table[hash_address] = value


def read_data(data):
    hash_address = hash_function(get_key(data))
    return hash_table[hash_address]


def test():
    save_data('Kim', '00000000')
    save_data('Lee', '10000000')
    print(read_data('Kim'))
    hash_t = list([0 for i in range(8)])


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


def network_4195():
    def find_network(x, case):
        if x == case[x]:
            return x
        else:
            p = find_network(case[x], case)
            case[x] = p
            return case[x]

    def union_network(x, y, case, num):
        x = find_network(x, case)
        y = find_network(y, case)
        if x != y:
            case[y] = x
            num[x] += num[y]
    tot_idx = int(sys.stdin.readline())
    for idx in range(tot_idx):
        case_idx = int(sys.stdin.readline())
        case_dic = {}
        num_dic = {}
        for each_idx in range(case_idx):
            friends = list(map(str, sys.stdin.readline().split()))
            if friends[0] not in case_dic:
                case_dic[friends[0]] = friends[0]
                num_dic[friends[0]] = 1
            if friends[1] not in case_dic:
                case_dic[friends[1]] = friends[1]
                num_dic[friends[1]] = 1
            union_network(friends[0], friends[1], case_dic, num_dic)
            sys.stdout.write(f"{num_dic[find_network(friends[0], case_dic)]}\n")


def top_1302():
    tot_idx = int(sys.stdin.readline())
    tot_dic = {}
    max_val = 0
    for idx in range(tot_idx):
        each_input = sys.stdin.readline().rstrip()
        if tot_dic.get(each_input) is None:
            tot_dic[each_input] = 1
        else:
            tot_dic[each_input] += 1
            if max_val < tot_dic[each_input]:
                max_val = tot_dic[each_input]
    ret_arr = []
    for key, value in tot_dic.items():
        if value == max_val:
            ret_arr.append(key)
    ret_arr.sort()
    sys.stdout.write(f"{ret_arr[0]}")


if __name__ == "__main__":
    # print(hash('Dave') % 8)
    # print(hash('Dd') % 8)
    # print(hash('Data') % 8)
    # save_data('Dd', '1201023010')
    # save_data('Data', '3301023010')
    # read_data('Dd')
    # find_str_17219()
    # network_4195()
    top_1302()
