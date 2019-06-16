# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 23:07:47 2019

@author: mas

%bookmark ri3 /Users/mas/learning/python_exercises/MyObjects
%cd ri3

"""

"""
def collect():
    names = ("Bill", "Anne", "Angy", "Cony", "Daniel", "Occhan")
    for i, name in enumerate(names):
        if name == "Angy":
            print("{0}.My name is {1}".format(i, name))
        else:
            print("{0}.{1} is my classmate".format(i, name))
"""

def print_sentence(i, name):
    print("{0}.My name is {1}".format(i, name)) if name == "Angy" else print("{0}.{1} is my classmate".format(i, name))
    
def loop_names(names):
    for i, name in enumerate(names):
        print_sentence(1, name)

if __name__ == "__main__":
    #collect()
    names = ("Bill", "Anne", "Angy", "Cony", "Daniel", "Occhan")
    loop_names(names)
    