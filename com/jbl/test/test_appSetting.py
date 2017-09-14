'''
Created on Sep 11, 2017

@author: hkumar04
'''
#import unittest
from com.jbl.config import setupConfig
from com.jbl.common_method import common_function as cf
#from com.jbl.common_method.commonMethod import skipButton
from ptr import null


class Test_appSetting(setupConfig):


    def test_01_ancsetting(self):
        
        self.driver.implicitly_wait(14000)
        if cf.skipSkin(self) != null:
            cf.skipSkin(self).click()
         
        
        anc_button = cf.ancButton(self)
        anc_button.click()
#         print "ANC button clicked\n"
        
    def test_02_ambientaware_setting(self):
          
        self.driver.implicitly_wait(14000)
        if cf.skipSkin(self) != null:
            cf.skipSkin(self).click()
          
        setting_btn = cf.settingButton(self)
        setting_btn.click()
         
        smart_btn = cf.programmableSmartButton(self)
        smart_btn.click()
        
        aa_button = cf.ambientawareButton(self)
        aa_button.click()
#         print "AA button clicked\n"