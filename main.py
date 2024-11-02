#!/usr/bin/env python3
# main.py
import time, math, random, sys, config, json, argparse,i18n, game, traceback

try:
    game.run()
except Exception as e:
    print("Game crashed!")
    e.add_note("game crashed!")
    traceback.print_exception(e)
    sys.exit(1)