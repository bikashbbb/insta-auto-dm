from telnetlib import EC

from selenium import webdriver
import csv
from pprint import pprint
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotInteractableException


class Login():

    def __init__(self, username, password,user_last_range, maximumuser, Message ):
        self.username = username
        self.password = password
        self.user_last_range = user_last_range
        self.maximumuser = maximumuser
        self.message = Message
        self.userlimit = 0
        self.limitcross = 60

    def directToAccount(self, usersid):
        self.driver.get('https://www.instagram.com/{}/'.format(usersid))
        self.driver.implicitly_wait(20)
        self.userlimit += 1

        if self.userlimit == self.limitcross:
            self.limitcross+=60
            print('**************** USER LIMIT EXCEED WAIT...................')
            time.sleep(1000)

        with open('lastuser.txt', 'w') as e:
            e.write(str(self.userlimit + self.user_last_range))
        # <<<<<<<<<<<<,IF STATEMENT AND REDIRETING TO SENT THE DESIRED MESSAGE

        try:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(6)
            htmlelement = self.driver.find_element_by_tag_name('html')
            htmlelement.send_keys(Keys.HOME)
            time.sleep(25)
            followbutton = self.driver.find_element_by_css_selector('._6VtSN')
            followbutton.click()
            time.sleep(6)
            messagebox = self.driver.find_element_by_css_selector('._8A5w5')
            messagebox.click()
            time.sleep(25)
            # <<<<<<<<<<<<< MESSENGING
            message_box = self.driver.find_element_by_css_selector('.focus-visible')
            message_box.send_keys('hey ! '+ str(usersid)+'\n'+ str(self.message))
            submit_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button')
            submit_button.click()
            time.sleep(6)



        except (NoSuchElementException , ElementClickInterceptedException,ElementNotInteractableException) as e:
            print('\n Next user ')


    # click and send

    def csvIntoList(self, user_last_range, maximumuser):
        time.sleep(2)
        with open('outputfile.csv', newline='') as file:
            reader = csv.reader(file)
            res = list(map(tuple, reader))
            usinglist = res[user_last_range:maximumuser]
        pprint('Username processing')
        # here we are gonna import all the necessary usernames

        # redirecting from here
        # bikash ko loop
        for user in usinglist:
            user = user[0]
            self.directToAccount(user)
        with open('history.csv','a') as p :
            p.write('from range ' + str(self.user_last_range) + ' to ' + str(self.maximumuser))
        print('\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< MISSION SUCESSFULL>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.')


    def directMessagePage(self, driver):
        # here we will go to direct message section by loging into the website
        self.driver = webdriver.Chrome(driver)
        startUrl = ('https://www.instagram.com/direct/inbox/')
        self.driver.get(startUrl)
        self.driver.implicitly_wait(20)
        # login
        username_Value = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_Value.send_keys(self.username)
        self.driver.implicitly_wait(2)
        password_field = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_field.send_keys(self.password)
        self.driver.implicitly_wait(2)
        password_field.submit()
        time.sleep(10)
        # <<<<<<<<<<<<<<<<<<<<<<<<<<<NOT NOW>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        time.sleep(3)
        self.driver.find_element_by_css_selector('.aOOlW.HoLwm').click()
        self.driver.implicitly_wait(16)
        self.csvIntoList(self.user_last_range, self.maximumuser)


obj = Login(input('enter your username mr.Bhatta : '),
            input('enter your password mr.Bhatta : '),int(input('Users last time range : ')),
            int(input('\nup the how much profile do you wanna message : ')

                ),
            input('\n what message do you want to send??? : ')
            )
obj.directMessagePage('C:\Program Files (x86)\chromedriver.exe')