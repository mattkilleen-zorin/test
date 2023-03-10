#!/usr/bin/env python3
'''#
     pwd-gen.py

     A bit like the Google Chrome password generator.

     Inputs: None
     Returns: Random password in format XXXXXX-XXXXXX-XXXXXX
              where X can be upper or lower-case character or
              numeric value. 

              For example: 9LhR23-BLJRw2-6h1x3n
'''

import random

sPassword = ""
nSwitch = 0

alphaList = [chr(chNum) for chNum in list(range(ord('a'),ord('z')+1))]
numList = [chr(chNum) for chNum in list(range(ord('0'),ord('9')+1))]
randChars = alphaList + numList

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
