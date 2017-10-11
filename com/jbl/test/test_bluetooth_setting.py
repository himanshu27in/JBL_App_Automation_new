'''
Created on Oct 9, 2017

@author: hkumar04
'''
import os
import re
from com.jbl.config.config import setupConfig
from com.jbl.common_method import constants
import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


'''
This class is having all test cases related to bluetooth pairing,
bluetooth available devices, connecting and disconnecting via BT 

'''
class Bluetooth_Connection_Setting(setupConfig):
    
    def connect_headphone_via_bt(self):
        value = 1
        counter = 0
        while((value == 1) and (counter <5)):
            bt_device_list=self.driver.find_elements_by_id("android:id/title")
            logging.info(len(bt_device_list))
            flag = 'true'
            for device_name in bt_device_list:
                #logging.info(line)
                headphoneObj = re.match(constants.JBL_Everest_Elite_750NC, device_name.text, re.M | re.I)
                if headphoneObj:
                    logging.info("Headphone available for connection is :  " + headphoneObj.group())
                    device_name.click()
                    self.driver.implicitly_wait(10000)
                    value = 0
                    break
                else:
                    flag = 'false'

            if flag == 'false':
                self.driver.swipe(800,1500,800,1300,200)
                counter=counter+1
                
        if counter>=5:
            logging.info(" Not able to find the Required Device name in phone BT window !!!!")
            assert False

    
    def disconnect_headphone_via_bt(self): 
        bt_connection_status = self.driver.find_element_by_id("android:id/summary")
        connected_string = "Connected"
        connectedStringObj = re.search(connected_string, bt_connection_status.text, re.M | re.I)
        logging.info(connectedStringObj.group())
        
        if connectedStringObj.group() == connected_string:
            bt_connection_status.click()

        disconnect_string= self.driver.find_element_by_id("android:id/alertTitle").text
        if disconnect_string=="Disconnect?":
            self.driver.find_element_by_id("android:id/button1").click()
            self.driver.implicitly_wait(10000)
            logging.info("Headphone is disconnected from previously connected device !")
            assert True
        else:
            logging.info("Not able to find the disconnect pop up message window !")
            assert False

         


    def test_01_connect_headphone_via_BT_in_pairing_state(self):
        # To open Bluetooth settings screen on mobile
        self.driver.implicitly_wait(10000)
        # adb command for sony xperia
        os.system("adb shell am start -n com.android.settings/.bluetooth.BluetoothSettings")
        #adb command for LG G5
        #os.system("adb shell am start -n com.lge.bluetoothsetting/.LGBluetoothSettingActivity")
        #put headphone in Bt pairing state, check for headphone name in BT window of phone. 
        
        
        #if found the BT name on phone then click on it else scroll the BT window screen check for headphone name
        # new list.
        
        # connect headphone via BT 
        self.connect_headphone_via_bt()
       
        # To check whether headphone is powered on or not
        connection_verification = self.driver.find_element_by_id("android:id/summary").text
        #waiting for Headphone to get connected with phone
        try:
            WebDriverWait(self.driver,5).until(EC.text_to_be_present_in_element((By.ID,'android:id/summary'),'Connected'))
            logging.info("Headphone connected via BT... ")
        except TimeoutException:
            connection_verification = connection_verification[:10]
            if connection_verification == "Connecting":
                logging.info("Headphone is powered off. please switch it ON or taking long time to connect...")
                assert False
                
        # validating connected string on Phone Bluetooth setting window  
        check_string="Connected"
        searchObj = re.search(check_string, connection_verification, re.M | re.I)

        logging.info("Comparing 'Connected' string with : " + searchObj.group())
        if searchObj.group() == "Connected":
            assert True
            logging.info("Headphone is Connected to device via BT")
        else:
            logging.info("Unable to connect via BT")
            assert False
        logging.info("going to call disconnect")
        self.disconnect_headphone_via_bt()   
        
#     # this test is dependent on test 01         
#     def test_02_disconnect_already_connected_headphone(self):
#         # To open Bluetooth settings screen on mobile
#         self.driver.implicitly_wait(10000)
#         # adb command for sony xperia
#         os.system("adb shell am start -n com.android.settings/.bluetooth.BluetoothSettings")
#          
#          
#         connection_verification = self.driver.find_element_by_id("android:id/summary").text
#         if connection_verification == None:
#              
#              
#         
#         
#         
#         
#         
#         
#         # To check whether headphone is powered on or not
#         connection_verification = self.driver.find_element_by_id("android:id/summary").text
#         connection_verification = connection_verification[:10]
#         if connection_verification == "Connecting":
#             logging.info("Headphone is powered off. please switch it ON...")
#             assert False
#         #waiting for Headphone to get connected with phone
#         try:
#             WebDriverWait(self.driver,5).until(EC.text_to_be_present_in_element((By.ID,'android:id/summary'),'Connected'))
#             logging.info("Headphone connected via BT... ")
#         except TimeoutException:
#             logging.info("time ran out...")
#             assert False
#         # validating connected string on Phone Bluetooth setting window  
#         check_string="Connected"
#         searchObj = re.search(check_string, connection_verification, re.M | re.I)
#         
#         logging.info("Comparing 'Connected' string with : " + searchObj.group())
#         if searchObj.group() == "Connected":
#             assert True
#             logging.info("Headphone is Connected to device via BT")
#         else:
#             logging.info("Unable to connect via BT")
#             assert False







