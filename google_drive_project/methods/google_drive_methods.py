#!/usr/bin/python3.8

#############################################################################################################
#Purpose of the script

#############################################################################################################

#1.This script has been designed to write python test scripts for Google Drive
#to copy, create, delete, emptytrash, export, get, list and update.

#############################################################################################################

#Below points has been considered in the script:

#############################################################################################################

#1.Write test scripts for both positive and negative test cases
#2.Use loggers to print all the information on screen while executing and in log files

#############################################################################################################

#Importing the sys module for importing the file that are present in another folder
import sys
sys.path.append('/home/ubuntu01/google_drive_project/quickstart')
from drive_quickstart import main
#This module is used to Uploading the files
from apiclient.http import MediaFileUpload, MediaIoBaseDownload
#Importing loggers 
import logging
#############################################################################################################

#Creating the logger file with date and time format
logging.basicConfig(filename="methods.log",filemode = 'w', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
logging.info('Execution starts Here.')

#############################################################################################################

#Calling the main function and store that in a variable calles services
service = main()
logging.info("Calling the main methods from quickstart.py")

#############################################################################################################

#create a folder in google_drive
def create_folder():
    #Giving the folder name and type of the folder
    file_metadata = {
        'name': 'google_drive_folder',
        'mimeType': 'application/vnd.google-apps.folder'
    }
    logging.info("Giving the folder name and type of the folde") 
    #Creating the folder by using files.create method
    file = service.files().create(body=file_metadata).execute()
    logging.info("Folder created successfully in Google Drive")
    return file
 #############################################################################################################

#Uploading the file in a folder in Google Drive
def upload_file_without_using_folder():
    #Uploading file in a Google Drive
    file_metadata = {
    'name':'google_drive_project.py'
    }
    media = MediaFileUpload('google_drive_methods.py',
                            mimetype='text/python',
                            resumable=True)
    file = service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()
    logging.info("Successfully uploaded the file in Google Drive")

 #############################################################################################################

#Uploading the file in a folder in Google Drive
def upload_file_with_particular_folder():
    #Giving the particular Folder Id along with giving the file name
    folder_id = '1nGyMth-ElY-en3zoc94bO6BUoMk_D3R6'
    file_metadata = {
    'name': 'drive_quicksort.py',
    'parents': [folder_id]
    }
    media = MediaFileUpload('/home/ubuntu01/google_drive_project/quickstart/drive_quickstart.py',
                        mimetype='text/python',
                        resumable=True)
    logging.info("Uploading the existing image/jpeg and storing it a variable")
    #Creating the uploaded file in Google Drive
    file = service.files().create(body=file_metadata,
                                    media_body=media,
                                    fields='id').execute()
    logging.info("Successfully uploaded the file in a folder.")

 #############################################################################################################

#Listing all the files along with ids
def list_the_files():
    #Creating the empty list to store the ids and file names
    lst=[]
    # Call the Drive v3 API
    results = service.files().list(
         pageSize=50, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])
    #If files are not there in Drive it will print no files found else it list out all the files.
    if not items:
        print('No files found.')
        logging.info('Files are not present')
    else:
        print('Files:')
        for item in items:
            lst.append([item['name'], item['id']])
        #print(lst)
        logging.info("Successfully listing all the files that are present in Google Drive.")
    return lst

#############################################################################################################

#Fetching the specific data by providing specific id
def get_files():
    results = service.files().get(fileId='1Nu8k6wjSk1taHzdaSUUAqaSnITPvCn2H-Ngd9-rbR8c').execute()
    #print(results)
    logging.info("Successfully returning the data that are present in particulat id.")
    return results

#############################################################################################################

#Delete the particular file by providing particular id
def delete_file(file_id):
    results = service.files().delete(fileId=file_id).execute()
    #print(results)
    logging.info("Successfully deleting the file in Google Drive")
    return results

#############################################################################################################

# Delete all the files and empty the bin
def empty_trash():
    results=service.files().emptyTrash().execute()
    #print(results)
    logging.info("Successfully empty the trash.")
    return results

#############################################################################################################

#copy the file into the google drive
def copy_file():
    results = service.files().copy(fileId='1BQq7FJJQ9NXOLvgjacoS83HgmAwWmu6b').execute()
    #print(results)
    logging.info("copy done successfully")
    return results

#############################################################################################################

#Genareting the file Ids present in google drive
def generate_id():
    results = service.files().generateIds().execute()
    #print(results)
    logging.info("Successfully generating all the file ids.")
    return results
#############################################################################################################

#converting documrnt to pdf file
def export_file():
    #providing the specific file id
    file_id='1Nu8k6wjSk1taHzdaSUUAqaSnITPvCn2H-Ngd9-rbR8c'
    #Exporting that document file to pdf format
    results = service.files().export(fileId=file_id,mimeType='application/pdf',fields='id').execute()
    #Opening and creating the file with pdf format and storing the results
    with open('/home/ubuntu01/prathyusha.pdf','wb') as f1:
        f1.write(results)
        f1.close()
        print("doc exported successfully")
    logging.info("Successfully exporting the file from decument to pdf format.")

#############################################################################################################

#Upating the specific file
def move_file():
    #Providing the specific fileid and folder id
    file_id='1Nu8k6wjSk1taHzdaSUUAqaSnITPvCn2H-Ngd9-rbR8c'
    folder_id='1nGyMth-ElY-en3zoc94bO6BUoMk_D3R6'
    logging.info("#Providing the specific fileid and folder id")
    #retrive the existing parents to remove
    file=service.files().get(fileId=file_id,fields='parents').execute()
    previous_parents=",".join(file.get('parents'))
    #move the file to new folder
    file=service.files().update(fileId=file_id,addParents=folder_id,removeParents=previous_parents,
                               fields='id, parents').execute()
    #print(file)
    print('moved')
    logging.info("Updating the file successfully.")
    return file

def update_file():
    file = service.files().get(fileId='1Nu8k6wjSk1taHzdaSUUAqaSnITPvCn2H-Ngd9-rbR8c').execute()
    file ['name'] = 'sandeep_kumar.docx'
    #print(file)
    return file



#calling the methods
if __name__ == '__main__':
    #upload_file_without_using_folder()
    #upload_file_with_particular_folder()
    #list_the_files()
    #get_files()
    #delete_file('1bPsryid2cfh7jozhLh3b2cODgzyaUkEX')
    #empty_trash()
    #copy_file()
    generate_id()
    #export_file()
    #update_file()
    #move_file()
    #create_folder()

#############################################################################################################
############################### Script Details ##############################################################

# Script name               :       google_drive_methods.py
# Script version            :       1.0
# Prepared By               :       Prathyusha.Konduru@infinite.com
# Create Date               :       23-JUNE-2021
# Last Modification Date    :       27-JUNE-2021

#############################################################################################################

