#!/usr/bin/python


import sys
import os
import random


f = open ("unsortedlist","w")
for i in range(int(sys.argv[1])):
	f.write("%d\n"%random.randint(0,1<<16))
f.close()



