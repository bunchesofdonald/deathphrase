#!/usr/bin/env python

import sys
import string
import hashlib
import smtplib
from Crypto.Random import random

if len(sys.argv) < 2:
    print "USAGE: deathphrase.py EMAIL_ADDRESS"
    exit()
else:
    EMAIL_ADDRESS = sys.argv[1]

WORD_LENGTH = (4, 5) # min, max
PHRASE_LENGTH = 5
GMAIL_USER = ''
GMAIL_PASSWORD = ''

def dictionary(dict_file='dictionary.txt'):
    '''
    Read words from dict_file
    dict_file format is simply one word per line.
    '''
    return open(dict_file).read().split('\n')

def get_words_of_length(length):
    correct_length = lambda word: len(word) >= length[0] and len(word) <= length[1]
    return filter(correct_length, dictionary()) 

def build_phrase(words, length):
    phrase = []
    for i in xrange(length):
        word_i = random.randint(0, len(words))
        phrase.append(words[word_i])

    return " ".join(phrase)

def rot13(phrase):
    rot13_trans = string.maketrans("ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz","NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
    return string.translate(phrase, rot13_trans)

def email_phrase(to, phrase):
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(GMAIL_USER, GMAIL_PASSWORD)
    header = 'To:' + to + '\n' + 'From: ' + GMAIL_USER + '\n' + 'Subject:Death Phrase\n'
    msg = header + '\n%s\n\n' % phrase
    smtpserver.sendmail(GMAIL_USER, to, msg)
    smtpserver.close()

# Generate phrase
words = get_words_of_length(WORD_LENGTH)
phrase = build_phrase(words, PHRASE_LENGTH)

# Write encrypted versions to file
oneway_enc_type = 'SHA256'
oneway_enc_phrase = hashlib.sha256(phrase).hexdigest()
rot13_phrase = rot13(phrase)
open('one_way_phrase.txt', 'w').write('%s:%s' % (oneway_enc_type, oneway_enc_phrase))
open('rot13_phrase.txt', 'w').write('%s' % rot13_phrase)

# Email unencrypted phrase
email_phrase(EMAIL_ADDRESS, phrase)
