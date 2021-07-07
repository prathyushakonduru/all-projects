#!/usr/bin/python3.8

#############################################################################################################

#To avoid the confusions of the existing tools
from __future__ import print_function
#It checks whether the path is exists or not
import os.path
#In order to build the client libraries
from googleapiclient.discovery import build
#In order to handle entire flow we import installed app flow
from google_auth_oauthlib.flow import InstalledAppFlow
#Manually refreshing the credentials
from google.auth.transport.requests import Request
#To provide the oauth2 access and refresh tokens
from google.oauth2.credentials import Credentials

#############################################################################################################

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive']

#############################################################################################################

def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                '/home/ubuntu01/google_drive_project/quickstart/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('drive', 'v3', credentials=creds)
    return service

#############################################################################################################

#Calling the main function
if __name__ == '__main__':
    main()
    
#############################################################################################################
############################### Script Details ##############################################################

# Script name               :       drive_quickstart.py
# Script version            :       1.0
# Prepared By               :       Prathyusha.Konduru@infinite.com
# Create Date               :       23-JUNE-2021
# Last Modification Date    :       25-JUNE-2021

#############################################################################################################