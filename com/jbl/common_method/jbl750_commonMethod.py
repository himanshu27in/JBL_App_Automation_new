'''
Created on Sep 7, 2017

@author: hkumar04
'''
import unittest
import constants

# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By

# class WaitForLaunch():
#     @staticmethod
#     def waitfor(self,element_id):
#         element_wait = WebDriverWait(self.driver,15)
#         #currently_waiting_for = element_wait.until(EC.element_located_to_be_selected(By.ID,element_id))
#         element_wait.until(EC.invisibility_of_element_located(element_id),"Element is found")


class AppPrelaunchPage(unittest.TestCase):

# This function will return skip button id
    @staticmethod
    def skipSkin(self):
        #WebDriverWait(self.driver,20).until(EC.element_located_to_be_selected(By.ID,constants.skip_button))
        return self.driver.find_element_by_id(constants.skip_button)


class AppLaunchPage(unittest.TestCase):

# This function will return setting button id     
    @staticmethod   
    def settingButton(self):
        return self.driver.find_element_by_id(constants.setting_button)

# This function will return Trunote text 
    @staticmethod
    def truNoteText(self):
        return self.driver.find_element_by_xpath("//android.widget.TextView[@text = 'TruNote']").text

# This function will return Trunote button id
    @staticmethod
    def trueNoteButton(self):
        return self.driver.find_element_by_id(constants.truenote_button)
    
# This function will return anc button id    
    @staticmethod
    def ancButton(self):
        return self.driver.find_element_by_id(constants.anc_button)
    

    
    
    
class AppSettingPage(unittest.TestCase):
     
    @staticmethod
    def programmableSmartButton(self):
        return self.driver.find_element_by_id(constants.smart_button)      
    
    #navigation function to setting screen
    
class AppProgrammableSmartButtonPage(unittest.TestCase):
    
    @staticmethod
    def ambientawareButton(self):
        return self.driver.find_element_by_id(constants.ambient_aware)
        
 
 
class AppNavigationPage(unittest.TestCase):   
    
    def navigateToSettingPage(self):
        self.settingButton().click()
        
    
    
