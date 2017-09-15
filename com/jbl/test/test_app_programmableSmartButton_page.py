'''
Created on Sep 15, 2017

@author: hkumar04
'''
#import unittest
from com.jbl.config import setupConfig
from com.jbl.common_method import AppPrelaunchPage as app
from com.jbl.common_method import AppSettingPage as asp
from com.jbl.common_method import AppLaunchPage as alp
from com.jbl.common_method import AppProgrammableSmartButtonPage as absbp
#from com.jbl.common_method.commonMethod import skipButton
from ptr import null


class Test_appProgrammableSmartButton(setupConfig):


        
    def test_01_ambientaware_setting(self):
          
        self.driver.implicitly_wait(14000)
        if app.skipSkin(self) != null:
            app.skipSkin(self).click()
          
        setting_btn = alp.settingButton(self)
        setting_btn.click()
         
        smart_btn = asp.programmableSmartButton(self)
        smart_btn.click()
        
        aa_button = absbp.ambientawareButton(self)
        aa_button.click()
#         print "AA button clicked\n"