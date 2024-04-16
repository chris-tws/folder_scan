import os  
import time  
import tkinter as tk  
from tkinter import messagebox  
  
def count_files_in_directory(directory):  
    try:  
        return len([name for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name))])  
    except FileNotFoundError:  
        print(f"The directory {directory} was not found.")  
        return -1  
  
def show_notification():  
    root = tk.Tk()  
    root.withdraw()  # We don't want a full GUI, so keep the root window from appearing  
    messagebox.showinfo("Notification", "The number of files has not changed.")  
    root.destroy()  
  
def monitor_directory(directory, interval_minutes):  
    prev_count = count_files_in_directory(directory)  
      
    while True:  
        time.sleep(interval_minutes * 60)  # Convert minutes to seconds  
        current_count = count_files_in_directory(directory)  
          
        if current_count == -1:  
            break  # Exit the loop if the directory doesn't exist  
  
        if current_count == prev_count:  
            show_notification()  
        else:  
            print(f"File count changed: {prev_count} -> {current_count}")  
  
        prev_count = current_count  # Update the previous count  
  
if __name__ == "__main__":  
    input_folder = input("Enter the path to the input folder: ")  
    interval = float(input("Enter the interval in minutes: "))  
    monitor_directory(input_folder, interval)  
