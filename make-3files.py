#!/usr/bin/env python
# -*- coding: utf-8 -*-
import jaconv

file=open('/tmp/news-44/all.tsv')
f2=open('/tmp/news-44/dev.tsv',mode='w')
f3=open('/tmp/news-44/test.tsv',mode='w')
f1=open('/tmp/news-44/train.tsv',mode='w')
nw=[]
#tag={'0':'A','1':'B','2':'C','3':'D','4':'E'}
tag={'0':'0','1':'1','2':'C','3':'D','4':'E'}
news=file.readline()
i=0
while (news):
	print (news)
	newss=news.strip()
	print (newss)
	nw.append(newss)
	news=file.readline()
	i+=1

print (i)
w15=int(i*0.15)

for ii in range(i):
	if (ii<w15):

		f2.write(nw[ii]+'\n')
		
	elif (ii>=w15 and ii<(w15*2)):
		f3.write(nw[ii]+'\n')

	else:
		f1.write(nw[ii]+'\n')

file.close()
f1.close()
f2.close()
f3.close()
