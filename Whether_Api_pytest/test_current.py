#!/usr/bin/python3.8

# Purpose of the Script
#############################################################################################

#The script has been designed to test whether api by using the pytest framework

#############################################################################################
# Below points has been considered in the Script
#############################################################################################
#1.sign up as new user in the in whether API 

#2.Login to the whether API we get the api key

#3.By using that API key we checked the different APIS

#4.Write test scripts for those APIS

##############################################################################################
#import logging with accurate time and date 
import logging
#import request and json
import requests,json
logging.basicConfig(filename="whether.log",
                    format='%(asctime)s %(message)s',
                    filemode='w',level=logging.INFO)
#URL is used for gettting the data from the Whether API
URL="http://api.weatherapi.com/v1/current.json?key=a95fc31d83624cdfbda52019212207&q=London&aqi=no"
response = requests.get(URL)
data = response.json()
print(data)
#Positive TESTCASES
#Positive Testcase For Testing The Status Code of the Current Api
def test_current_status():
    assert response.status_code==200
    logging.info("Tested status code .successfully passsed positive testcase")

#Positive Testcase For Testing The Region of the Current Api
def test_current_region():
    assert data['location']['region']=='City of London, Greater London'
    logging.info("Tested region .successfully passsed positive testcase")

#Positive Testcase For Testing The Country of the Current Api
def test_current_country():
    assert data['location']['country']=='United Kingdom'
    logging.info("Tested country.successfully passsed positive testcase")

#Positive Testcase For Testing The type of content of the Current Api
def test_current_get_content_type_equals_json():
    assert response.headers["Content-Type"] == "application/json"
    logging.info("Tested content type.successfully passsed positive testcase")

#Positive Testcase For Testing The Type of Response of the Current Api
def test_current_type():
    assert type(data)==dict
    logging.info("Tested the type of response body.successfully passsed positive testcase")

#Positive Testcase For Testing Whether the key is present or not for the Current Api
def test_current_key_is_present():
    assert "location" in data
    logging.info("Tested the particular key in the response body.successfully passsed positive testcase ")

#############################################################################################

#NEGATIVE TESTCASES
#Negative Testcase For Testing The Status Code of the Current Api
def test_negative_current_status():
    assert response.status_code!=401
    logging.info("Tested status code .successfully passsed negative testcase")

#Negative Testcase For Testing The Region of the Current Api
def test_negative_current_region():
    assert data['location']['region']!='City of London'
    logging.info("Tested region .successfully passsed negative testcase")

#Negative Testcase For Testing The Country of the Current Api
def test_negative_current_country():
    assert data['location']['country']!='England'
    logging.info("Tested country.successfully passsed negative testcase")

#Negative Testcase For Testing The type of content of the Current Api
def test_negative_current_get_content_type_equals_json():
    assert response.headers["Content-Type"] != "application/xml"
    logging.info("Tested content type.successfully passsed negative testcase")
    
#Negative Testcase For Testing The Type of Response of the Current Api
def test_negative_current_type():
    assert type(data)!=list
    logging.info("Tested the type of response body.successfully passsed negative testcase")

#Positive Testcase For Testing Whether the key is present or not for the Current Api
def test_negative_current_key_is_present():
    assert "time"  not in data
    logging.info("Tested the particular key in the response body.successfully passsed negative testcase ")

############# Script Details #################################################################

# Script Name            :  test_current.py
# Script version         :  3.8.5
# Prepared By            :  Prathyusha.Konduru@infinite.com
# Created_date           :  22-07-21
# last_modification_date :  26-07-21

##############################################################################################

