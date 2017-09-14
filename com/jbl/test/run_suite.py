'''
Created on Sep 11, 2017

@author: hkumar04
'''


import unittest

from com.jbl.test.test_appSetting import Test_appSetting
from com.jbl.test.test_app_launch_page import Test_launchApp

if __name__ == "__main__":
   
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_launchApp,Test_appSetting) 
    unittest.TextTestRunner(verbosity=2).run(suite)