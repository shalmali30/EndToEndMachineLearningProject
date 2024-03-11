#This init file can be created in the logging folder(extra folder in src/mlProject/logging) But in the main.py , import from src.mlProject.logging

#we will be using this logging in every other component to track the project logs

import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
#This is default logging string . You can always use this. 

#This will give you : date and time /level/modulename/log_message

log_dir ="logs"  #create log folder variable

log_filepath = os.path.join(log_dir,"Running_log.log")      #create log file variable. We will create the file inside log folder
os.makedirs(log_dir,exist_ok=True) #Create if not already exists

logging.basicConfig(
    level = logging.INFO,  #define level 
    format = logging_str,  #define format of logging message
    handlers=[
        logging.FileHandler(log_filepath),  #this will store output in Running_log.log file
        logging.StreamHandler(sys.stdout)   # this will print output in terminal/output window
    ]
)

#define logger object:

logger = logging.getLogger("ML project Logging")

#We will test this in main.py