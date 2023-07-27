#!/usr/bin/env python

import sys

args = sys.argv[1:]

if len(args) < 1:
    print("Please give some arguments")

for i in args:
    print("=>", i)
