#!/usr/bin/env python3
# util.py
import time, math, random, sys, tqdm

def workl(list: list, func, **kwargs):
    """
    Work on all elements of a list with a function.

    :param list : list to work on
    :param func : function to apply
    """
    exceptions = []
    for i in list:
        try:
            func(i, **kwargs)
        except Exception as e:
            e.add_note("This exception occurred when working on "+str(i))
            exceptions.append(e)
    if exceptions:
        raise ExceptionGroup("Multiple errors occurred (input:"+str(list)+")", exceptions)


def workr(cnt, func, *wargs, **kwargs):
    exceptions = []
    res = []
    for i in range(1,cnt+1):
        try:
            res += func(*wargs,**kwargs)
        except* Exception as e:
            e.add_note(f"Index: {i}/{cnt}")
            exceptions.append(e)

    if exceptions:
        raise ExceptionGroup("Multiple errors occurred", exceptions)
    return res

def to_int(var):
    if type(var) == list:
        return workl(var.copy(), to_int)
    return int(var)

def ati(list):
    return workl(list, to_int)

def print_sep(char='=', count=20):
    print(char * count)

if __name__ == "__main__":
    # unit test
    base1 = [1,2]
    base2 = ["aaa", "abc"]

    ati(base1+base2+[base1+base2])