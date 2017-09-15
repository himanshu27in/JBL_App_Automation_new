'''
Created on Sep 7, 2017

@author: hkumar04
'''
import unittest


# app first page
skip_button = "jbl.stc.com:id/skipButton"
setting_button = "jbl.stc.com:id/leftHeaderBtn"
truenote_button = "jbl.stc.com:id/rightBtnText"
battery_percent = "jbl.stc.com:id/txtBattery"
right_arrow = "jbl.stc.com:id/rightArrow"
eq_setting_value = "jbl.stc.com:id/txtCurrentEq"
anc_button = "jbl.stc.com:id/noiseCancelButton"

# Setting screen page

left_header_button = "jbl.stc.com:id/leftHeaderBtn"
setting_title_text = "jbl.stc.com:id/barTitleText"
device_name = "jbl.stc.com:id/deviceName"
device_id = "jbl.stc.com:id/deviceId"
update_device = "jbl.stc.com:id/text_updateDevice"
smart_button = "jbl.stc.com:id/text_smartButton"
auto_off_text = "jbl.stc.com:id/text_autoOff"
voice_prompt_text = "jbl.stc.com:id/text_voicePrompt"
auto_off_button = "jbl.stc.com:id/toggleautoOff"
voice_prompt_button = "jbl.stc.com:id/toggleVoicePrompt"
app_version = "jbl.stc.com:id/appVersion"

#programmable smart button
ambient_aware = "jbl.stc.com:id/ambientLayout"
noise_cancellation_button = "jbl.stc.com:id/noiceCancelling"
programmable_button_title_text = "jbl.stc.com:id/barTitleText"
left_header_button = "jbl.stc.com:id/leftHeaderBtn"


class AppPrelaunchPage(unittest.TestCase):

    @staticmethod
    def skipSkin(self):
        return self.driver.find_element_by_id(skip_button)


class AppLaunchPage(unittest.TestCase):

     
    @staticmethod   
    def settingButton(self):
        return self.driver.find_element_by_id(setting_button)
    
    @staticmethod
    def trueNoteButton(self):
        return self.driver.find_element_by_id(truenote_button)
    
    @staticmethod
    def ancButton(self):
        return self.driver.find_element_by_id(anc_button)
    

    
    
    
class AppSettingPage(unittest.TestCase):
     
    @staticmethod
    def programmableSmartButton(self):
        return self.driver.find_element_by_id(smart_button)      
    
    #navigation function to setting screen

    
class AppProgrammableSmartButtonPage(unittest.TestCase):
    
    @staticmethod
    def ambientawareButton(self):
        return self.driver.find_element_by_id(ambient_aware)
        
 
 
class AppNavigationPage(unittest.TestCase):   

    @staticmethod
    def navigateToSettingPage(self):
        self.settingButton().click()
        
    
    
