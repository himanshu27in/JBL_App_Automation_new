'''
Created on Sep 4, 2017
@author: hkumar04
'''

#import unittest
from com.jbl.config import setupConfig
from com.jbl.common_method import AppPrelaunchPage as app
from com.jbl.common_method import AppLaunchPage as alp
#from com.jbl.common_method.commonMethod import skipButton

#from com.jbl.test.test_appSetting import Test_appSetting
from ptr import null
#import logging
import unittest
import logging


class Test_launchApp(setupConfig):

# Test to verify skin is displayed while App launch
#    @unittest.skip("Test Skipped2")  
    def test_01_appLaunch(self):
        self.driver.implicitly_wait(14000)
        skip_ele = app.skipSkin(self)     #class name is used to call skipSkin function as it is a static method
        logging.debug("skip_ele.click() is called-----")
        skip_ele.click()
        logging.info("test_01_appLaunch is passed-----")
 
# Test to verify the setting button after App launch     
#     @unittest.skip("Test Skipped1")
    def test_02_settingButton(self):
 
        self.driver.implicitly_wait(14000)
        if app.skipSkin(self) != null:
            app.skipSkin(self).click()
            
        setting_btn = alp.settingButton(self)
        setting_btn.click()
       

# Test to verify the TruNote text after App launch
    def test_03_truNoteText(self):
        self.driver.implicitly_wait(14000)
        if app.skipSkin(self) != null:
            app.skipSkin(self).click()

        truNote_txt = alp.truNoteText(self)
        logging.info(truNote_txt + " will be printed")
        self.assertEqual("TruNote",truNote_txt,"TruNote text is not matching")   

 
#     @unittest.skip("Test Skipped2")    
    def test_04_ancsetting(self):
         
        self.driver.implicitly_wait(14000)
        if app.skipSkin(self) != null:
            app.skipSkin(self).click()
          
         
        anc_button = alp.ancButton(self)
        anc_button.click()
