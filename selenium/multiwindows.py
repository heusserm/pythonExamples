
#To get this to run:
# Use python 2.7 
# (To find your python version, use python -V from the command line.) 
#
# pip install -U seleniun
#
#
#You'll also need a Sauce Labs Account
#Get you free trial at https://app.saucelabs.com/
#
#
#
# This code originally derived from https://gist.github.com/santiycr/511658
# but adapted for selenium3 at the request of Sauce Labs.
#

import os
 
# Selenium 3.14+ doesn't enable certificate checking
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
  
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from threading import Thread
#from selenium import selenium
import time
try:
    import json
except ImportError:
    import simplejson as json

USERNAME = "YOUR_USERNAME_NOT_YOUR_EMAIL_ADDRESS"
ACCESS_KEY = "YOUR_ACCESS_KEY_GET_IT_IN_YOUR_PROFILE_SETTINGS"

def get_sauce_browser(os="Windows 2003", browser="firefox", version="."):
    
    desired_cap = {    
                'platform': "Mac OS X 10.12",
                'browserName': "chrome",
                 'version': "latest",
    }

    return webdriver.Remote(   
       command_executor='https://{}:{}@ondemand.saucelabs.com/wd/hub'.format(USERNAME, ACCESS_KEY),
       desired_capabilities=desired_cap)

b1 = get_sauce_browser(version="70")
b2 = get_sauce_browser(version="69")
b3 = get_sauce_browser(version="68")

browsers = [b1, b2, b3]
browsers_waiting = []

def get_browser_and_wait(browser, browser_num):
    print "starting browser %s" % browser_num
    browser.get("http://www.google.com")
    browsers_waiting.append(browser)
    print "browser %s ready" % browser_num
    while len(browsers_waiting) < len(browsers):
        print "browser %s sending heartbeat while waiting" % browser_num
        browser.get("https://saucelabs.com/")
        time.sleep(3)

thread_list = []
for i, browser in enumerate(browsers):
    t = Thread(target=get_browser_and_wait, args=[browser, i + 1])
    thread_list.append(t)
    t.start()

for t in thread_list:
    t.join()

print "all browsers ready"
for i, b in enumerate(browsers):
    title = b.title
    print "browser %s's title: %s" % (i + 1, title)
    b.quit()
