'''
Created on Nov 3, 2017

@author: hkumar04
'''

import os
import win32gui

import logging
from time import sleep
import win32api
import win32con

from com.jbl.common_method import constants
from os import path
class Logmon_Tool_Parser():

    ''' 
    This file is created to capture log from logmon tool.
    First enable logmon and clear all old log .After tha copy log and parse it
    
    '''
    
 
    
    
    @staticmethod
    def open_avserve_tool():
        os.startfile(constants.avserve_tool_path)
        sleep(3)
        logging.info("Opening avserve tool to capture log")
        avserve_handler = win32gui.FindWindow(None,"AvServe (8377)")
        logging.info(avserve_handler)

    
    
    @staticmethod
    def open_logmon_tool():
        os.startfile(constants.logmon_tool_path)
        sleep(5)
        logging.info("Opening Logmon tool to capture log")
        logmon_handler = win32gui.FindWindow(None,"LxLogMon localhost:8377")
        logging.info(logmon_handler)
        win32gui.SetForegroundWindow(logmon_handler)
     
     
    @staticmethod   
    def click_enableButton_logmon_tool():

        # To Click on Enable button in LogMon
        logmon_handler = win32gui.FindWindow(None,"LxLogMon localhost:8377")
        logmon_child_handler=win32gui.FindWindowEx(logmon_handler,0,"wxWindowClassNR",'panel') 
        enable_child_handle=win32gui.FindWindowEx(logmon_child_handler, 0, 'wxWindowClassNR', 'Enable')
        enable_childwindow_Name = win32gui.GetWindowText(enable_child_handle)
        logging.info("Enable window text" + enable_childwindow_Name)
        win32api.PostMessage(enable_child_handle,win32con.WM_LBUTTONDOWN,win32con.MK_RBUTTON,0)
        sleep(0.5)
        win32api.PostMessage(enable_child_handle, win32con.WM_LBUTTONUP, win32con.MK_RBUTTON, 0)
        sleep(1)
        
        
    @staticmethod   
    def click_readCodesButton_logmon_tool(): 
        # To Click on Read codes button in LogMon
        logmon_handler = win32gui.FindWindow(None,"LxLogMon localhost:8377")
        logmon_child_handler=win32gui.FindWindowEx(logmon_handler,0,"wxWindowClassNR",'panel') 
        enable_child_handle=win32gui.FindWindowEx(logmon_child_handler, 0, 'wxWindowClassNR', 'Read Codes')
        enable_childwindow_Name = win32gui.GetWindowText(enable_child_handle)
        logging.info("Enable window text" + enable_childwindow_Name)
        win32api.PostMessage(enable_child_handle,win32con.WM_LBUTTONDOWN,win32con.MK_RBUTTON,0)
        sleep(0.5)
        win32api.PostMessage(enable_child_handle, win32con.WM_LBUTTONUP, win32con.MK_RBUTTON, 0)
        sleep(1)  
    
    
    @staticmethod  
    def click_clearButton_logmon_tool():
        # To click Clear button in LogMon to clear old log
        logmon_handler = win32gui.FindWindow(None,"LxLogMon localhost:8377")
        logmon_child_handler=win32gui.FindWindowEx(logmon_handler,0,"wxWindowClassNR",'panel') 
        enable_child_handle=win32gui.FindWindowEx(logmon_child_handler, 0, 'wxWindowClassNR', 'Clear')
        enable_childwindow_Name = win32gui.GetWindowText(enable_child_handle)
        logging.info("Enable window text" + enable_childwindow_Name)
        win32api.PostMessage(enable_child_handle,win32con.WM_LBUTTONDOWN,win32con.MK_RBUTTON,0)
        sleep(0.5)
        win32api.PostMessage(enable_child_handle, win32con.WM_LBUTTONUP, win32con.MK_RBUTTON, 0)         
        sleep(1)
        
    @staticmethod
    def capture_logmon_log_and_save_it():
        logmon_handler = win32gui.FindWindow(None,"LxLogMon localhost:8377")
        #win32gui.SetForegroundWindow(logmon_handler)
        sleep(2)
        panel_child_handler=win32gui.FindWindowEx(logmon_handler,0,"wxWindowClassNR",'panel') 
        splitter_child_handler=win32gui.FindWindowEx(panel_child_handler,0,"wxWindowClassNR",'splitter') 
        log_display_child_handler=win32gui.FindWindowEx(splitter_child_handler,0,"RICHEDIT50W",None)
        win32gui.SetForegroundWindow(log_display_child_handler)       
        sleep(1)
        #ctrl+A
        win32api.keybd_event(0x11,0,0,0)
        win32api.keybd_event(0x41,0,0,0)
        sleep(.5)
        win32api.keybd_event(0x11, 0, win32con.KEYEVENTF_KEYUP, 0)
        win32api.keybd_event(0x41, 0, win32con.KEYEVENTF_KEYUP, 0)
 
        # ctrl+C
        win32api.keybd_event(0x11, 0, 0, 0)
        win32api.keybd_event(0x43, 0, 0, 0)
        sleep(.5)
        win32api.keybd_event(0x11, 0, win32con.KEYEVENTF_KEYUP, 0)
        win32api.keybd_event(0x43, 0, win32con.KEYEVENTF_KEYUP, 0)
        sleep(2)
        
        
        #if path.isfile("logmon_logging.txt"):
        #open("logmon_logging.txt",'w')
        os.startfile(r"D:\Automation\Eclipse_workspace\JBL_python\com\jbl\third_party_app\logmon_logging.txt")
        notepad_handle = win32gui.FindWindow(None, "logmon_logging - Notepad")
        sleep(2)
        #win32gui.SetForegroundWindow(notepad_handle)
        win32gui.GetForegroundWindow()
        
        #ctrl+A
        win32api.keybd_event(0x11,0,0,0)
        win32api.keybd_event(0x41,0,0,0)
        sleep(.5)
        win32api.keybd_event(0x11, 0, win32con.KEYEVENTF_KEYUP, 0)
        win32api.keybd_event(0x41, 0, win32con.KEYEVENTF_KEYUP, 0)
        sleep(1)
        
        win32api.keybd_event(0x11, 0, 0, 0) #0x11 is ctrl
        win32api.keybd_event(0x56, 0, 0, 0) # 0x41 is v
        sleep(.05)
        win32api.keybd_event(0x11, 0, win32con.KEYEVENTF_KEYUP, 0)
        win32api.keybd_event(0x56, 0, win32con.KEYEVENTF_KEYUP, 0)
        
        # ctrl+S
        win32api.keybd_event(0x11, 0, 0, 0)
        win32api.keybd_event(0x53, 0, 0, 0)
        sleep(.5)
        win32api.keybd_event(0x11, 0, win32con.KEYEVENTF_KEYUP, 0)
        win32api.keybd_event(0x53, 0, win32con.KEYEVENTF_KEYUP, 0)


        
        #To close the open notepad, first use Alt+F, press down arrow for six time and click on enter.
        #Alt+F
        win32api.keybd_event(0x12, 0, 0, 0)
        win32api.keybd_event(0x46, 0, 0, 0)
        sleep(.5)
        win32api.keybd_event(0x12, 0, win32con.KEYEVENTF_KEYUP, 0)
        win32api.keybd_event(0x46, 0, win32con.KEYEVENTF_KEYUP, 0)
        #down arrow
        for i in range (0,6):
            win32api.keybd_event(0x11, 0, 0, 0)
            win32api.keybd_event(0x28, 0, 0, 0)
            sleep(.5)
            win32api.keybd_event(0x11, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(0x28, 0, win32con.KEYEVENTF_KEYUP, 0)

        #enter
        win32api.keybd_event(0x0D, 0, 0, 0)

        
    @staticmethod   
    def compare_and_validate_functioanlity(listOfStringToValidate):
        
        flag = True
        i=0
        with open('D:\Automation\Eclipse_workspace\JBL_python\com\jbl\third_party_app\logmon_logging.txt','r') as logmon_log:
            for line in logmon_log:
                if listOfStringToValidate[i] == line:
                    i+=1
                    continue
                else:
                    flag = False 
        return flag

    
    