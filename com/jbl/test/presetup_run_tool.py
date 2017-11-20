'''
Created on Nov 3, 2017

@author: hkumar04
'''

from com.jbl.third_party_app.logmon_log_capture_tool import Logmon_Tool_Parser
from com.jbl.config import setupConfig

class run_pre_requisite_tool(setupConfig):
    
    def test_run_pre_requisite_tool(self):
        #Logmon_Tool_Parser.open_avserve_tool()
        Logmon_Tool_Parser.open_logmon_tool()
        Logmon_Tool_Parser.click_enableButton_logmon_tool()
        Logmon_Tool_Parser.click_readCodesButton_logmon_tool()
        Logmon_Tool_Parser.click_clearButton_logmon_tool()