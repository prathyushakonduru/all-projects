#!/usr/bin/python3.8

# Purpose of the Script
#############################################################################################

#The script has been designed to test any E_commerce_application(Amazon) by using selenium

#############################################################################################
# Below points has been considered in the Script
#############################################################################################

#1.sign up as new user in the particular e_commerce_application(Amazon)  

#2.Enter username,phone_number,email_id and password(password read from text_files )

#3.If username mobile_number and password has not been provided 

#4.filter out the string error and the corresponding color 

#5.Then compared obtained_color with a set of expected output colors and print success message and error message accordingly 

#6.Then signin with valid mail_id and password

#7.Check system behavior when valid email id and invalid password is entered.

#8.Check system behavior when invalid email id and valid password is entered.

#9.Then check forgot password is working or not

#10.check keepme signed in working or not

#11.A log file created with the current date time along with message specified.

###########################################################################################

#importinfg webdriver to perform automated browser testing on chrome browser
from selenium.webdriver import Chrome, ChromeOptions
#importing the time module
import time
#importing the action chains to drag an element ,click an element
from selenium.webdriver.common.action_chains import ActionChains
#import loggers
import logging

#############################################################################################

#creating a file with date nd time format
logging.basicConfig(filename="amazon.log",
                    format='%(asctime)s %(message)s',
                    filemode='w',level=logging.INFO)
#providing the url
BASE_URL = "https://www.amazon.in"
#providing the mail id
EMAIL_ID = "prathyusharaju223@gmail.com"
#providing the expected colour
EXPECTED_COLOR = "rgba(221, 0, 0, 1)"

                   
#This method is used to open the amazon home page
def getPage():
   browser = Chrome('/usr/bin/chromedriver')
   browser.get(BASE_URL)
   return browser.current_url

#############################################################################################

 #creating a class     
class BrowserstackCrawler(object):
   def __init__(self):
      self.browser = Chrome('/usr/bin/chromedriver')
      self.browser.get(BASE_URL)
   

#############################################################################################
   # This method is used to sign in the amazon
   def signup(self):
      # Navigate to Signup Page
      action=ActionChains(self.browser)
      firstmenu= self.browser.find_element_by_xpath('//*[@id="nav-link-accountList-nav-line-1"]')
      action.move_to_element(firstmenu).perform()
      #It clicks on signup  page
      secondmenu = self.browser.find_element_by_xpath('//*[@id="nav-flyout-ya-newCust"]/a')
      secondmenu.click()
      logging.info("successfully clicked on signup button")
      mobile_number="9381194363"
      # It fills the username
      element = self.browser.find_element_by_name("customerName")
      element.send_keys("sandeep")
      logging.info("successfully filled the username")
      #It fills the mobile number
      element = self.browser.find_element_by_name("email")
      element.send_keys('9381194363')
      logging.info("successfully filled the mobile number")
      #it fills the mail_id
      element = self.browser.find_element_by_name("secondaryLoginClaim")
      element.send_keys('konduruprathyushas@gmail.com')
      logging.info("successfully filled the email_id")
      #it fills the password
      element = self.browser.find_element_by_name("password")
      element.send_keys("sandeep@25")
      logging.info("successfully filled the password")
      #it clicks on continue button
      element = self.browser.find_element_by_id("continue")
      logging.info("successfully clicked on continue button")
      element.click()
      #it checks the mobile number 
      if mobile_number=="9381194363":
         return "mobile number is already in use"
      else:
         print("acoount created successfully")
      #time.sleep(40)
      self.browser.quit()

