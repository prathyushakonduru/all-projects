#Purpose of the script
########################################################################################################################
# Google drive API Validation.
# Create and execute test cases in pytest for the all the operations COPY, CREATE, DELETE, EMPTYTRASH, EXPORT, GET, LIST and UPDATE
########################################################################################################################


#import sys module to append the path
import sys 
sys.path.append('/home/ubuntu01/google_drive_project/methods')
#importing the google_drive methods
import google_drive_methods
#importing the pytest module to test the script
import pytest
#import logging
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
#initialising list to store the file_ids
lst=[]
#storing the file_ids and fiel_names in the result variable
result=google_drive_methods.list_the_files()
for i in range(len(result)):
    lst.append(result[i][1])

#POSITIVE TESTCASES

#Checking whether the id is present in google drive or not
def test_list_files():
    id='1Nu8k6wjSk1taHzdaSUUAqaSnITPvCn2H-Ngd9-rbR8c'
    for i in range(len(result)):
        if id in result[i][1]:
            assert id in result[i][1]
    logger.info("file_id is present in google drive positive testcase  done successfully")


#Checking the particular filename in google drive 
def test_get_file():
    result = google_drive_methods.get_files()
    assert 'sandeep.docx' in result['name']
    logger.info("fileneme is present in result positive testcase done sucessfully")

#Checking type of data    
def test_get_file_1():
    result = google_drive_methods.get_files()
    assert type(result) is dict
    logger.info("The type of result is dict positive testcase done successfully")

#Checking length of the data   
def test_get_file_2():
    result = google_drive_methods.get_files()
    assert len(result) > 0
    logger.info("The length is greater than 0 positive testcase done successfully")

#Checking the particular File is deleted or not
def test_delete():
    google_drive_methods.delete_files('1-0hY7IktX3FXhJn-jLdrGptXQqzT_yXq')
    result=google_drive_methods.list_the_files()
    print(result)
    lst=[]
    for i in range(len(result)):
        lst.append(result[i][1])
    assert '1-0hY7IktX3FXhJn-jLdrGptXQqzT_yXq' not in lst
    logger.info("file_id is deleted positive testcase done successfully")

#creating the folder in google drive
folder_details=google_drive_methods.create_folder()
def test_create_folder():
    assert folder_details['name']=='google_drive_folder'
    logger.info("tested the create folder done successfully")
#creatin the type of id   
def test_create_folder_1():
    assert type(folder_details) is dict
    logger.info("Tested the type of result")

#Checking the folder_id is present in list or not
def test_create_3():
    for i in range(len(result)):
        if folder_details['id'] in result[i][1]:
            assert folder_details['id'] in result[i][0]
            logger.info("file_id is present in result then positive testcase done successfully")

#Checking the trash is empty or not
def test_emptytrash():
    empty_trash=''
    result=google_drive_methods.empty_trash()
    assert result==empty_trash
    logger.info("If result equal to empty positive testcase done successfully")

#Checking the id is generated or not
def test_generate_id_1():
    results=google_drive_methods.generate_id()
    assert len(results)!=0
    logger.info("if result is not equal to zero  positive testcase done successfully")

#Checking the type of generated id
def test_generate_id_2():
    results=google_drive_methods.generate_id()
    assert type(results)==dict
    logger.info("If type of result is equal to dict positive testcase done successfully")

move_data=google_drive_methods.move_file()
#move the file to google drive
def test_move_file():
    file_id='1Nu8k6wjSk1taHzdaSUUAqaSnITPvCn2H-Ngd9-rbR8c'
    assert file_id==move_data['id']
    logger.info("both file_ids are same positive testcase passed successfully")

#move the folder to google drive
def test_move_file_1():
    folder_id=['1nGyMth-ElY-en3zoc94bO6BUoMk_D3R6']
    assert folder_id==move_data['parents']
    logger.info("Both folder_ids are same positive testcase done successfully")

###############################################################################################

#NEGATIVE TESTCASES

#checking the id is present in list or not
def test_negative_list_files():
    id='1Nu8k6wjSk1taHzdaS'
    for i in range(len(result)):
        if id not in result[i][1]:
            assert id not in result[i][1]
    logger.info("id is not present in list negative testcase done successfully")

#Checking particular file id present in google drive or not
def test_negative_get_file():
    result = google_drive_methods.get_files()
    assert 'sandeep_kumar.docx' not in result['name']
    assert type(result) is not set
    logger.info("get the file done negative testcase passed successfully")

#Tested the creation of  folder
def test_negative_create_folder():
    assert folder_details['name']!='google_folder'
    assert type(folder_details) is not list
    logger.info("Tested create folder done negative testcase passed successfully")

#Tested the trash is empty or not
def test_negative_emptytrash():
    empty_trash='sjadlskj'
    result=google_drive_methods.empty_trash()
    assert result!=empty_trash
    logger.info("both the results are same negative testcase pased done successfully ")
#Checking the type and length of generated ids
def test_negative_generate_id_1():
    results=google_drive_methods.generate_id()
    assert len(results)>=0
    assert type(results)is not list
    logger.info("Tested the type of generate_ids negative testcase passed successfully")
#move the file to google drive
def test_negative_move_file():
    file_id='1Nu8k6wjSk1taHzdaSUUAqaSnITPvCn'
    assert file_id!=move_data['id']
    logger.info("both ids are not same negative testcase done successfully")

#move the folder to google drive
def test_negative_move_folder():
    folder_id=['1nGyMth-ElY-en3zoc94bO6BUoMk_D3']
    assert folder_id!=move_data['parents']
    logger.info("both ids are not same negative testcase done successfully")

###################################################################################################

#The below function test_response_time_less_than_200() is used to check if the ressponse time taken is less than 300.
def test_response_time_less_than_200():
    response = requests.get('https://drive.google.com/drive/u/1/my-drive')
    time = response.elapsed.total_seconds() * 1000
    print(time)
    assert time <= 300

# The below function test_response_time_more_than_200() is used to check if the ressponse time taken is more than 200.
def test_response_time_more_than_200():
    response = requests.get('https://drive.google.com/drive/u/1/my-driv')
    time = response.elapsed.total_seconds() * 1000
    print(time)
    assert time >= 300   

#############################################################################################################

#Checking if a valid headers has being received from the server.
def test_valid_headers():
    response = requests.get('https://drive.google.com/drive/u/0/my-drive')      
    head = response.headers['Content-Type']
    assert head == 'text/html; charset=UTF-8'
    logging.info('Valid headers has been fetched')
    
#Checking if a valid headers has being received from the server.
def test_invalid_headers():
    response = requests.get('https://drive.google.com/drive/u/0/my-driv')      
    head = response.headers['Content-Type']
    assert head != 'text/html; charset=UTF-8'
    logging.error('Invalid Page')
    
#############################################################################################################
############################### Script Details ##############################################################

# Script name               :       google_drive_methods.py
# Script version            :       1.0
# Prepared By               :       Prathyusha.Konduru@infinite.com
# Create Date               :       23-JUNE-2021
# Last Modification Date    :       27-JUNE-2021

#############################################################################################################
 












       
    