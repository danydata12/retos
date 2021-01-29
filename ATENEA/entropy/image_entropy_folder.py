#!/usr/bin/python
# file_entropy.py
#
# Shannon Entropy 
# FB - 201011291
import sys
import math
import os
import hashlib
 
# read the whole file into a byte array
def entropy(name):
    f = open(name, "rb")
    byteArr = map(ord, f.read())
    f.close()
    fileSize = len(byteArr)
 
    # calculate the frequency of each byte value in the file
    freqList = []
    for b in range(256):
        ctr = 0
        for byte in byteArr:
            if byte == b:
                ctr += 1
        freqList.append(float(ctr) / fileSize)
 
    # Shannon entropy
    ent = 0.0
    for freq in freqList:
        if freq > 0:
            ent = ent + freq * math.log(freq, 2)
    ent = -ent
    entropyList[name] = ent
 
 
entropyList = {}
for file in os.listdir("entropy"):
    entropy("entropy/"+file)
 
max_value = max(entropyList.values())
max_keys = [k for k, v in entropyList.items() if v == max_value]
maxEntr = max_keys[0].split('/')[1]
print ( maxEntr + " : " + str(max_value) )
print "flag{"+hashlib.md5(maxEntr).hexdigest()+"}"