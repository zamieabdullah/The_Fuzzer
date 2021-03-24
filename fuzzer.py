# fuzzer.py
# Created by Zamie Abdullah
# Date of last edit: 03/24/2021
# 
# Program: 
# A fuzzing test script that identifies reflected Cross-Site Scripting (XSS) bugs.

import requests
import argparse

list = []


# Reads through a given fuzzing wordlist within the directory and appends 
# each line into a list.
def read_list(fuzz_list):
    try:
        with open(fuzz_list, 'r') as file:
            content = file.readlines()
        for line in content:
            line = line.strip('\n')
            list.append(line)
        
    except:
        print('Fuzz list not found within directory')

# Using a given target url, a payload from the fuzzing wordlist will be added 
# to the end of the url, checking to see if the payload is visible when it is
# being posted.
def fuzz(target):
    try:
        for payload in list:
            req = requests.post(target + payload)
            if payload in req.text:
                print(payload + ' has been identified in HTTP request\n')
            else:
                print(payload, ' NOT identified in HTTP request\n')
    except:
        print('HTTP request not available')
    

parser = argparse.ArgumentParser(description='A fuzzer program that identifies Cross-Site Scripting bugs')
parser.add_argument('-u', dest='url', help='link that will be fuzzed by the program', default = '')
parser.add_argument('-r', dest='fuzzlist', help='a fuzzing wordlist that will be injected into the link', default = '')
args = parser.parse_args()

if args.url == '':
    target = input('Target Link: ') # Asks for user to input a target link when not in argument
else:
    target = args.url
    print('Target Link:', target)
    
if args.fuzzlist == '':
    word_list = input('Input fuzz: ') # Asks for user to input a target link when not in argument
    list.append(word_list)
else:
    read_list(args.fuzzlist)
    
fuzz(target)