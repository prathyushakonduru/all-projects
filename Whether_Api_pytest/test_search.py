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
import logging
logging.basicConfig(filename="whether.log",
                    format='%(asctime)s %(message)s',
                    filemode='w',level=logging.INFO)
import requests, json
URL="http://api.weatherapi.com/v1/search.json?key=a95fc31d83624cdfbda52019212207&q=London&days=1&aqi=no&alerts=no"
response=requests.get(URL)
data=response.json()
print(data)
#POSITIVE TESTCASES
#Positive Testcase For Testing The Status Code of the Search Api
def test_search_success_code():
    assert response.status_code==200
    logging.info("status code  is 200.successfully passsed positive testcase")

#Positive Testcase For Testing The Content-Type of the Search Api
def test_search_get_content_type_equals_json():
    assert response.headers["Content-Type"] == "application/json"
    logging.info("content type is application/json .successfully passsed positive testcase")

#Positive Testcase For Testing The Type of data of the Search Api
def test_search_key_is_present_or_not():
    assert type(data)==list
    logging.info("Type of response body is list .successfully passsed positive testcase")

#Positive Testcase For Testing whether the KEY is present or not for the Search Api
def test_search_key_is_present_or_not():
    assert data[0]['country']=='United Kingdom'
    logging.info("country is United Kingdom.successfully passsed positive testcase")
    
#########################################################################################

#Negative Testcases
#Negative Testcase For Testing The Status Code of the Search Api
def test_negative_search_success_code():
    assert response.status_code!=400
    logging.info("status code  is 400.successfully passsed positive testcase")

#Negative Testcase For Testing The Content-Type of the Search Api
def test_negative_search_get_content_type_equals_json():
    assert response.headers["Content-Type"] != "application/xml"
    logging.info("content type is application/xml .successfully passsed positive testcase")

#Negative Testcase For Testing The Type of data of the Search Api
def test_negative_search_key_is_present_or_not():
    assert type(data)!=dict
    logging.info("Type of response body is dict .successfully passsed positive testcase")

#Negative Testcase For Testing whether the KEY is present or not for the Search Api
def test_search_key_is_present_or_not():
    assert data[0]['country']!='United states'
    logging.info("country is United states.successfully passsed positive testcase")

############# Script Details #################################################################

# Script Name            :  test_search.py
# Script version         :  3.8.5
# Prepared By            :  Prathyusha.Konduru@infinite.com
# Created_date           :  22-07-21
# last_modification_date :  26-07-21

##############################################################################################
