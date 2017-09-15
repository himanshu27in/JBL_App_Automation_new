'''
Created on Sep 11, 2017

@author: hkumar04
'''


import unittest
from com.jbl.test.test_appSetting import Test_appSetting
from com.jbl.test.test_app_launch_page import Test_launchApp
from com.jbl.test.test_app_programmableSmartButton_page import Test_appProgrammableSmartButton

if __name__ == "__main__":
   
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_launchApp,Test_appSetting,Test_appProgrammableSmartButton) 
    unittest.TextTestRunner(verbosity=2).run(suite)