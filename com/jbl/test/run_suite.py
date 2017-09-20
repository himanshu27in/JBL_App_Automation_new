'''
Created on Sep 11, 2017

@author: hkumar04
'''


# import unittest
#from com.jbl.test.test_appSetting import Test_appSetting
# from com.jbl.test.test_app_launch_page import Test_launchApp
# from com.jbl.test.test_app_programmableSmartButton_page import Test_appProgrammableSmartButton

# if __name__ == "__main__":
#    
#     suite = unittest.TestLoader().loadTestsFromTestCase(Test_launchApp,Test_appSetting,Test_appProgrammableSmartButton) 
#     unittest.TextTestRunner(verbosity=2).run(suite)
    
    

######## to run all test cases

# if __name__ == '__main__':
#     test_classes_to_run = [Test_appSetting, Test_launchApp,Test_appProgrammableSmartButton]
#    
#     loader = unittest.TestLoader()
#    
#     suites_list = []
#     for test_class in test_classes_to_run:
#         suite = loader.loadTestsFromTestCase(test_class)
#         suites_list.append(suite)
#    
#     big_suite = unittest.TestSuite(suites_list)
#    
#     runner = unittest.TextTestRunner()
#     results = runner.run(big_suite)



   
import unittest
import test_appSetting
import test_app_launch_page
import test_app_programmableSmartButton_page
#import HtmlTestRunner
from HtmlTestRunner import HTMLTestRunner
import logging

   
#####  Running test case- by using below run method each test result will be displayed
   
    #initialize the test suite
def main():   
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
          
        # add tests to test suite
          
    suite.addTest(loader.loadTestsFromModule(test_appSetting))
    suite.addTest(loader.loadTestsFromModule(test_app_launch_page))
    suite.addTest(loader.loadTestsFromModule(test_app_programmableSmartButton_page))
        
    # runner = unittest.TextTestRunner(verbosity=2)
    # result = runner.run(suite)
    logging.debug("This will be printed 1============================")  
    
    
    logging.debug("This will be printed 2============================")   
    #unittest.TextTestRunner(verbosity=2).run(suite)
    #outfile = open('JBL_Test_Report')
    #runner = HTMLTestRunner(output='D:\\Automation\\Eclipse_workspace\\JBL_python\\com\\jbl\\test\\')
    runner = HTMLTestRunner(output='JBL_Test_Report')
    logging.debug("This will be printed 3============================")  
    runner.run(suite)
    logging.debug("This will be printed 4============================")  

if __name__ == "__main__":
    main()