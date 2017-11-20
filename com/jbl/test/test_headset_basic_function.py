'''
Created on Nov 15, 2017

@author: hkumar04
'''

import logging
from time import sleep
from com.jbl.third_party_app.apiclient_headphone_control import HeadsetControlButton as hcb

from com.jbl.third_party_app.logmon_log_capture_tool import Logmon_Tool_Parser
from com.jbl.common_method import logmonlogStringToCompare
import unittest


class Headset_Basic_Function(unittest.TestCase):

        
    def test_01_send_play_request_to_headset(self):
        logging.info("Executing test_01_send_play_request_to_headset")
    
        # open logmon and clear logmon log
         
        Logmon_Tool_Parser.click_clearButton_logmon_tool()
        #Logmon_Tool_Parser.click_readCodesButton_logmon_tool()          
        sleep(1)
        #self.driver.implicitly_wait(2)
        #send play command   
        hcb.headPhone_Play_Button(self)
        #call enable function twice to get log in logmon tool -some issue with logmon tool
        Logmon_Tool_Parser.click_enableButton_logmon_tool()
        Logmon_Tool_Parser.click_enableButton_logmon_tool()

        #self.driver.implicitly_wait(2)
        Logmon_Tool_Parser.capture_logmon_log_and_save_it()
        
        Logmon_Tool_Parser.click_enableButton_logmon_tool()
        Logmon_Tool_Parser.click_enableButton_logmon_tool()
        
        #play_log_list = ['AVRCP_PASS_THROUGH_ID_PLAY','A2DP_Playing','AUDIO_PLAYBACK']
        assert Logmon_Tool_Parser.compare_and_validate_functionality(logmonlogStringToCompare.a2dp_playing_log)
        # capture logmon log and save  it
        
        
    def test_02_send_pause_request_to_headset(self):
        logging.info("Executing test_02_send_pause_request_to_headset")
    
        # open logmon and clear logmon log
         
        Logmon_Tool_Parser.click_clearButton_logmon_tool()
        #Logmon_Tool_Parser.click_readCodesButton_logmon_tool()          
        sleep(1)
        #self.driver.implicitly_wait(2)
        #send play command   
        hcb.headPhone_Pause_Button(self)
        #call enable function twice to get log in logmon tool -some issue with logmon tool
        Logmon_Tool_Parser.click_enableButton_logmon_tool()
        Logmon_Tool_Parser.click_enableButton_logmon_tool()

        #self.driver.implicitly_wait(2)
        Logmon_Tool_Parser.capture_logmon_log_and_save_it()
        
        Logmon_Tool_Parser.click_enableButton_logmon_tool()
        Logmon_Tool_Parser.click_enableButton_logmon_tool()
        
        #play_log_list = ['AVRCP_PASS_THROUGH_ID_PLAY','A2DP_Playing','AUDIO_PLAYBACK']
        assert Logmon_Tool_Parser.compare_and_validate_functionality(logmonlogStringToCompare.a2dp_paused_log)
        # capture logmon log and save  it
        
    def test_03_send_ambientaware_change_request(self):
        logging.info("Executing test_03_send_ambientaware_change_request")
        
        Logmon_Tool_Parser.click_clearButton_logmon_tool()
        
        hcb.headphone_smart_button_press_once(self)
        
        #call enable function twice to get log in logmon tool -some issue with logmon tool
        Logmon_Tool_Parser.click_enableButton_logmon_tool()
        Logmon_Tool_Parser.click_enableButton_logmon_tool()
        
        #self.driver.implicitly_wait(2)
        Logmon_Tool_Parser.capture_logmon_log_and_save_it()
        
        Logmon_Tool_Parser.click_enableButton_logmon_tool()
        Logmon_Tool_Parser.click_enableButton_logmon_tool()
        
        assert Logmon_Tool_Parser.compare_and_validate_functionality(logmonlogStringToCompare.aa_off_log) | Logmon_Tool_Parser.compare_and_validate_functionality(logmonlogStringToCompare.aa_low_log) | Logmon_Tool_Parser.compare_and_validate_functionality(logmonlogStringToCompare.aa_high_log)
        
    def test_04_send_volume_up_request(self):
        logging.info("Executing test_04_send_volume_up_request")  
        
        Logmon_Tool_Parser.click_clearButton_logmon_tool()
        
        hcb.headphone_volume_up_button(self)
    