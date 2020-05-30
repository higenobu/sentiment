#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import jaconv
import sys

args = sys.argv

#with open(args[1]) as f:
#    reader = csv.reader(f, delimiter='\t')


f2=open(args[1])
#f=open(args[3],mode='w')
nw=[]
#tag={'':'','0':'A','1':'B','2':'C','3':'D','4':'E'}
#tagab=['A','B']
#tag={'0':'0','1':'1','2':'C','3':'D','4':'E'}
#read news
news=f2.readline()

i=0
while (news):
	#print (news)
	nw.append(news)
	news=f2.readline()
	i+=1

kk=i

i=0
s=0
ff=0
a=0
#f.write("NO  datatag  correct predict same content"+'\n')
for i in range(len(nw)):
	
	cont=nw[i]
	#print (cont)
	ww=cont.split(';')
	
	
	print (ww[2])
	if (ww[2]=='0'):
		print (ww[4])
		ff+=1
	else:
		s+=1
		

print (ff)
print (s)
print (len(nw))		
print (str(float(ff)/float(len(nw))))
	

f2.close()