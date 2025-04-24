# python builtin implementation
from itertools import permutations, combinations


def generate_permutations(lst:list):
    if len(lst)==0:
        return [[]]
    permutations = []
    for i in range(len(lst)):
        lst[0], lst[i] = lst[i], lst[0]
        partial_permutations = generate_permutations(lst[1:])
        lst[0], lst[i] = lst[i], lst[0]
        for permutation in partial_permutations:
            permutations.append([lst[i]]+permutation)
    return permutations 


def generate_increasing_permutations(lst:list):
    if len(lst)==0:
        return [[]]
    for i in range(len(lst)):
        copy_list = lst.copy()
        cur_value = copy_list.pop(i)
        copy_list.insert(0, cur_value)
        partial_permutations = generate_permutations(lst[1:])

        for permutation in partial_permutations:
            permutations.append([lst[i]]+permutation)
    return permutations


def generate_combinations(lst:list, n:int):
    if n==1:
        for x in lst:
            yield [x]
    elif n==len(lst):
        yield lst
    else:
        for idx, val in enumerate(lst):
            sub_combos = generate_combinations(lst[idx+1:], n-1)
            for sub_combo in sub_combos:
                combo = [val] + sub_combo
                yield combo


def pprint(lst):
    for entry in lst:
        print(entry)


if __name__== "__main__":
    n = 4
    pprint(generate_permutations(list(range(n))))
    k = 3
    pprint(generate_combinations(list(range(n)), k))
