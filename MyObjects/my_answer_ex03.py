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
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if re.match(r'##.*', line):
                print(line)  ## output line


pattern = re.compile(r'##.*')
matched = []
with open(file, "r", encoding="utf-8") as f:
    for line in f:
        m = pattern.match(line.strip())
        if m:
            matched.append(m.group(0))

test_data = open(tg_file, "r", encoding='utf-8')                     
lines = test_data.readlines()
lines[0].strip()
m = pattern.match(lines[2].strip())
m.group(0)
m.group(1)
m.groups()

file_path = os.path.join(os.path.dirname(__file__), "README.md")
os.path.dirname(tg_file)


if __name__ == "__main__":
    file = 'README.md'
    dir_md = 'learning/python_exercises/MyObjects/exercises/'
    dir_md_test = 'exercises/'
    tg_file = dir_md_test + file
    find_pattern(tg_file)
    