#!/usr/bin/python
import sys

d={}
for line in sys.stdin:
	line=line.strip()	
	word,word1=line.split("\t")
	word1=word1.split()	
	d[word]=word1	
	for nodes in word1:
		print "%s,%s" % (word, nodes)
		print "%s,%s" % (nodes, word)
