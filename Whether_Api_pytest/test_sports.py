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
URL="http://api.weatherapi.com/v1/sports.json?key=a95fc31d83624cdfbda52019212207&q=London&days=1&aqi=no&alerts=no"
response=requests.get(URL)
data=response.json()
print(data)
#POSITIVE TESTCASES
#Positive Testcase For Testing The Status Code of the sports Api
def test_sports_success_code():
    assert response.status_code==200
    logging.info("status code  is 200.successfully passsed positive testcase")

#Positive Testcase For Testing The type of content of the sports   Api
def test_sports_get_content_type_equals_json():
    assert response.headers["Content-Type"] == "application/json"
    logging.info("content type is application/json .successfully passsed positive testcase")

#Positive Testcase For Testing The stadium of the sports Api
def test_sports_football_stadium():
    assert "football in data"
    logging.info("stadium is Maurice Dufrasne Stadium.successfully passsed positive testcase")

#Positive Testcase For Testing The country of the sports Api
def test_sports_football_country():
    assert data['football'][0]['region']==''
    logging.info("football region is empty.successfully passsed positive testcase")

##########################################################################################3

#NEGATIVE TESTCASES
#Positive Testcase For Testing The Status Code of the sports Api
def test_negative_sports_success_code():
    assert response.status_code!=400
    logging.info("status code  is 400 .successfully passsed negative testcase")

#negative Testcase For Testing The type of content of the sports   Api
def test_negative_sports_get_content_type_equals_json():
    assert response.headers["Content-Type"] != "application/xml"
    logging.info("content type is application/xml .successfully passsed negative testcase")

#negative Testcase For Testing The stadium of the sports Api
def test_negative_sports_key():
    assert 'stadium' not in data 
    logging.info("stadium is present in data.successfully passsed negative testcase")


#negative Testcase For Testing The country of the sports Api
def test_negative_sports_football_country():
    assert data['football'][0]['region']!="belgium"
    logging.info("region is belgium.successfully passsed negative testcase")

############# Script Details #################################################################

# Script Name            :  test_sports.py
# Script version         :  3.8.5
# Prepared By            :  Prathyusha.Konduru@infinite.com
# Created_date           :  22-07-21
# last_modification_date :  26-07-21

##############################################################################################

