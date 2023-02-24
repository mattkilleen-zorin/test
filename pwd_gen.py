#!/bin/python3
#
#     pwd-gen.py
#
#     A bit like the Google Chrome password generator.
#

import random

sPassword = ""
nSwitch = 0

randChars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
             "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

for n in range(0,20):
    if n == 6 or n == 13:
        sPassword += "-"
    else:
        nSwitch = random.randint(0,1)
        if nSwitch == 0:
            sPassword += random.choice(randChars)
        else:
            sPassword += random.choice(randChars).upper()
    
print(sPassword)
