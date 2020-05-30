#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import pprint
import httplib2
from googleapiclient.discovery import build
import googleapiclient.http
import oauth2client.client

import io
from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools
from apiclient.http import MediaIoBaseDownload
#from apiclient.http import MediaFileUpload

#from pydrive.auth import GoogleAuth
#from pydrive.drive import GoogleDrive
import time
from datetime import timedelta

import datetime
import psycopg2

import codecs
from apiclient import errors
from apiclient.http import MediaFileUpload
import sys
import csv
import os


# ...

def update_file(service, file_id, new_title, new_description, new_mime_type,
                new_filename, new_revision):
  """Update an existing file's metadata and content.

  Args:
    service: Drive API service instance.
    file_id: ID of the file to update.
    new_title: New title for the file.
    new_description: New description for the file.
    new_mime_type: New MIME type for the file.
    new_filename: Filename of the new content to upload.
    new_revision: Whether or not to create a new revision for this file.
  Returns:
    Updated file metadata if successful, None otherwise.
  """
  try:
    # First retrieve the file from the API.
    file = DRIVE.files().get(fileId=file_id).execute()
    
    '''
    file['title'] = new_title
    file['description'] = new_description
    file['mimeType'] = new_mime_type
	'''
    
    media_body = MediaFileUpload(
        'efj', mimetype=new_mime_type, resumable=True)

    # Send the request to the API.
    updated_file = service.files().update(fileId=file_id,body=file,media_body=media_body).execute()
    return updated_file
  except errors.HttpError, error:
    print ('An error occurred: %s' % error)
    return None
def read_news():
	now=datetime.datetime.now()
	tdate=now.strftime("%Y-%m-%d")  
	conn = psycopg2.connect(dbname="medex13a", user="medex", password="medex")
	cur = conn.cursor()
	try:
		users=[]
		sql = 'copy(select "ID", "OrderDate",a1 from nsnotex2 where "患者"=252111 and "OrderDate"=current_date  order by "OrderDate" desc) to '+"'/tmp/today-news.csv' delimiter ','"
		cur.execute(sql)
		conn.commit()
	  
	except (Exception, psycopg2.DatabaseError) as error:
		pass
	finally:
		if conn is not None:
			conn.close()
		
	return 


if __name__ == '__main__':
	args = sys.argv
	filename=args[1]
	print (filename)
	subfilename=filename
	exist=True
	now=datetime.datetime.now()
	tdate=now.strftime("%Y%m%d")
	yes=now + timedelta(days=-1)
	ydate=yes.strftime("%Y%m%d")

	ffname='/tmp/'+subfilename+tdate+'.csv'
	print (ffname)
		
	if (os.path.isfile(ffname)):
		exist=True
		ddate=tdate
		print (ffname)
	
	else:
		ffname='/tmp/'+subfilename+ydate+'.csv'
		if (os.path.isfile(ffname)):
			exist=True
			ddate=ydate
		
			print (ffname)
		else:	
			exist=False

	#use yesterday date

	SCOPES = 'https://www.googleapis.com/auth/drive'
	store = file.Storage('storage.json-tn')
	creds = store.get()
	if not creds or creds.invalid:
		flow = client.flow_from_clientsecrets('client_id.json', SCOPES)
		creds = tools.run_flow(flow, store)
	DRIVE = discovery.build('drive', 'v3', http=creds.authorize(Http()))
		
	
	#read_news()
	#ffname='/tmp/'+subfilename+"_"+tdate+'.csv'
	if (exist):
		file_metadata = {
    'name': subfilename+ddate,
		
    'mimeType': 'application/vnd.google-apps.spreadsheet'}
		media = MediaFileUpload(ffname,
                        mimetype='text/csv',
                        resumable=True)
		file = DRIVE.files().create(body=file_metadata,
                                    media_body=media,
                                    fields='id').execute()
		print ('File ID: %s' % file.get('id'))

		
		
					
				
		
		
	print (ffname)
	#end of while
