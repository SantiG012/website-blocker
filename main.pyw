from datetime import datetime as dt
from constans import *
from hosts_file_manager import HostsFileManager

actual_time = dt.now()

hosts_file_manager = HostsFileManager()
  
    # time of your work 
if LABOR_TIME_START  < actual_time < LABOR_TIME_END: 

    hosts_file_manager.block_websites()

else: 
    hosts_file_manager.unblock_websites()

