'''
Created on Oct 9, 2017

@author: hkumar04
'''
import re
from com.jbl.config.config import setupConfig
from com.jbl.common_method import constants
import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from com.jbl.third_party_app.apiclient_headphone_control import HeadsetControlButton as hcb
from com.jbl.common_method import SonyXperiaNativeApp as SXNA
from time import sleep
import unittest
from appium.webdriver.common.touch_action import TouchAction

'''
This class is having all test cases related to bluetooth pairing,
bluetooth available devices, connecting and disconnecting via BT 

'''
class Bluetooth_Connection_Setting(setupConfig):

    def refresh_bluetooth_list(self):
        more_options = self.driver.find_element_by_accessibility_id("More options")
        more_options.click()
        self.driver.implicitly_wait(3000)
        
        refresh_button_list = self.driver.find_elements_by_id("android:id/title")
        
        for refresh_button in refresh_button_list:
            logging.info(refresh_button.text)
            if refresh_button.text == "Refresh":
                TouchAction().press(refresh_button).release()
                #to get all available devices
                sleep(3)
                assert True
    
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
                    sleep(3)
                    value = 0
                    logging.info('Headphone is connected with device')
                    break
                else:
                    flag = 'false'

            if flag == 'false':
                self.driver.swipe(800,1500,800,1300,200)
                counter=counter+1
                
        if counter>=5:
            logging.info(" Not able to find the Required Device name in phone BT window !!!!")
            assert False
        while counter <=5 and counter >0:
            self.driver.swipe(800,1300,800,1500,200)
            counter = counter-1

    
    def disconnect_headphone_via_bt(self): 
        bt_connection_status = self.driver.find_element_by_id("android:id/summary")
        connected_string = "Connected"
        connectedStringObj = re.search(connected_string, bt_connection_status.text, re.M | re.I)
        logging.info(connectedStringObj.group())
        flag = False
        if connectedStringObj.group() == connected_string:
            bt_connection_status.click()
            sleep(1)
        disconnect_string= self.driver.find_element_by_id("android:id/alertTitle").text
        if disconnect_string=="Disconnect?":
            self.driver.find_element_by_id("android:id/button1").click()
            self.driver.implicitly_wait(10000)
            logging.info("Headphone is disconnected from previously connected device !")
            flag = True
        else:
            logging.info("Not able to find the disconnect pop up message window ! or already disconnected")
            flag = False
        return flag

    def headphone_already_connected(self):
        bt_connection_status = self.driver.find_elements_by_class_name("android.widget.TextView")
        
        connected_to_headset = self.driver.find_element_by_id("android:id/title")
        
        flag = False
        for status in bt_connection_status:
            logging.info(status.text)
            logging.info(connected_to_headset.text)
            logging.info("==================")
            if status.text[:9] == "Connected" and connected_to_headset.text == constants.JBL_Everest_Elite_750NC:
                logging.info("Device is connected with JBL headphone")
                flag = True
                break
        return flag
        
    def connect_headphone_when_paired_and_poweredoff(self):

        bt_device_list=self.driver.find_element_by_id("android:id/title")
        headphoneObj = re.match(constants.JBL_Everest_Elite_750NC, bt_device_list.text, re.M | re.I)
        if headphoneObj:
            logging.info("Headphone available for connection is :  " + headphoneObj.group())
            bt_device_list.click()
            sleep(3)
            connection_verification = self.driver.find_element_by_id("android:id/summary").text
            connection_verification = connection_verification[:10]
            if connection_verification == "Connecting" or connection_verification == None:
                logging.info("Headphone is powered off. Please switch it ON or taking long time to connect...")
                return True
        else:
            logging.info("Headphone is not paired with device")
            return False
        
    def unpair_connected_device(self):
        bt_setting_button = self.driver.find_element_by_id("com.android.settings:id/deviceDetails")
        bt_setting_button.click()
        product_under_test = self.driver.find_element_by_id("com.android.settings:id/name")
        flag = False
        if product_under_test.text == constants.JBL_Everest_Elite_750NC:
            self.driver.find_element_by_id("android:id/button3").click()
            self.driver.implicitly_wait(10000)
            logging.info("Headphone is unpaired with device !")
            flag = True     
         
#         bt_available_list = self.driver.find_elements_by_class_name("android.widget.TextView")
#         flag = False
#         for bt_list in bt_available_list:
#             if bt_list.text == "Paired devices" and product_under_test.text == constants.JBL_Everest_Elite_750NC:
#                 logging.info("Headphone is not unpaired properly")
#                 flag = False
#                 break
#             else:
#                 logging.info("Headphone is unpaired with device !")
#                 flag = True
        return flag             

