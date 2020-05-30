#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import jaconv
#https://pypi.org/project/jaconv/
#import pandas as pd
import sys
import csv
import argparse

args = sys.argv





def nsdatacl(news,addnews):
	file=open(news)
	f=open(addnews,mode='w')

	memo=file.readline()
	i=0
	while (memo):
		i+=1
	
		print (memo.strip())
		mm=memo.split(';')
	
		odate=mm[0]
		kk=mm[1]
	#kk=kk.decode('utf-8')
	
		kk=kk.replace('"','')
		kk=kk.replace('.','')
		kk=kk.replace(',','')
		kk=kk.replace('\\r','')
		kk=kk.replace('\\t','')
		kk=kk.replace('\\n','')
		kk=kk.replace('^','')
		aa=kk.find('datePublished:')
		if (aa):
			print ("find date")
			mk=kk[0:aa]
		else:
			mk=kk[:]
		f.write(odate+';'+mk+'\n')
		memo=file.readline()
		i+=1
		print (i)
		if (i>500000):
			break


	file.close()
	f.close()

if __name__=='__main__':
  parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
  parser.add_argument(
      'news',
      help='news')
  parser.add_argument(
      'addnews',
      help='addnews')
    
    
  args = parser.parse_args()
    
  nsdatacl(args.news,args.addnews)
