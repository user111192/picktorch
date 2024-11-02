#!/usr/bin/env python
# io.py
import time, math, random, sys, config, json, argparse, i18n, util

disableInputRepeat = True


def input_type(type, msg=''):
    while True:
        try:
            return type(input(msg))
        except ValueError as e:
            if not disableInputRepeat:
                print(i18n.getTranslation("gui.error.invalid_input"))
            else:
                e.add_note("Invalid input and input retrying is disabled. ")
                raise e


def ensure_number(num, minv=-math.inf, maxv=math.inf):
    return max(min(num, maxv), minv)


def number_in_range(num, minv=-math.inf, maxv=math.inf):
    return num >= minv and num <= maxv


def input_number(type=int, minv=-math.inf, maxv=math.inf, msg=''):
    return ensure_number(input_type(type, msg), minv, maxv)


def input_numbers(count, type=int, minv=-math.inf, maxv=math.inf, msg=''):
    exceptions = []
    res = []
    for i in range(1, count + 1):
        try:
            res += [input_number(type, minv, maxv, msg + " (" + str(i) + ") ")]
        except Exception as e:
            exceptions.append(e)
    if exceptions:
        raise ExceptionGroup("Multiple errors occurred when handling user input", exceptions)
    return res
