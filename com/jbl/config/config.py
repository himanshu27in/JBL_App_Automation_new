'''
Created on Sep 7, 2017

@author: hkumar04
'''
import unittest
from appium import webdriver

class setupConfig(unittest.TestCase):
    '''
    classdocs
    '''
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        #desired_caps['platformVersion'] = '7.1.1'
        desired_caps['deviceName'] = 'F8332'
        desired_caps['app'] = 'D://Automation//Android_Automation//JBL_APP_APK//7F72B000.apk'
        desired_caps['appPackage'] = 'jbl.stc.com'
        desired_caps['appActivity'] = 'jblcontroller.st.com.com.views.activities.DashboardHome'
        #desired_caps['appActivity'] = 'jblcontroller.st.com.com.views.activities.Splash'                           
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

    def tearDown(self):
        self.driver.quit()

#     def __init__(self, params):
#         '''
#         Constructor
#         '''
        