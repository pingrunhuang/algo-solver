#!/bin/zsh

echo $#
if [ $# -ne 1 ]; then
    echo "please enter the number of the challenge" >&2
    exit 1
fi

echo "if __name__ == \"__main__\":" > ./$1.py
echo "    solution = Solution()" >> ./$1.py
