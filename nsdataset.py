#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import jaconv
#https://pypi.org/project/jaconv/
#import pandas as pd
import sys
import csv
import argparse

args = sys.argv


def nsdataset(news,addnews):
	conv={'A':'1','B':'1','C':'1','D':'0','E':'0'}
	file=open(news)
	f=open(addnews,mode='w')

	memo=file.readline()
	i=0
	while (memo):
		i+=1
	
		print (memo.strip())
		mm=memo.split('\t')
	
		flag=mm[1]
		flag=flag.strip('\n')
		kk=mm[0]
		newflag=conv[flag]
		print (newflag)

		f.write(kk+'\t'+newflag+'\n')
		memo=file.readline()
		i+=1
		print (i)
		if (i>50000):
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
    
  nsdataset(args.news,args.addnews)
