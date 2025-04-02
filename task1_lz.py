import getpass 
import datetime
from datetime import date, datetime
import pandas as pd
import os

def log(func):
    def wrapper(*args, **kwargs):
        original_result = func(*args, **kwargs)


        user_name = getpass.getuser()
        func_name = func.__name__
        formatted_date = datetime.now().strftime("%d.%m.%Y")
        formatted_time = datetime.now().strftime("%H:%M:%S")
        
        if os.path.isfile("logs.csv"):
            print("Файл существует")
            file_df = pd.read_csv("logs.csv")
            new_id = len(file_df) + 1
        else:
            print("Файл не существует")
            new_id = 1

        new_entry = pd.DataFrame([{'id': new_id, 'pc_username': user_name,'function_name': func_name, 'Date': formatted_date,'Time': formatted_time}])

        if os.path.isfile("logs.csv"):
            new_entry.to_csv("logs.csv", mode='a', header=False, index=False)
        else:
            new_entry.to_csv("logs.csv", mode='w', header=True, index=False)
        
        return original_result
    return wrapper
