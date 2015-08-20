#!/usr/bin/python
import sys

q=[]
x=0
a=1
flag=0
line=sys.stdin.readline()

line=line.strip()	
node1,node2=line.split(",")
q.append([node1,node2])
for line2 in sys.stdin:
	flag=0
	for x in range(0,a):
		line2 = line2.strip()
		n1,n2=line2.split(",")	
		if n1 in q[x] and n2 not in q[x]:
			q[x].extend([n2])
			flag=0
			break
		elif n1 not in q[x] and n2 in q[x]:
			q[x].extend([n1])
			flag=0
			break
		elif n1 in q[x] and n2 in q[x]:
			flag=0
			break
		elif n1 not in q[x] and n2 not in q[x]:
			flag=1
	if (flag==1):
		q.append([n1,n2])
		a=a+1	
				
for y in range(0,a):
	print "%s,%d" %(''.join(q[y]),y+1)
