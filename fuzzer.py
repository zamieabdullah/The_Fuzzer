# fuzzer.py
# Created by Zamie Abdullah

import requests
import argparse

list = []

def fuzz(target):
    try:
        for payload in list:
            req = requests.post(target + payload)
            if payload in req.text:
                print(payload, ' has been identified in HTTP request')
            else:
                print(payload, ' not identified in HTTP request')
    except:
        print('HTTP request not available')
    

parser = argparse.ArgumentParser(description='A fuzzer program that identifies Cross-Site Scripting bugs')
parser.add_argument('-u', dest='url', help='Link that will be fuzzed by the program', default = '')
parser.add_argument('-r', dest='fuzzlist', help='A fuzzing wordlist that will be injected into the link', default = '')
args = parser.parse_args()

if args.url == '':
    target = input('Target Link: ')
else:
    target = args.url
    print('Target Link:', target)
    
if args.fuzzlist == '':
    word_list = input('Input fuzz: ')
    list.append(word_list)
else:
    pass
    
fuzz(target)