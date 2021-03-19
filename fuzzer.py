# fuzzer.py
# Created by Zamie Abdullah

import argparse

parser = argparse.ArgumentParser(description='A fuzzer program that identifies Cross-Site Scripting bugs')
parser.add_argument('-u', dest='url', help='Link that will be fuzzed by the program')
parser.add_argument('-r', dest='fuzzlist', help='A fuzzing wordlist that will be injected into the link')
args = parser.parse_args()

