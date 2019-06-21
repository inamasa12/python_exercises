# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 23:16:02 2019

@author: mas

%bookmark ri3 /Users/mas/learning/python_exercises/MyObjects
%cd ri3


"""
import os
import re

#正規表現
# .: 任意の一文字
# *: ０回以上の繰り返し

def find_pattern(file):

    pattern = re.compile(r'##.*')
    matched = []

    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            m = pattern.match(line.strip())
            if m:
                matched.append(m.group(0))
    print(matched)


if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__) + 'exercises', "README.md")
    find_pattern(file_path)
    