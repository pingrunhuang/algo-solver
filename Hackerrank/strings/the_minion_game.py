"""
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.
"""
def minion_game(string):
    # your code goes here
    vowels = ["A", "E", "I", "O", "U"]
    stuart_score = 0
    kevin_score = 0
    for i, c in enumerate(string):
        if c in vowels:
            kevin_score += len(string)-i
        else:
            stuart_score += len(string)-i

    if stuart_score>kevin_score:
        print(f"Stuart {stuart_score}")
    elif stuart_score<kevin_score:
        print(f"Kevin {kevin_score}")
    else:
        print("Draw")

if __name__ == '__main__':
    s = "BAANANAS"
    minion_game(s)
    s = "ANANAS"
    minion_game(s)
    s = "BANANA"
    minion_game(s)
