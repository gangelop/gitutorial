#!/usr/bin/env python

import sys
import utils

args = sys.argv[1:]

if len(args) < 1:
    utils.usage()

utils.animalPrint(args)
