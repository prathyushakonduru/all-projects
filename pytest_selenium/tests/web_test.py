##########################################################################################################
#Pupose of the Script
#Creating the report by writing the python code

##########################################################################################################
#Contents of the script
##########################################################################################################

#1.By using python code provide token.
#2.The token will be generated in integrations and copy it and paste in token.
#3.provide username and password.

##########################################################################################################
from src.testproject.sdk.drivers import webdriver
#importing the logging
import logging

logging.basicConfig(filename="web_test_log.log",level=logging.DEBUG,format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

##########################################################################################################
def simple_test():
    logging.info('providing the token ')
    driver = webdriver.Chrome(token="7GjsewSQLddLkDwhrA3KW7kYjfPoMd2pEQvyBnekguc1")
    logging.info('providing the web of testproject')
    driver.get("https://example.testproject.io/web/")
    logging.info('providing the username and password')
    driver.find_element_by_css_selector("#name").send_keys("John Smith")
    driver.find_element_by_css_selector("#password").send_keys("12345")
    driver.find_element_by_css_selector("#login").click()

    passed = driver.find_element_by_css_selector("#logout").is_displayed()

    print("Test passed") if passed else print("Test failed")

    driver.quit()


if __name__ == "__main__":
    simple_test()

##########################################################################################################

############################################# Script Details #############################################

# Script name               :       web_test.py
# Script version            :       1.0
# Prepared By               :       Rishitha.Gurramkonda@infinite.com
# Create Date               :       03-JUNE-2021
# Last Modification Date    :       07-JUNE-2021

##########################################################################################################
