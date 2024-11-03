#!/usr/bin/env python3
# game.py
import time, math, random, sys, config, json, argparse, i18n, traceback, util, tqdm, utils.io

_ = i18n.getTranslation

total = 0
max_choose = 0
def run():
    global total,max_choose
    util.print_sep()
    print(_("meta.game_name"))
    util.print_sep()
    for __ in tqdm.trange(100,file=sys.stdout):
        time.sleep(0.01)
    total = utils.io.input_number(int, 1, math.inf, _("gui.prompt.input_total_count"))
    aaa = util.workr(5, utils.io.input_numbers, 5, int, 1, 10, _("gui.prompt.input_total_count"))
    print(aaa)