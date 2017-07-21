# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 22:22:12 2017

@author: AnthyG
"""

import sys, os, subprocess

myinput = open('myinput.in')
myoutput = open('myoutput.out', 'w')

p = subprocess.Popen([
    "python", "interface/interface.py", "-port 54123"
])#, stdin=myinput, stdout=myoutput)

p.wait()
print(p)
#myoutput.flush()