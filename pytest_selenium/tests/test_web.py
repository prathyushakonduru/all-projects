
##############################################################################################
#Purpose of the script
##########################################################################################################
#1.automating the website using automation testing with python,selenium

##########################################################################################################
#contents of the script:
##########################################################################################################
#1.Install the selenium
#2.Write the python code with selenium webdriver using chrome
#3.Creating a pages folder in that create a files result.py, search.py.
#4.In tests folder  test_web.py change the code and create config.json with time and browser
#5.In tests create the confest.py where write the logic for fixtures, browser
##########################################################################################################

import pytest

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage
import logging
##########################################################################################################
logging.basicConfig(filename="test_web.log",level=logging.DEBUG,format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
logging.info('Execution starts Here.')

##########################################################################################################
logging.info('function for duckduckgo web')
def test_basic_duckduckgo_search(browser):
  # Set up test case data
    logging.info("passing panda as phrase")
    PHRASE = 'panda'
  # Search for the phrase
    search_page = DuckDuckGoSearchPage(browser)
    logging.info('page loading')
    search_page.load()
    logging.info('phrase searching')
    search_page.search(PHRASE)
  # Verify that results appear
    result_page = DuckDuckGoResultPage(browser)
    assert result_page.link_div_count() > 0
    assert result_page.phrase_result_count(PHRASE) > 0
    assert result_page.search_input_value() == PHRASE
    logging.info('Execution ends here')

##########################################################################################################

############################################# Script Details #############################################

# Script name               :       test_web.py
# Script version            :       1.0
# Prepared By               :       Rishitha.Gurramkonda@infinite.com
# Create Date               :       03-JUNE-2021
# Last Modification Date    :       07-JUNE-2021

##########################################################################################################
