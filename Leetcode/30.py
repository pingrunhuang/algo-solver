from typing import List

"""
You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated substring in s is a substring that contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated substring because it is not the concatenation of any permutation of words.
Return the starting indices of all the concatenated substrings in s. You can return the answer in any order.

idea:
checking from listing all the permutations and then check with the string one char by one char
will run out of time
better idea is starting from the string, check if occurance after wlen*wwords char match exactly the number of the occurance in words
"""

class Solution_one:
    # run out of time limit
    def findPermutations(self, result:set[str], words:List[str], permutation:List[int]):
        if len(words) == len(permutation):
            result.add("".join(words[i] for i in permutation)) # using index to avoid duplication
            return
        else:
            
            for i in range(len(words)):
                if i in permutation:
                    continue
                permutation.append(i)
                self.findPermutations(result, words, permutation)
                permutation.pop()

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_length = len(words[0])
        words_num = len(words)
        str_length = len(s)
        if str_length < word_length*words_num:
            return []
        permutations = set()
        self.findPermutations(permutations, words, [])
        
        result = []
        for i in range(0, str_length-word_length*words_num+1, word_length):
            perm = s[i:i+word_length*words_num]
            if perm in permutations:
                result.append(i)
        return result

from collections import Counter
class Solution:
    # openai provided
    def findSubstring(self, s:str, words:List[str]) -> List[int]:
        word_length = len(words[0])
        words_num = len(words)
        permutation_length = word_length*words_num
        str_length = len(s)
        words_counter = Counter(words)
        result = []
        for i in range(str_length-word_length+1):
            seen = Counter()
            j = 0
            while j < permutation_length:
                word = s[i+j:i+j+word_length]
                if word in words_counter:
                    seen[word] += 1
                    if seen[word] > words_counter[word]:
                        break
                else:
                    break
                j+=word_length
            if seen==words_counter:
                result.append(i)
        return result
            

if __name__ == "__main__":
    sol = Solution()
    args = ["barfoothefoobarman", ["foo","bar"]]
    assert sol.findSubstring(*args)==[0, 9]
    args = ["wordgoodgoodgoodbestword", ["word","good","best","word"]]
    assert sol.findSubstring(*args)==[]
    args =["barfoofoobarthefoobarman", ["bar","foo","the"]]
    assert sol.findSubstring(*args)==[6,9,12]
    args = ["wordgoodgoodgoodbestword", ["word","good","best","good"]]
    assert sol.findSubstring(*args)==[8]
    args = ["lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"]]
    assert sol.findSubstring(*args)==[13]
    from collections import Counter