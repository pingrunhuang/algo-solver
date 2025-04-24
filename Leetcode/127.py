"""
127. Word Ladder

Given two words (beginWord and endWord), and a dictionary's word list, 
find the length of shortest transformation sequence from beginWord to endWord, such that:

1. Only one letter can be changed at a time.
2. Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:
1. Return 0 if there is no such transformation sequence.
2. All words have the same length.
3. All words contain only lowercase alphabetic characters.
4. You may assume no duplicates in the word list.
5. You may assume beginWord and endWord are non-empty and are not the same.

TODO
Graph theory:
bidirectional 
bfs
"""
import time
import functools
from collections import defaultdict

def timing(func):
    @functools.wraps(func)
    def run(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(time.time() - start)
        return result
    return run


class Solution(object):
    """
    TODO: did not pass the final test case 
    """
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        # alphabetic matrix is used for look up for a character that could be changed to in different position
        alphabetic_matrix = []
        word_length = len(beginWord)
        # keep track on the current level of traversal

        queue = [(beginWord, 1)]
        
        visited_words = [beginWord]

        for i in range(word_length):
            alphabetic_matrix.append([])
            for word in wordList:
                alphabetic_matrix[i].append(word[i])

        while queue:
            beginWord, level = queue.pop(0)
            for i in range(word_length):
                for char in alphabetic_matrix[i]:
                    # replace the char at position i
                    next_word = beginWord[:i] + char + beginWord[i+1:]
                    if next_word == endWord:
                        return level+1
                    if next_word not in wordList:
                        continue
                    if next_word not in visited_words:
                        queue.append((next_word, level+1))
                        visited_words.append(next_word)
        return 0

class Solution1(object):
    @timing
    def ladderLength(self, beginWord, endWord, wordList):
        """
        The idea is to use bfs and hashmap
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        # alphabetic matrix is used for look up for a character that could be changed to in different position

        word_length = len(beginWord)
        # keep track on the current level of traversal

        queue = [(beginWord, 1)]
        # to prevent cycles 
        visited_words = set([beginWord])

        # preprocessing: how do I know the next word I will get by changing one char? Use a candidate word list
        fuzzy_candidate_words_map = defaultdict(list)
        for i in range(word_length):
            for word in wordList:
                fuzzy_candidate_words_map[word[:i]+"*"+word[i+1:]].append(word)

        while queue:
            current_word, level = queue.pop(0)
            for i in range(word_length):
                # fuzzy out one character
                fuzzy_word = current_word[:i] + "*" + current_word[i+1:]
                for next_word in fuzzy_candidate_words_map[fuzzy_word]:
                    if endWord == next_word:
                        return level+1
                    if next_word not in visited_words:
                        queue.append((next_word, level+1))
                        visited_words.add(next_word)
        return 0

class Solution2(object):
    """
    Bidirectional bfs single worker solution
    Problem: need to reinitialize the object again for each new test case
    """
    def __init__(self):
        self.length = 0
        self.fuzzy_candidate_words_map = defaultdict(list)
        # key is the visited words and value is the corresponding level
        self.wordList = []

    def _search_adjacent_word(self, queue, visited_words, opposite_visited_words):
        current_word, level = queue.pop(0)
        for i in range(self.length):
            fuzzy_word = current_word[:i] + "*" + current_word[i+1:]
            for next_word in self.fuzzy_candidate_words_map[fuzzy_word]:
                # if the next word is found in the opposite direction of visited words, means we found a path 
                if next_word in opposite_visited_words:
                    
                    return level + opposite_visited_words[next_word]
                # prevent the transformed word not in the available words
                if next_word not in visited_words and next_word in self.wordList:
                    visited_words[next_word] = level+1
                    queue.append((next_word, level+1))
        return None

    def ladderLength(self, beginWord, endWord, wordList):
        if len(beginWord)!=len(endWord) or endWord not in wordList:
            return 0
        begin2end_visited_words = {beginWord: 1}
        end2begin_visited_words = {endWord: 1}
        begin2end_queue = [(beginWord, 1)]
        end2begin_queue = [(endWord, 1)]
        self.length = len(beginWord)
        self.wordList = wordList
        # init fuzzy word mapping
        for i in range(self.length):
            for word in wordList:
                key = word[:i] + "*" + word[i+1:]
                self.fuzzy_candidate_words_map[key].append(word)
        while begin2end_queue and end2begin_queue:
            result = self._search_adjacent_word(begin2end_queue, begin2end_visited_words, end2begin_visited_words)
            if result:
                return result
            result = self._search_adjacent_word(end2begin_queue, end2begin_visited_words, begin2end_visited_words)
            if result:
                return result
        return 0

if __name__ == "__main__":
    s = Solution2()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    print(s.ladderLength(beginWord, endWord, wordList))

    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log"]
    print(s.ladderLength(beginWord, endWord, wordList))

    beginWord = "a"
    endWord = "c"
    wordList = ["a","b","c"]
    print(s.ladderLength(beginWord, endWord, wordList))

    beginWord = "hot"
    endWord = "dog"
    wordList = ["hot","dog"]
    print(s.ladderLength(beginWord, endWord, wordList))

    beginWord = "qa"
    endWord = "sq"
    wordList = ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]
    print(s.ladderLength(beginWord, endWord, wordList)) # 5
