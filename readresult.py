#!/usr/bin/env python
# -*- coding: utf-8 -*-
import jaconv
#https://pypi.org/project/jaconv/
'''
def han2zen(han):
	ZEN = "".join(chr(0xff01 + i) for i in range(94))
	HAN = "".join(chr(0x21 + i) for i in range(94))

	ZEN2HAN = str.maketrans(ZEN, HAN)
	HAN2ZEN = str.maketrans(HAN, ZEN)
	return han.translate(HAN2ZEN)
# 全角から半角
	#print(ZEN.translate(ZEN2HAN))
# 結果
# !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~

# 半角から全角
	#print(HAN.translate(HAN2ZEN))

'''






#file=open('/disk3/news/ns22-f')
#f=open('/disk3/news/news-22-0.csv',mode='w')
#file=open('/home/medex/nlpnews/news-result-0310-2.txt')
file=open('/home/medex/nlpnews/log2.text')
f2=open('/home/medex/nlpnews/dev.tsv')
f=open('/home/medex/nlpnews/news-result',mode='w')
nw=[]
tag={'0':'A','1':'B','2':'C','3':'D','4':'E'}
#tag={'0':'0','1':'1','2':'C','3':'D','4':'E'}
news=f2.readline()
i=0
while (news):
	print (news)
	nw.append(news)
	news=f2.readline()
	i+=1

print (i)

memo=file.readline()
i=0
s=0
ff=0
f.write("NO  datatag  correct predict same content"+'\n')
while (memo):
	cont=nw[i]
	ww=cont.split('\t')
	#print (ww[1])
	#print (memo)
	wws=ww[1].replace('\t','')
	#wws=wws.replace('\r','')
	memo=memo.strip()
	mm=memo.split(' ')
	tag0=tag[mm[0]]
	tag1=tag[mm[1]] 
	if (tag0==tag1):
		s+=1
		same='s'
	else:
		same=' '
		ff+=1
	f.write(str(i)+';'+wws+';'+tag1+';'+tag0+';'+same+';'+cont+'\n')
	memo=file.readline()
	i+=1
	#print (i)
	if (i>500):
		break
print (i)
print ("correct"+str(s))
print ("wrong"+str(ff))
file.close()
f.close()