#############################################################################################

   '''This method is used to filter out the string error and the corresponding color 
      Then  it comparedobtained_color with a set of expected output colors and 
      print success message and error message accordingly''' 
   def validate_signupform(self):
      action=ActionChains(self.browser)
      firstmenu= self.browser.find_element_by_xpath('//*[@id="nav-link-accountList-nav-line-1"]')
      action.move_to_element(firstmenu).perform()
      time.sleep(2)
      secondmenu = self.browser.find_element_by_xpath('//*[@id="nav-flyout-ya-newCust"]/a')
      secondmenu.click()
      logging.info("successfully clicked on the signup button")
      element = self.browser.find_element_by_id("continue")
      element.click()
      logging.info("successfully clicked on continue")
      time.sleep(4)
      #username is not provided in the signup page
      username = self.browser.find_element_by_name('customerName')
      if "error" in username.get_attribute('outerHTML'):
         #get the colour and storing in the variable called obtained colour
         obtained_color = username.value_of_css_property('border-bottom-color')
         logging.info("get the colourand storing in the variable called obtained colour")
         if not self.check_color(obtained_color, "rgba(221, 0, 0, 1)"):
            print(f"expected color is {EXPECTED_COLOR} and got {obtained_color}")
         else:
            print("please provide the username")
            logging.info("please provide the username")
      #mobile number is not provided signup page
      mobile_number = self.browser.find_element_by_id('ap_phone_number')
      if "error" in mobile_number.get_attribute('outerHTML'):
         #get the colour and storing in the variable called obtained colour
         obtained_color = mobile_number.value_of_css_property('border-bottom-color')
         logging.info("get the colour and storing in the variable called obtained colour")
         if not self.check_color(obtained_color, "rgba(221, 0, 0, 1)"):
            print(f"expected color is {EXPECTED_COLOR} and got {obtained_color}")
         else:
            print("please provide valid mobile number")
            logging.info("please provide the valid mobile number")
      #password is not provided in the sign up page
      password = self.browser.find_element_by_id('ap_password')
      if "error" in password.get_attribute('outerHTML'):
         #get the colour and storing in the variable called obtained colour
         obtained_color = password.value_of_css_property('border-bottom-color')
         logging.info("get the colour and stiring in the variable called obtained colour")
         #checking the condition whether the obtained colour is equal or not
         if not self.check_color(obtained_color, "rgba(221, 0, 0, 1)"):
            print(f"expected color is {EXPECTED_COLOR} and got {obtained_color}")
         else:
            print("please provide correct passwords")

      error_messages = ["At least 3 characters",
                        "Invalid Email", "At least 6 characters"]
      message_body_html_elements = self.browser.find_elements_by_class_name('msg-body')
      for msg in message_body_html_elements:
         error_msg = msg.get_attribute('innerHTML').split("span")[1][1:-2]
         if error_msg not in error_messages:
            print(f"{msg.get_attribute('outerHTML')} is missing error message")
      return obtained_color
      self.close_browser()

#############################################################################################

   #This method is used to store the password successfully
   def password(self):
      with open("password.txt","r") as fr:
         password=fr.read()
         #res=fr.readlines()
      return password
   #This method is used to sign in the user in the amazon
   def signin(self):
      firstmenu=self.browser.find_element_by_xpath('//*[@id="nav-link-accountList-nav-line-1"]')
      firstmenu.click()
      logging.info("successfully clicked on sign in button")
      time.sleep(3)
      email_id="prathyusharaju223@gmail.com"
      #it fills the email_id
      element = self.browser.find_element_by_name("email")
      element.send_keys(email_id)
      logging.info("successfully fills email_id")
      #it clicks on continue button
      element = self.browser.find_element_by_id("continue")
      element.click()
      logging.info("successfully clicked on continue button")
      #it fills the password
      element = self.browser.find_element_by_name("password")
      element.send_keys(self.password())
      logging.info("successfully fills password")
      #it clicks on submit button
      element = self.browser.find_element_by_id("signInSubmit")
      element.click()
      logging.info("successfully clicked on submit button")
      #it close the browser
      self.browser.quit()
      logging.info("successfully close the chrome browser")
      return "user sign in done successfully"
   
#############################################################################################

   #This method is used to change the password 
   def forgot_password(self):
      #it clicks on sign in button
      firstmenu=self.browser.find_element_by_xpath('//*[@id="nav-link-accountList-nav-line-1"]')
      firstmenu.click()
      logging.info("successfully clicked on sign in button")
      #it fills the email_id in sign in page
      element = self.browser.find_element_by_name("email")
      element.clear()
      element.send_keys("prathyusharaju223@gmail.com")
      logging.info("it fills the emailid successfully")
      #it clicks on continue button in sign in page
      element = self.browser.find_element_by_id("continue")
      element.click()
      logging.info("successfully clicked on continue button")
      time.sleep(1)
      #it clicks on forgot_password button in sign page
      element=self.browser.find_element_by_xpath('//*[@id="auth-fpp-link-bottom"]')
      element.click()
      logging.info("successfully clicked on forgot password button")
      #it clicks on continue button in sign in page
      element = self.browser.find_element_by_id("continue")
      element.click()
      time.sleep(50)
      new_password="prathyusha@99"
      confirm_password="prathyusha@99"
      #it fills the new_password in sign in page
      element = self.browser.find_element_by_name("password")
      element.clear()
      element.send_keys(new_password)
      logging.info("it fills the new password successfully")
      #it fills the confirm_password in sign in page
      element = self.browser.find_element_by_name("passwordCheck")
      element.clear()
      element.send_keys(confirm_password)
      logging.info("it fills the confirm password successfully")
      #it clicks on continue button
      element = self.browser.find_element_by_id("continue")
      element.click()
      logging.info("successfully clicked on continue button")
      if new_password==confirm_password:
         return confirm_password
      else:
         return "some mismatch occurs"
      self.browser.quit()

