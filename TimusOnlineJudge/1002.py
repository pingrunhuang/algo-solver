from sys import stdin

lookup_table = {
    'i': 1,
    'j': 1,
    'a': 2,
    'b': 2,
    'c': 2,
    'd': 3,
    'e': 3,
    'f': 3,
    'g': 4,
    'h': 4,
    'k': 5,
    'l': 5,
    'm': 6,
    'n': 6,
    'p': 7,
    'r': 7,
    's': 7,
    't': 8,
    'u': 8,
    'v': 8,
    'w': 9,
    'x': 9,
    'y': 9,
    'o': 0,
    'q': 0,
    'z': 0
}


def str_to_num(input_str):
    result = ''
    for e in input_str:
        result += str(lookup_table[e])
    return result

def solve(mobile_phone, list_of_word):
    list_of_word.sort(key=lambda x: -len(x))
    list_of_sorted_wordnum = [str_to_num(x) for x in list_of_word]
    list_of_sorted_wordnum.sort(key=lambda x: -len(x))
    index_in_phone = 0
    result = ''
    mobile_length = len(mobile_phone)
    for index, wordnum in enumerate(list_of_sorted_wordnum):
        if mobile_length < len(wordnum):
            continue
        for num in wordnum:
            if mobile_phone[index_in_phone] != num:
                index_in_phone = 0
                break
            index_in_phone += 1
        result += list_of_word[index] + ' '
    if index_in_phone == (mobile_length - 1):
        return result
    else:
        return 'No solution.'

mobile_phone=input()
while mobile_phone != '-1':
    num_of_words = input()
    available_words = []
    for _ in range(int(num_of_words)):
        available_words.append(input())
    # sort the list of string first by the length of each string, then alphabetic
    # available_words.sort(key=lambda x: (-len(x),x))
    print(solve(mobile_phone, available_words))
    mobile_phone = input()
