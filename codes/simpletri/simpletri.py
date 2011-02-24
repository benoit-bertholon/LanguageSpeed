#!/usr/bin/python

import sys


def tri ( l):
	for i in range(len(l)):
		c = 0
		for j in range(i+1,len(l)):
			if l[i]> l[j]:
				(l[i], l[j])=(l[j], l[i])
				c =1
		if not c :
			return


f = open(sys.argv[1])
unsortedlist = []

for l in f.readlines():
	if len(l)>0:
		unsortedlist.append (int(l))

tri(unsortedlist)

f = open(sys.argv[2],"w")
for i in unsortedlist:
	f.write("%d\n"%i)