#############################################################################################

   #This method is used to make the user to be keepme signed in
   def keep_signin(self):
      #it clicks on sign in page
      firstmenu=self.browser.find_element_by_xpath('//*[@id="nav-link-accountList-nav-line-1"]')
      firstmenu.click()
      logging.info("successfully clicked on sign in button")
      #it fill the email_id in the sign in page
      element = self.browser.find_element_by_name("email")
      element.clear()
      element.send_keys("prathyusharaju223@gmail.com")
      logging.info("it fills the email successfully")
      #it clicks on continue button
      element = self.browser.find_element_by_id("continue")
      element.click()
      logging.info("successfully clicked on continue button ")
      #it clicks on keepme sign in radio button in sign in page
      element=self.browser.find_element_by_xpath('//*[@id="authportal-main-section"]/div[2]/div[1]/div/div/form/div/div[2]/div/div/label/div/label/span')
      element.click()
      logging.info("successfully clicked on keepme signed in")
      #it fills the password in the sign in page
      element = self.browser.find_element_by_name("password")
      element.send_keys(self.password())
      logging.info("it fills the password successfully")
      #it clicks on submit button
      element = self.browser.find_element_by_id("signInSubmit")
      element.click()
      logging.info("sucessfully clicked on submit button")
      #it close the browser
      self.browser.quit()
      logging.info("successfully close the browser")
      return "keep me signed in done successfully"

#############################################################################################

   #This method is used to check if invaild username is provided
   def invalid_username(self):
      #it clicks on signin page
      firstmenu=self.browser.find_element_by_xpath('//*[@id="nav-link-accountList-nav-line-1"]')
      firstmenu.click()
      logging.info("successfully clicked on sign in button")
      time.sleep(3)
      email_id="prathyusharaju223#gmail.com"
      #it fills the invalid email id in signin page
      element = self.browser.find_element_by_name("email")
      element.send_keys(email_id)
      logging.info("it fills the email_id successfully")
      #it clicks on the continue button in signin page
      element = self.browser.find_element_by_id("continue")
      element.click()
      logging.info("successfully clicked on continue button")
      self.browser.quit()
      return "we cant find the account with that email address"

#############################################################################################

   #This method is used when invalid password is provided
   def invalid_password(self):
      #it clicks on sign in page 
      firstmenu=self.browser.find_element_by_xpath('//*[@id="nav-link-accountList-nav-line-1"]')
      firstmenu.click()
      logging.info("successfully clicked on sign in button")
      time.sleep(3)
      #it fills the correct emailid in the signin page 
      email_id="prathyusharaju223@gmail.com"
      element = self.browser.find_element_by_name("email")
      element.send_keys(email_id)
      logging.info("it fills the email_id successfully")
      #it clicks on continue button
      element = self.browser.find_element_by_id("continue")
      element.click()
      logging.info("successfully clicked on signin button")
      #it fills the invaild password in the signin page
      element = self.browser.find_element_by_name("password")
      element.send_keys("prathyusha")
      logging.info("it fills the password successfully ")
      #it clicks on submit button
      element = self.browser.find_element_by_id("signInSubmit")
      element.click()
      logging.info("successfully clicked on submit button")
      #it close the browser
      self.browser.quit()
      return "invalid password"

#############################################################################################

   # it checks the colour
   def check_color(self, color, orginal_color):
      return color == orginal_color

#############################################################################################

   #it close the browser
   def close_browser(self):
      self.browser.close()

############# Script Details #################################################################

# Script Name            :  quicksort.py
# Script version         :  3.8.5
# Prepared By            :  Prathyusha.Konduru@infinite.com
# Created_date           :  09-06-21
# last_modification_date :  14-06-21

##############################################################################################


   