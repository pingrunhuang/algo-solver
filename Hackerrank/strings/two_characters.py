#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
# 
# Given a string, remove characters until the string is made up of any two alternating characters. 
# When you choose a character to remove, all instances of that character must be removed. 
# Determine the longest string possible that contains just two alternating letters.

def alternate(s):
    # Write your code here
    distinct_chars = set(s)
    prev_char = None
    longest_length = 0
    
    for combo in combinations(distinct_chars, 2):
        temp_length = 0
        is_consecutive = False
        # print(combo)
        for char in s:
            if char in combo and prev_char is None:
                prev_char = char
                temp_length+=1
                is_consecutive=True
            elif char in combo and prev_char!=char:
                temp_length+=1
                prev_char = char
                is_consecutive = True
                # print(char)
            elif char in combo and prev_char==char:
                is_consecutive = False
                continue
        if is_consecutive:
            longest_length=temp_length if temp_length>longest_length else longest_length
    return longest_length


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # l = int(input().strip())

    # s = input()

    # result = alternate(s)

    # fptr.write(str(result) + '\n')

    # fptr.close()
    result = alternate("beabeefeab")
    print(result)