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
URL="http://api.weatherapi.com/v1/astronomy.json?key=a95fc31d83624cdfbda52019212207&q=London&dt=2021-07-22"
response = requests.get(URL)
data = response.json()
print(data)

#POSITIVE TESTCASES
#Positive Testcase For Testing The Status Code of the Astronomy Api
def test_astronomy_status_code():
    assert response.status_code==200
    logging.info("status code is 200 .successfully passsed positive testcase")
    
#Positive Testcase For Testing The type of content of the Astronomy Api
def test_astronomy_content_type_equals_to_json():
    assert response.headers["Content-Type"] == "application/json"
    logging.info("content type is application/json .successfully passsed positive testcase")

#Positive Testcase For Testing The Region of the Astronomy Api
def test_astronomy_city():
    assert data['location']['region']=='City of London, Greater London'
    logging.info("region is City of London, Greater London.successfully passsed positive testcase")

#Positive Testcase For Testing The Country of the Astronomy Api
def test_astronomy_country():
    assert data['location']['country']=='United Kingdom'
    logging.info("country is United Kingdom.successfully passsed positive testcase")

    
#Positive Testcase For Testing The Type of Response of the Astronomy Api
def test_astronomy_type():
    assert type(data)==dict
    logging.info("Type of response body is dict .successfully passsed positive testcase")

#Positive Testcase For Testing Whether the key is present or not for the Astronomy Api
def test_astronomy_key():
    assert "location" in data
    logging.info("Tested the particular key in the response body.successfully passsed positive testcase ")
###############################################################################################

#NEGATIVE TESTCASES
#Positive Testcase For Testing The Status Code of the Astronomy Api
def test_neagtive_astronomy_status_code():
    assert response.status_code!=400
    logging.info("status code  is 400.successfully passsed negative testcase")

#Positive Testcase For Testing The type of content of the Astronomy Api
def test_negative_astronomy_content_type_equals_to_json():
    assert response.headers["Content-Type"] != "application/xml"
    logging.info("content type is application/xml .successfully passsed negative testcase")

#Positive Testcase For Testing The Region of the Astronomy Api
def test_negative_astronomy_city():
    assert data['location']['region']!='City of London'
    logging.info("Region is City of London .successfully passsed negative testcase")

#Positive Testcase For Testing The Country of the Astronomy Api
def test_negative_astronomy_country():
    assert data['location']['country']!='United states'
    logging.info("Country is United states .successfully passsed negative testcase")

#Positive Testcase For Testing The Type of Response of the Astronomy Api
def test_negative_astronomy_type():
    assert type(data)!=list
    logging.info("Type of data is list  .successfully passsed negative testcase")

#Positive Testcase For Testing Whether the key is present or not for the Astronomy Api
def test_negative_astronomy_key():
    assert "current" not  in data
    logging.info("Tested the particular key in the response body.successfully passsed negative testcase ")
############# Script Details #################################################################

# Script Name            :  test_astronomy.py
# Script version         :  3.8.5
# Prepared By            :  Prathyusha.Konduru@infinite.com
# Created_date           :  22-07-21
# last_modification_date :  26-07-21

##############################################################################################


