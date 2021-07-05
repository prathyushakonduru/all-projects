#!/usr/bin/python3.8

#############################################################################################################

#Purpose of the script

#############################################################################################################

#1.This script has been designed to test the any Ecommerce Application(Amazon) by using selenium

#############################################################################################################

#Below points has been considered in the script:

#############################################################################################################

#1.Signup as a new user in paticular Ecommerce Application(Amazon).
#2.Then enter username, phoneno, password(it is readed from text file).
#3.After clicking on signup button. If username, password, phoneno has not been provided.
#4.Then filter out the string error and the corresponding color .
#5.Then compare obtained colors with a set of expected output colors and print success message and error message accordingly.
#6.Then sigin with valid emailid and valid password.
#7.Check system behavior when invalid email id and valid password is entered.
#8.Check system behavior when valid email id and invalid password is entered.
#9.Then check Forgot your password is working as expected or not.
#10.Check system behavior when "Keep me signed" is checked or not.
#11.Use loggers to print all the information on screen while executing and in log files

#############################################################################################################

#import the unittest and file
import ecommerce_signup 
import unittest
from selenium import webdriver
import selenium
import time
import logging
from selenium.webdriver.common.keys import Keys
amazon_class_instance=ecommerce_signup.BrowserstackCrawler()
class TestLogin(unittest.TestCase):
    logger=logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO)

    #Test the get page             
    def test_getpage(self):
        assert ecommerce_signup.getPage()=="https://www.amazon.in/"
        self.logger.info("it checks the getpage successfully")

    #Test_signup page
    def test_signup(Self):
        assert amazon_class_instance.signup()=="mobile number is already in use"
        self.logger.info("Already a user,testcase passed successfully")

    #Test the colour
    def test_colour(self):
        assert amazon_class_instance.validate_signupform()=="rgba(221, 0, 0, 1)"
        self.logger.info("Getting color and expected color both are same.Testcase passed successfully")

    #Test the invalid_username
    def test_invalid_username(self):
        assert amazon_class_instance.invalid_username()=="we cant find the account with that email address"
        self.logger.info("it checks successfully if invaild userid is provided")
    #Test invalid_pasword
    def test_invalid_password(self):
        assert amazon_class_instance.invalid_password()=="invalid password"
        self.logger.info("tested the invaild password successfully")
    
    #Test forgot password
    def test_forgot_password(self):
        assert amazon_class_instance.forgot_password()=="prathyusha@99"
        self.logger.info("forgot password checked successfully")

    #Test the keepme signed in
    def test_keepme_signed_in(self):
        assert amazon_class_instance.keep_signin()=="keep me signed in done successfully"
        self.logger.info("keepme signed in checked successfully")

    #Test the valid user and password
    def test_valid_user_password(self):
        assert amazon_class_instance.signin()=="user sign in done successfully"
        self.logger.info("tested succssfully when valid username and valid password")

    #Closing the browser every testcase    
    
#############################################################################################################

#Change the command-line entry point to call unittest.main()
if __name__ == '__main__':
    unittest.main()
logger.info("Execution ended here:")

#############################################################################################################
############################### Script Details ##############################################################

# Script name               :       test_ecommerce_unittest.py
# Script version            :       1.0
# Prepared By               :       Prathyusha.Konduru@infinite.com
# Create Date               :       15-JUNE-2021
# Last Modification Date    :       18-JUNE-2021

#############################################################################################################