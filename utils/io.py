#!/usr/bin/env python
# io.py
import time, math, random, sys, config, json, argparse, i18n, util


def input_type(type, msg):
    while True:
        try:
            return type(input(msg))
        except ValueError:
            print(i18n.getTranslation("gui.error.invalid_input"))


def ensure_number(num, minv=-math.inf,maxv=math.inf):
    return max(min(num, maxv), minv)

def number_in_range(num, minv=-math.inf,maxv=math.inf):
    return num >= minv and num <= maxv

def input_number(type=int, minv=-math.inf,maxv=math.inf, msg=''):
    return ensure_number(input_type(type, msg), minv, maxv)