#!/usr/bin/env python

import sys
import hashlib

phrase_file = 'one_way_phrase.txt'
phrase = open(phrase_file).read().split(':')[1]

print "What is the phrase?"
check_phrase = raw_input()

print hashlib.sha256(check_phrase).hexdigest() == phrase
