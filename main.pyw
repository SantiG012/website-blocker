from datetime import datetime as dt
from constans import *


actual_time = dt.now()
  
    # time of your work 
if LABOR_TIME_START  < actual_time < LABOR_TIME_END: 

    with open(HOSTS_PATH, 'r+') as file: 
        content = file.read() 
        for website in WEBSITES: 
            if not website in content: 
                file.write(LOCALHOST + " " + website + "\n") 
else: 
    with open(HOSTS_PATH, 'r+') as file: 
        content=file.readlines() 
        file.seek(0) 
        for line in content: 
            if not any(website in line for website in WEBSITES): 
                file.write(line) 
  
            # removing hostnmes from host file 
        file.truncate() 

