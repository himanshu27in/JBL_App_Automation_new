'''
Created on Sep 7, 2017

@author: hkumar04
'''
import unittest


# app first page
skip_button = "jbl.stc.com:id/skipButton"
setting_button = "jbl.stc.com:id/leftHeaderBtn"
truenote_button = "jbl.stc.com:id/rightBtnText"
anc_button = "jbl.stc.com:id/noiseCancelButton"
battery_percent = "jbl.stc.com:id/txtBattery"

#programmable smart button
ambient_aware = "jbl.stc.com:id/ambientLayout"


# Setting screen page

device_name = "jbl.stc.com:id/deviceName"
device_id = "jbl.stc.com:id/deviceId"
update_device = "jbl.stc.com:id/text_updateDevice"
smart_button = "jbl.stc.com:id/text_smartButton"
auto_off_button = "jbl.stc.com:id/text_autoOff"
voice_prompt_button = "jbl.stc.com:id/toggleVoicePrompt"
app_version = "jbl.stc.com:id/appVersion"





class common_function(unittest.TestCase):

    @staticmethod
    def skipSkin(self):
        return self.driver.find_element_by_id(skip_button)
     
    @staticmethod   
    def settingButton(self):
        return self.driver.find_element_by_id(setting_button)
    
    @staticmethod
    def trueNoteButton(self):
        return self.driver.find_element_by_id(truenote_button)
    
    @staticmethod
    def ancButton(self):
        return self.driver.find_element_by_id(anc_button)
    
    @staticmethod
    def ambientawareButton(self):
        return self.driver.find_element_by_id(ambient_aware)
    
    @staticmethod
    def programmableSmartButton(self):
        return self.driver.find_element_by_id(smart_button)
    
    #navigation function to setting screen
    @staticmethod
    def navigateToSettingPage(self):
        self.settingButton().click()
        
    
    
