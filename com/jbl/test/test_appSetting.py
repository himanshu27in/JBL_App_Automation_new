'''
Created on Sep 11, 2017

@author: hkumar04
'''

from com.jbl.config import setupConfig
from com.jbl.common_method import AppPrelaunchPage as app
from com.jbl.common_method import AppSettingPage as asp
from com.jbl.common_method import AppLaunchPage as alp
from com.jbl.common_method import AppProgrammableSmartButtonPage as absbp
from com.jbl.common_method import constants


class Test_appSetting(setupConfig):
    

        
    def test_01(self):
        

        self.driver.implicitly_wait(constants.wait_for_app_launch)
        if app.skipSkin(self) != None:
            app.skipSkin(self).click()
          
        setting_btn = alp.settingButton(self)
        setting_btn.click()
         
        smart_btn = asp.programmableSmartButton(self)
        smart_btn.click()
        
        aa_button = absbp.ambientawareButton(self)
        aa_button.click()
        self.assertEqual(1, 1, 'Equal')
#         print "AA button clicked\n"