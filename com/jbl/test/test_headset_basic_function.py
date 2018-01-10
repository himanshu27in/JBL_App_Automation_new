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
from shutil import copyfile
#import os
from com.jbl.common_method import constants

class Headset_Basic_Function(unittest.TestCase):


#     os.chdir(constants.project_path)
#     logging.info(os.getcwd())
#     
#     #logmon_logging.txt path
#     logmon_logging_path = os.path.join(os.getcwd(),r'com\jbl\\third_party_app\logmon_logging.txt')
#     logging.info(logmon_logging_path + "-------logmon_logging.txt path")
#     
#     #failed log folder path
#     failed_log_folder = os.path.join(os.getcwd(),r'com\jbl\failed_log_file')
#     logging.info(failed_log_folder + r'\\test_02_send_pause_request_to_headset.txt')
    
    
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
        status = Logmon_Tool_Parser.compare_and_validate_functionality(logmonlogStringToCompare.a2dp_playing_log)
        if status == False:
            #copyfile(r'D:\Automation\Eclipse_workspace\JBL_python\com\jbl\third_party_app\logmon_logging.txt', r'D:\Automation\Android_Automation\Failed_logs\test_02_send_pause_request_to_headset.txt')
            copyfile(constants.logmon_logging_path,  constants.failed_log_folder + r'\\test_01_send_play_request_to_headset.txt')
            assert status
        else:
            assert status 
          
          
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
        sleep(1)
        #self.driver.implicitly_wait(2)
        Logmon_Tool_Parser.capture_logmon_log_and_save_it()
          
        Logmon_Tool_Parser.click_enableButton_logmon_tool()
        Logmon_Tool_Parser.click_enableButton_logmon_tool()
          

        #path = os.path.join(os.path.dirname(__file__), 'logmon_logging.txt')
        
        status = Logmon_Tool_Parser.compare_and_validate_functionality(logmonlogStringToCompare.a2dp_paused_log)
        if status == False:
            copyfile(constants.logmon_logging_path,  constants.failed_log_folder + r'\\test_02_send_pause_request_to_headset.txt')
            assert status
        else:
            assert status 

          
    def test_03_send_ambientaware_change_request(self):
        logging.info("Executing test_03_send_ambientaware_change_request")
           
        Logmon_Tool_Parser.click_clearButton_logmon_tool()
        sleep(2)
        #Enable ANC for AA
        hcb.headphone_anc_on_button(self)
        sleep(3)
           
        hcb.headphone_smart_button_press_once(self)
        sleep(2) 
        #call enable function twice to get log in logmon tool -some issue with logmon tool
        Logmon_Tool_Parser.click_enableButton_logmon_tool()
        Logmon_Tool_Parser.click_enableButton_logmon_tool()
           
        #self.driver.implicitly_wait(2)
        Logmon_Tool_Parser.capture_logmon_log_and_save_it()
           
        Logmon_Tool_Parser.click_enableButton_logmon_tool()
        Logmon_Tool_Parser.click_enableButton_logmon_tool()
           
        status = Logmon_Tool_Parser.compare_and_validate_functionality(logmonlogStringToCompare.aa_off_log) | Logmon_Tool_Parser.compare_and_validate_functionality(logmonlogStringToCompare.aa_low_log) | Logmon_Tool_Parser.compare_and_validate_functionality(logmonlogStringToCompare.aa_high_log)

        if status == False:
            copyfile(constants.logmon_logging_path,  constants.failed_log_folder + r'\\test_03_send_ambientaware_change_request.txt')
            assert status
        else:
            assert status        
          
    def test_04_validate_min_volume(self):
        logging.info("test_07_validate_min_volume")  
           
        Logmon_Tool_Parser.click_clearButton_logmon_tool()
           
        hcb.headphone_set_min_volume(self)
        sleep(3) 
        #call enable function twice to get log in logmon tool -some issue with logmon tool
        Logmon_Tool_Parser.click_enableButton_logmon_tool()
        Logmon_Tool_Parser.click_enableButton_logmon_tool()
        sleep(1)
        #self.driver.implicitly_wait(2)
        Logmon_Tool_Parser.capture_logmon_log_and_save_it()
           
        Logmon_Tool_Parser.click_enableButton_logmon_tool()
        Logmon_Tool_Parser.click_enableButton_logmon_tool()
           
        status = Logmon_Tool_Parser.compare_and_validate_functionality(logmonlogStringToCompare.min_volume_down_log) 

        if status == False:
            copyfile(constants.logmon_logging_path,  constants.failed_log_folder + r'\\test_04_validate_min_volume.txt')
            assert status
        else:
            assert status 
     
    def test_05_validate_max_volume(self):
        logging.info("Executing test_06_validate_max_volume")  
             
        Logmon_Tool_Parser.click_clearButton_logmon_tool()
             
        hcb.headphone_set_max_volume(self)
        sleep(3)
            
        #call enable function twice to get log in logmon tool -some issue with logmon tool
        Logmon_Tool_Parser.click_enableButton_logmon_tool()
        Logmon_Tool_Parser.click_enableButton_logmon_tool()
        sleep(1)
        #self.driver.implicitly_wait(2)
        Logmon_Tool_Parser.capture_logmon_log_and_save_it()
            
        Logmon_Tool_Parser.click_enableButton_logmon_tool()
        Logmon_Tool_Parser.click_enableButton_logmon_tool()
            
        status = Logmon_Tool_Parser.compare_and_validate_functionality(logmonlogStringToCompare.max_volume_up_log) 

        if status == False:
            copyfile(constants.logmon_logging_path,  constants.failed_log_folder + r'\\test_05_validate_max_volume.txt')
            assert status
        else:
            assert status 
     
            
     
    def test_06_send_volume_down_request(self):
        logging.info("Executing test_05_send_volume_down_request")  
             
        Logmon_Tool_Parser.click_clearButton_logmon_tool()
             
        hcb.headphone_volume_down_button(self)
        sleep(1)
        hcb.headphone_volume_down_button(self)
        #call enable function twice to get log in logmon tool -some issue with logmon tool
        Logmon_Tool_Parser.click_enableButton_logmon_tool()
        Logmon_Tool_Parser.click_enableButton_logmon_tool()
        sleep(1)
        #self.driver.implicitly_wait(2)
        Logmon_Tool_Parser.capture_logmon_log_and_save_it()
            
        Logmon_Tool_Parser.click_enableButton_logmon_tool()
        Logmon_Tool_Parser.click_enableButton_logmon_tool()
            
        status = Logmon_Tool_Parser.compare_and_validate_functionality(logmonlogStringToCompare.volume_low_log)  

        if status == False:
            copyfile(constants.logmon_logging_path,  constants.failed_log_folder + r'\\test_06_send_volume_down_request.txt')
            assert status
        else:
            assert status 
     
         
          
    def test_07_send_volume_up_request(self):
        logging.info("Executing test_04_send_volume_up_request")  
             
        Logmon_Tool_Parser.click_clearButton_logmon_tool()
        sleep(1)
            
        hcb.headphone_volume_up_button(self)
        sleep(1)
        hcb.headphone_volume_up_button(self)
        #call enable function twice to get log in logmon tool -some issue with logmon tool
        Logmon_Tool_Parser.click_enableButton_logmon_tool()
        Logmon_Tool_Parser.click_enableButton_logmon_tool()
        sleep(1)
   
        #self.driver.implicitly_wait(2)
        Logmon_Tool_Parser.capture_logmon_log_and_save_it()
            
        Logmon_Tool_Parser.click_enableButton_logmon_tool()
        Logmon_Tool_Parser.click_enableButton_logmon_tool()
            
        status = Logmon_Tool_Parser.compare_and_validate_functionality(logmonlogStringToCompare.volume_up_log)

        if status == False:
            copyfile(constants.logmon_logging_path,  constants.failed_log_folder + r'\\test_07_send_volume_up_request.txt')
            assert status
        else:
            assert status 
     
 
      
    def test_08_send_anc_on_request(self):
        logging.info("Executing test_08_send_anc_on_request")  
            
        Logmon_Tool_Parser.click_clearButton_logmon_tool()
        sleep(1)
           
        hcb.headphone_anc_off_button(self)
        Logmon_Tool_Parser.click_clearButton_logmon_tool()
 
        sleep(2)
        hcb.headphone_anc_on_button(self)
        sleep(3)
        #call enable function twice to get log in logmon tool -some issue with logmon tool
        Logmon_Tool_Parser.click_enableButton_logmon_tool()
        Logmon_Tool_Parser.click_enableButton_logmon_tool()
        sleep(1)
  
        #self.driver.implicitly_wait(2)
        Logmon_Tool_Parser.capture_logmon_log_and_save_it()
           
        Logmon_Tool_Parser.click_enableButton_logmon_tool()
        Logmon_Tool_Parser.click_enableButton_logmon_tool()
           
        status = Logmon_Tool_Parser.compare_and_validate_functionality(logmonlogStringToCompare.anc_on_log)   

        if status == False:
            copyfile(constants.logmon_logging_path,  constants.failed_log_folder + r'\\test_08_send_anc_on_request.txt')
            assert status
        else:
            assert status 
     
     
    def test_09_send_anc_off_request(self):
        logging.info("Executing test_09_send_anc_off_request")  
            
        Logmon_Tool_Parser.click_clearButton_logmon_tool()
        sleep(1)
           
        hcb.headphone_anc_on_button(self)
        Logmon_Tool_Parser.click_clearButton_logmon_tool()
 
        sleep(2)
        hcb.headphone_anc_off_button(self)
        sleep(3)
        #call enable function twice to get log in logmon tool -some issue with logmon tool
        Logmon_Tool_Parser.click_enableButton_logmon_tool()
        Logmon_Tool_Parser.click_enableButton_logmon_tool()
        sleep(1)
  
        #self.driver.implicitly_wait(2)
        Logmon_Tool_Parser.capture_logmon_log_and_save_it()
           
        Logmon_Tool_Parser.click_enableButton_logmon_tool()
        Logmon_Tool_Parser.click_enableButton_logmon_tool()
           
        status = Logmon_Tool_Parser.compare_and_validate_functionality(logmonlogStringToCompare.anc_off_log)   

        if status == False:
            copyfile(constants.logmon_logging_path,  constants.failed_log_folder + r'\\test_09_send_anc_off_request.txt')
            assert status
        else:
            assert status 