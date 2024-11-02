import time, math, random, json, sys

# config.py


config = {}
defaultconfig = {"languages": ["zh_cn", "en_us"], "lang": "zh_cn"}

try:
    configfile = open("config.json", "r", encoding='utf-8')
except FileNotFoundError:
    print("找不到 config.json! 开启创建流程! ")
    configfile = open("config.json", "w+", encoding='utf-8')
    json.dump(defaultconfig, configfile, ensure_ascii=False, indent=4)
    configfile.close()
finally:
    configfile = open("config.json", "r", encoding='utf-8')
    config = json.load(configfile)
    configfile.close()

# print("Config:", config)


def setConfig(path, value):
    config[path] = value
    configfile = open("config.json", "w+", encoding='utf-8')
    json.dump(config, configfile, ensure_ascii=False, indent=4)
    configfile.close()

def getConfig(path):
    return config[path]
