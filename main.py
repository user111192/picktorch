#!/usr/bin/env python3
# main.py
import time, math, random, sys, config, json, argparse,i18n, game, traceback
from rich.console import Console
console = Console()

try:
    game.run()
except Exception as e:
    print("Game crashed!")
    e.add_note("game crashed!")
    console.print_exception(extra_lines=5, show_locals=True, word_wrap=True)
    traceback.print_exception(e)
    sys.exit(1)