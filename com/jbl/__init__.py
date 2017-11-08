from os import path, remove
import logging
import logging.config
import json
  
#from .first_class import FirstClass
#from .second_class import SecondClass
   
#from test.test_app_launch_page import Test_launchApp
  
   
# If applicable, delete the existing log file to generate a fresh log file during each execution
if path.isfile("jbl_logging.log"):
    remove("jbl_logging.log")
   
with open("../jbl_logging_configuration.json", 'r') as logging_configuration_file:
    config_dict = json.load(logging_configuration_file)
   
logging.config.dictConfig(config_dict)
   
# Log that the logger was configured
logger = logging.getLogger(__name__)
logger.info('Completed configuring logger()!')