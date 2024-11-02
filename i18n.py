#!/usr/bin/env python3
# i18n.py
import time, math, random, sys, config, json, argparse

lang = config.getConfig("lang")
fallback_lang = 'en_us'
langkeys = {}

# load
langs = config.getConfig("languages")
success, failure = 0, 0
for i in langs:
    try:
        langfile = open(f"lang/{i}.json", "r", encoding='utf-8')
        lang_keys = json.load(langfile)
        langkeys[i] = lang_keys
    except FileNotFoundError as e:
        if i == fallback_lang:
            raise e
        print(f"语言 {i} 加载错误 (找不到文件):",e,"跳过")
        failure += 1
        continue
    except PermissionError as e:
        if i == fallback_lang:
            raise e
        print(f"语言 {i} 加载错误 (权限不足):",e,"跳过")
        failure += 1
        continue
    except IOError as e:
        if i == fallback_lang:
            raise e
        print(f"语言 {i} 加载错误 (读取文件时发生错误):",e,"跳过")
        failure += 1
        continue
    except json.JSONDecodeError as e:
        if i == fallback_lang:
            raise e
        print(f"语言 {i} 加载错误 (JSON格式错误):",e,"跳过")
        failure += 1
        continue
    else:
        print(f"语言 {i} 加载完成")
        success += 1
print(len(langs),f"个语言加载完成! ({success} 个成功, {failure} 个失败)")

def getTranslation(key, values=(), selectedlang = ''):
    try:
        result = langkeys[selectedlang if selectedlang != '' else lang].get(key, langkeys[fallback_lang].get(key, key))
    except KeyError:
        result = langkeys[fallback_lang].get(key, key)
    finally:
        result = result % values
        return result