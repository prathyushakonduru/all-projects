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

###################################################################################################
#import logging with accurate time and date
import logging
logging.basicConfig(filename="whether.log",
                    format='%(asctime)s %(message)s',
                    filemode='w',level=logging.INFO)
#import requests and json
import requests, json
URL="http://api.weatherapi.com/v1/forecast.json?key=a95fc31d83624cdfbda52019212207&q=London&days=1&aqi=no&alerts=no"
response=requests.get(URL)
data=response.json()
print(data)
#Positive Testcase For Testing The Status Code of the Forecast Api
def test_forecast_success_code():
    assert response.status_code==200
    logging.info("status code  is 200.successfully passsed positive testcase")

#Positive Testcase For Testing The Region of the Forecast Api
def test_forecast_region():
    assert data['location']['region']=='City of London, Greater London'
    logging.info("region is City of London, Greater London.successfully passsed positive testcase")

#Positive Testcase For Testing The Country of the Forecast Api
def test_forecast_country():
    assert data['location']['country']=='United Kingdom'
    logging.info("country is United Kingdom.successfully passsed positive testcase")

#Positive Testcase For Testing The type of content of the Forecast Api
def test_forecast_get_content_type_equals_json():
    assert response.headers["Content-Type"] == "application/json"
    logging.info("content type is application/json .successfully passsed positive testcase")

#Positive Testcase For Testing The Type of Response of the Forecast Api
def test_forecast_type():
    assert type(data)==dict
    logging.info("Type of response body is dict .successfully passsed positive testcase")

#Positive Testcase For Testing Whether the key is present or not for the Forecast Api
def test_forecast_key_is_present_or_not():
    assert "forecast" in data
    logging.info("Tested whether the particular key is present in  the response body .successfully passsed positive testcase")

##########################################################################################################################################

#NEGATIVE TESTCASES
#Negative Testcase For Testing The Status Code of the Forecast Api
def test_negative_forecast_success_code():
    assert response.status_code!=400
    logging.info("status code  is 400.successfully passsed negative testcase")

#Negative Testcase For Testing The Region of the Forecast Api
def test_negative_forecast_region():
    assert data['location']['region']!='City of London'
    logging.info("Region is City of London .successfully passsed negative testcase")

#Negative Testcase For Testing The Country of the Forecast Api
def test_negative_forecast_country():
    assert data['location']['country']!='United states'
    logging.info("Country is United states .successfully passsed negative testcase")

#Negative Testcase For Testing The type of content of the Forecast Api
def test_negative_forecast_get_content_type_equals_json():
    assert response.headers["Content-Type"] != "application/xml"
    logging.info("content type is application/xml .successfully passsed negative testcase")

#Negative Testcase For Testing The Type of Response of the Forecast Api
def test_negayive_forecast_type():
    assert type(data)!=list
    logging.info("Type of data is list  .successfully passsed negative testcase")

#Negative Testcase For Testing Whether the key is present or not for the Forecast Api
def test_negative_forecast_key_is_present_or_not():
    assert "timezone" not in data


############# Script Details #################################################################

# Script Name            :  test_forecast.py
# Script version         :  3.8.5
# Prepared By            :  Prathyusha.Konduru@infinite.com
# Created_date           :  22-07-21
# last_modification_date :  26-07-21

##############################################################################################


   

