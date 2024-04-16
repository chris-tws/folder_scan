import os  
import time  
from datetime import datetime  
import tkinter as tk  
from tkinter import messagebox  
  
def count_files_in_directory(directory):  
    try:  
        with os.scandir(directory) as it:  
            return sum(1 for entry in it if entry.is_file())  
    except FileNotFoundError:  
        print(f"The directory {directory} was not found.")  
        return -1  
  
def show_notification():  
    root = tk.Tk()  
    root.withdraw()  # We don't want a full GUI, so keep the root window from appearing  
    messagebox.showinfo("Notification", "The number of files has not changed.")  
    root.destroy()  
    # print("The number of files has not changed.")
  
def monitor_directory(directory, interval_minutes):  
    prev_count = count_files_in_directory(directory)  
    sleep_time = interval_minutes * 60  # Convert minutes to seconds
    if prev_count != -1:  
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Initial file count: {prev_count} ")  
        print(f"Sleep for every {sleep_time} secs")
      
    while True:  
        time.sleep(sleep_time)  # Convert minutes to seconds  
        current_count = count_files_in_directory(directory)  
          
        if current_count == -1:  
            break  # Exit the loop if the directory doesn't exist  
  
        if current_count == prev_count:  
            show_notification()  
            break  # Exit the loop if the file count hasn't changed
        else:  
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] File count changed: {prev_count} -> {current_count} ")  
  
        prev_count = current_count  # Update the previous count  
  
if __name__ == "__main__":  
    input_folder = input("Enter the path to the input folder: ")  
    interval = float(input("Enter the interval in minutes: "))  
    monitor_directory(input_folder, interval)  