#     @unittest.skip("test_01_connect_headphone_via_BT_in_pairing_state")
    def test_01_connect_headphone_via_BT_in_pairing_state(self):
        logging.info("Executing test_01_connect_headphone_via_BT_in_pairing_state")
        # To open Bluetooth settings screen on mobile
        SXNA.launch_bt_setting_page(self)
        
        #put headphone in Bt pairing state, check for headphone name in BT window of phone. 
        hcb.headPhone_Pairing_request_Button(self)
        sleep(5)
        # Refresh BT list on phone
        self.refresh_bluetooth_list()
        
        #if found the BT name on phone then click on it else scroll the BT window screen check for headphone name
        # new list. 
        # connect headphone via BT 
        if self.headphone_already_connected() == False:
            self.connect_headphone_via_bt()
        else:
            logging.info("Headphone is not in pairing state,Pairing request failed ...")
            assert False
        # To check whether headphone is powered on or not
        connection_verification = self.driver.find_element_by_id("android:id/summary").text

        #waiting for Headphone to get connected with phone
        try:
            WebDriverWait(self.driver,10).until(EC.text_to_be_present_in_element((By.ID,'android:id/summary'),'Connected'))
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
            logging.info("Unable to connect via BT or not able to capture connected string")
            assert False

        
#     @unittest.skip("test_02_disconnect_already_connected_headphone")      
    def test_02_disconnect_already_connected_headphone(self):
        logging.info("Executing test_02_disconnect_already_connected_headphone")
        # To open Bluetooth settings screen on mobile
        SXNA.launch_bt_setting_page(self)
        
        #First check headphone is connected or not, if not connected then display the message as headphone is in BT disconnected mode. otherwise performing BT disconnect operation
        # check whether device disconnected properly or not.
    
        if self.headphone_already_connected() == False :
            logging.info("Headphone is in BT disconnected mode, please connect the headphone via BT....!!!")
            self.connect_headphone_via_bt()
        else:
            self.disconnect_headphone_via_bt()
            self.driver.implicitly_wait(10000)
            if self.headphone_already_connected() == False:
                logging.info("device proper disconnected from previously connected device .....")
                assert True
            else:
                logging.info(" device still in connected state after BT disconnect operation ")
                assert False



#     @unittest.skip("test_03_reboot_headphone_to_validate_connected_to_previously_connected_device")  
    def test_03_reboot_headphone_to_validate_connected_to_previously_connected_device(self):
        
        logging.info("Executing test_03_reboot_headphone_to_validate_connected_to_previously_connected_device")
        # To open Bluetooth settings screen on mobile        
        SXNA.launch_bt_setting_page(self)

        #Headphone is already paired and connected to any mobile
        check_connected = self.headphone_already_connected()
        if check_connected == True:
            logging.info("Headphone already connected")
        else:
            self.connect_headphone_via_bt()
        
        #Power off and power ON headphone
        
        # validate it is connected to previously connected device 
        
        check_connected = self.headphone_already_connected()
        assert check_connected        

#     @unittest.skip("test_04_unpair_connected_device")      
    def test_04_unpair_connected_device(self):
        logging.info("Executing test_04_unpair_connected_device")
        # To open Bluetooth settings screen on mobile
        SXNA.launch_bt_setting_page(self)

        #Headphone is already paired and connected to any mobile
        check_connected = self.headphone_already_connected()
        if check_connected == True:
            logging.info("Headphone already connected")
            # unpair it
            unpair_status = self.unpair_connected_device()
            assert unpair_status
        else:
            logging.info("Headphone is already unpaired with the device")
            assert False
            
#     @unittest.skip("test_05_send_pairing_request_and_connect")             
    def test_05_send_pairing_request_and_connect(self):
        logging.info("Executing test_05_send_pairing_request_and_connect")
        # To open Bluetooth settings screen on mobile
        SXNA.launch_bt_setting_page(self)
    
        #send pairing request
        hcb.headPhone_Pairing_request_Button(self)
        
        # Refresh BT list on phone
        self.refresh_bluetooth_list()
        
        if self.headphone_already_connected() == False:
            self.connect_headphone_via_bt()
        else:
            logging.info("Headphone is not in pairing state,Pairing request failed ...")
            assert False
        