

def from_bit_string_to_num(bit_str):
    result = 0
    for idex, bit in enumerate(reversed(bit_str)):
        if bit=='1':
            result += 2 ** idex
    return result


def from_num_to_bit_string(num):
    return bin(num)

if __name__ == '__main__':
    test_case1='10010011011101'
    binary = from_bit_string_to_num(test_case1)
    s=from_num_to_bit_string(binary)
    print(binary)
    print(s)