#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import jaconv
#https://pypi.org/project/jaconv/
#import pandas as pd
import sys
import csv


args = sys.argv



def check (i):

	if '\u3040'<=i<='\u309F' or '\u30A0'<=i<='\u30FF' or '\u0030'<=i<='\u0039' or '\u0041'<=i<='\u005A' or '\u0061'<=i<='\u007A' or '\u3000'<=i<='\u303F' or  '\u4e00'<=i<='\u9fff' or '\uFF00'<=i<='\uFFEF' or '\u0000'<=i<='\u007F':

		return True
	else:
		return False

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

#ZEN = "".join(chr(0xff01 + i) for i in range(94))
#HAN = "".join(chr(0x21 + i) for i in range(94))




file=open(args[1])


f=open(args[2],mode='w')

news=[]
memo=file.readline()
i=0
while (memo):
	i+=1

	#print (memo.strip())
	mm=memo.split(',')
	
	flag='1'
	kk=mm[4]
	print (kk)

	seq=mm[0]
	tag=mm[2]
	print (tag)

	if (tag=='0'):
		memo=file.readline()
		continue		
	
	if (len(kk)<50):
		memo=file.readline()
		continue		
	kk=kk.strip()
	kk=kk.rstrip('… ')
	kk=kk.lstrip('※')
	kk=kk.replace('.','')
	kk=kk.replace('^','')
	kk=kk.replace(',','')
	kk=kk.replace("\\t",'')
	kk=kk.replace("\\r",'')
	kk=kk.replace("\\n",'')
	
	if (kk in news):
		memo=file.readline()
		continue


	f.write(kk+'\t'+'1'+'\n')
	news.append(kk)

	memo=file.readline()
	i+=1
	#print (i)
	if (i>1000000):
		break

print (i)
file.close()
f.close()
