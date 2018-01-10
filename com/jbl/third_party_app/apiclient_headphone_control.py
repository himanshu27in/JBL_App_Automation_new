'''
Created on Oct 24, 2017

@author: hkumar04
'''

from com.jbl.common_method import constants
import os
from __builtin__ import staticmethod
from time import sleep
class HeadsetControlButton(object):
    '''
    This class is used to control the headset button functionality like play pause and others.
    Different function will be defined within this class for different for headphone button
    apilient.exe provided by Avnera is used here to send command to headphone
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
    @staticmethod
    def headPhone_Play_Button(self):
        os.system(constants.headphone_play_button)

    @staticmethod
    def headPhone_Pause_Button(self):
        os.system(constants.headphone_pause_button)

    @staticmethod        
    def headPhone_Pairing_request_Button(self):
        os.system(constants.headphone_pairing_request_button)
        
    @staticmethod
    def headphone_smart_button_press_once(self):
        os.system(constants.headphone_smart_button)
    
    @staticmethod
    def headphone_volume_up_button(self):
        os.system(constants.headphone_volumeUp_button)
        
    @staticmethod
    def headphone_volume_down_button(self):
        os.system(constants.headphone_volumeDown_button)   
        
    @staticmethod
    def headphone_set_max_volume(self):
        for _volume in range(0,17):   #_variable name is used if it is unused
            os.system(constants.headphone_volumeUp_button)
            sleep(1)
            
    @staticmethod
    def headphone_set_min_volume(self):
        for _volume in range(0,17):
            os.system(constants.headphone_volumeDown_button)
            sleep(1)
    
    @staticmethod
    def headphone_anc_on_button(self):
        os.system(constants.headphone_volumeUp_smart_button)
        
    @staticmethod
    def headphone_anc_off_button(self):
        os.system(constants.headphone_volumeDown_smart_button)
        
    @staticmethod
    def headphone_factory_reset_button(self):
        os.system(constants.headphone_volumeUp_volumeDown_button)