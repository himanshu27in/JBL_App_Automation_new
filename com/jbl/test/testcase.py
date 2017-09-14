'''
Created on Sep 1, 2017

@author: hkumar04
'''

import os
import unittest
from appium import webdriver
from com.jbl.config import setupConfig
from com.jbl.common_method import common_function as cf

class Test(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1.1'
        desired_caps['deviceName'] = 'F8332'
        desired_caps['app'] = 'D://Automation//Android_Automation//JBL_APP_APK//7F72B000.apk'
        desired_caps['appPackage'] = 'jbl.stc.com'
        desired_caps['appActivity'] = 'jblcontroller.st.com.com.views.activities.DashboardHome'
        #desired_caps['appActivity'] = 'jblcontroller.st.com.com.views.activities.Splash' 
        #                              
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
        
        #pass

    def tearDown(self):
        #self.driver.implicitly_wait(20)
        self.driver.quit()

    
#     def test_Connectmessgae(self):
#         connect_msg = self.driver.find_element_by_id("jbl.stc.com:id/txtConnectMessage")
#         #connect_msg = self.driver.find_element_by_android_uiautomator('new UiSelector().text("Please connect headphones.")')
#         self.driver.implicitly_wait(5)
#         self.assertTrue(connect_msg.is_displayed())

    def test_01_appLaunch(self):
        self.driver.implicitly_wait(14000)
        cf.skipSkin(self)     #class name is used to call skip function as it is a static method
        
#         demo_skip = self.driver.find_element_by_id("jbl.stc.com:id/skipButton")
#         demo_skip.click()
        
#         app_launch = self.driver.find_element_by_id("jbl.stc.com:id/txtConnectMessage")
#         self.assertTrue(app_launch.is_displayed())  
#         self.driver.quit()
     
#     def test_02_settingButton(self):
#         self.driver.implicitly_wait(14000)
#         setting_button = self.driver.find_element_by_id("jbl.stc.com:id/leftHeaderBtn")
#         setting_button.click()
        
#     def test_01_appLaunch(self):
#         self.driver.implicitly_wait(10000)
#         app_launch = self.driver.find_element_by_id("jbl.stc.com:id/txtConnectMessage")
#         #connect_msg = self.driver.find_element_by_android_uiautomator('new UiSelector().text("Please connect headphones.")')
#         self.assertTrue(app_launch.is_displayed())  
#         
        
    def test_02_setlowAA(self):
        self.driver.implicitly_wait(140000)
        aa_low = self.driver.find_element_by_id("jbl.stc.com:id/lowTxt")
#         if aa_low.text == "LOW":
#             print "Already set t low"
#         else:
        aa_low.click()
        self.assertTrue("It is not set to low", aa_low.is_displayed())
   

    #def test_02_setting_displayed(self):
        

#     def test_appLaucnh_withoutConnection(self):
#         app_launch = self.driver.find_element_by_id("jbl.stc.com:id/txtConnectMessage")
#         self.assertTrue(app_launch.is_displayed())


    #def testName(self):
     #   pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    #unittest.main()
    
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)