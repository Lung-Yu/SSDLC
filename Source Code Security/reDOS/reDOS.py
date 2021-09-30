#!/usr/bin/env python
# coding: utf-8

import re
import time
def reDOS(target_str):
    s1 = time.time()
    
    regex = re.compile('^(a+)+$')
    regex.match(target_str)
    
    s2 = time.time()
    return (s2-s1)

if __name__ == '__main__':


    for i in range(1,32):
        evil_str = "a"*i+"!"
        calcTime = reDOS(evil_str)
        print(i,evil_str,"Consuming time: %.2f s" % (calcTime))