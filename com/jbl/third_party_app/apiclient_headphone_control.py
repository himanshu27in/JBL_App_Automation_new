'''
Created on Oct 24, 2017

@author: hkumar04
'''

from com.jbl.common_method import constants
import os
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