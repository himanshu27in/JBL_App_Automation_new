'''
Created on Sep 26, 2017

@author: hkumar04
'''
import os
import logging

# app first page
skip_button = "jbl.stc.com:id/skipButton"
setting_button = "jbl.stc.com:id/leftHeaderBtn"
trunote_txt = "TruNote"
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


wait_for_app_launch = 15000

# Bluetooth Setting on native app

JBL_Everest_Elite_750NC = 'JBL Everest Elite 750NC'

# Avnera apiclient.exe path
#code part

# ButtonIdx_INVALID,      // INVALID BUTTON
#     ButtonIdx_MFB,          // BUTTON_IDX_MFB
#     ButtonIdx_SMART,        // BUTTON_IDX_SHAREME //Called SMART
#     ButtonIdx_VOLUP,        // BUTTON_IDX_VOLUME_UP
#     ButtonIdx_VOLDN,        // BUTTON_IDX_VOLUME_DOWN
#     ButtonIdx_PWR,          // Power
#     ButtonIdx_BT,           // BT PAIRING 
#        ButtonIdx_AUX,
#     ButtonIdx_VOLUP_MFB,    // BUTTON_IDX_VOLUME_UP_MFB
#     ButtonIdx_VOLDN_MFB,    // BUTTON_IDX_VOLUME_DOWN_MFB
#     ButtonIdx_VOLUP_VOLDN,  // BUTTON_IDX_VOLUME_UP_VOLUME_DOWN
#     ButtonIdx_VOLUP_SMART,  // BUTTON_IDX_VOLUME_UP_SMART
#     ButtonIdx_VOLDN_SMART,  // BUTTON_IDX_VOLUME_DOWN_MFB
#     ButtonIdx_S3,           // Boot lo


headphone_play_button = "start cmd.exe /C D:\\apiclient.exe app.param.set 0x84 0x10005"
headphone_pause_button = "start cmd.exe /C D:\\apiclient.exe app.param.set 0x84 0x10005"
headphone_smart_button = "start cmd.exe /C D:\\apiclient.exe app.param.set 0x84 0x20005"
headphone_volumeUp_button = "start cmd.exe /C D:\\apiclient.exe app.param.set 0x84 0x30005"
headphone_volumeDown_button = "start cmd.exe /C D:\\apiclient.exe app.param.set 0x84 0x40005"
headphone_power_button = "start cmd.exe /C D:\\apiclient.exe app.param.set 0x84 0x50005" #not enabled
headphone_pairing_request_button = "start cmd.exe /C D:\\apiclient.exe app.param.set 0x84 0x60008"

# not available
headphone_volumeUp_MFB_button = 0
headphone_volumeDown_MFB_button = 0
headphone_volumeUp_volumeDown_button = "start cmd.exe /C D:\\apiclient.exe app.param.set 0x84 0xA0009" #factory reset
headphone_volumeUp_smart_button = "start cmd.exe /C D:\\apiclient.exe app.param.set 0x84 0xB0009"  #ANC On
headphone_volumeDown_smart_button = "start cmd.exe /C D:\\apiclient.exe app.param.set 0x84 0xC0009"  #ANC off


#########################################
#logmon tool

logmon_tool_path = r"D:\Project\Harman_Project\JBL_150NC_Project\Tools\lxlogmon.exe"
avserve_tool_path = r"D:\Project\Harman_Project\JBL_150NC_Project\Tools\avserve_sdk27.exe"

# Project path
project_path = r'D:\Automation\Eclipse_workspace\JBL_python'

os.chdir(project_path)
logging.info(os.getcwd())

#logmon_logging.txt path
logmon_logging_path = os.path.join(os.getcwd(),r'com\jbl\\third_party_app\logmon_logging.txt')
logging.info(logmon_logging_path + "-------logmon_logging.txt path")

#failed log folder path
failed_log_folder = os.path.join(os.getcwd(),r'com\jbl\failed_log_file')
logging.info(failed_log_folder)
    


