'''
Created on Sep 4, 2017
@author: hkumar04
'''

#import unittest
from com.jbl.config import setupConfig
from com.jbl.common_method import common_function as cf
#from com.jbl.common_method.commonMethod import skipButton

#from com.jbl.test.test_appSetting import Test_appSetting
from ptr import null
import logging


class Test_launchApp(setupConfig):
    
    def test_01_appLaunch(self):
        self.driver.implicitly_wait(14000)
        skip_ele = cf.skipSkin(self)     #class name is used to call skipSkin function as it is a static method
        skip_ele.click()
#         print "skip button clicked\n"
#         logging.debug("passing---")
        logging.info("passed--------")
     
    def test_02_settingButton(self):
          
        self.driver.implicitly_wait(14000)
        if cf.skipSkin(self) != null:
            cf.skipSkin(self).click()
           
        setting_btn = cf.settingButton(self)
        setting_btn.click()
        
        
#         print "setting button clicked"
#         logging.debug("test_02_settingButton")


        #validate all Basic UI is displaying
    

# 
# if __name__ == "__main__":
#    
#     suite = unittest.TestLoader().loadTestsFromTestCase(Test_launchApp,Test_appSetting) 
#     unittest.TextTestRunner(verbosity=2).run(suite)