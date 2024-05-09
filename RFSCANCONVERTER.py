import os
import tkinter as tk
import tkinter.filedialog as filedialog
import csv
import subprocess
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def detect_csv_separator(file_path):
    # Function to detect the most likely CSV separator used in the file
    with open(file_path, 'r') as csv_file:
        sample_data = csv_file.read(1024)  # Read the first 1024 bytes (adjust as needed)
        if ';' in sample_data and ',' not in sample_data:
            return ';'
        elif ',' in sample_data and ';' not in sample_data:
            return ','
        else:
            # Default to semicolon if both comma and semicolon are found or if none is found
            return ';'

def convert_files():
    file_paths = filedialog.askopenfilenames(filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*")))
    for file_path in file_paths:
        directory = os.path.dirname(file_path)
        file_name = os.path.basename(file_path)
        output_file_name = "{}_OK.txt".format(file_name)
        output_file_path = os.path.join(directory, output_file_name)

        csv_separator = detect_csv_separator(file_path)

        with open(file_path, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=csv_separator)

            converted_data = []

            for row in reader:
                frequency = row[0].strip()
                if '.' in frequency:
                    freq_parts = frequency.split('.')
                    if len(freq_parts[0]) < 3:
                        frequency = "{:<3}.{}".format(freq_parts[0], freq_parts[1][:6].ljust(6, '0'))
                    else:
                        frequency = "{:3}.{:<6}".format(freq_parts[0][:3], freq_parts[1][:6].ljust(6, '0'))
                elif ',' in frequency:
                    freq_parts = frequency.split(',')
                    if len(freq_parts[0]) < 3:
                        frequency = "{:<3},{}".format(freq_parts[0], freq_parts[1][:6].ljust(6, '0'))
                    else:
                        frequency = "{:3},{:<6}".format(freq_parts[0][:3], freq_parts[1][:6].ljust(6, '0'))
                converted_data.append("{:>10s}, {:>10s}".format(frequency, row[1].strip()))

        with open(output_file_path, 'w') as txt_file:
            txt_file.write('\n'.join(converted_data))

    # Open Finder window in the folder where the new files were created
    subprocess.call(['open', directory])

    # Display "YOUR FILES ARE READY! COMMUNISM WINS!" message
    message_label.config(text="YOUR FILES ARE READY!\nCOMMUNISM WINS!", fg="red")

root = tk.Tk()
root.title("RF SCAN CONVERTER")
root.geometry("500x500")

# Load the background image after the Tk instance is created
background_image_path = resource_path('Images/roadcase.gif')
background_image = tk.PhotoImage(file=background_image_path)
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

title_frame = tk.Frame(root, bg="white")
title_frame.pack(pady=10)

rf_label = tk.Label(title_frame, text="RF SCAN CONVERTER", font=("Helvetica", 24, "bold"), fg="black")
rf_label.pack()

name_label = tk.Label(title_frame, text="BY DIOGO GUEDES", font=("Helvetica", 12), fg="black")
name_label.pack()

button = tk.Button(root, text="Select Multiple .CSV Files", command=convert_files, font=("Helvetica", 12))
button.pack(pady=30)

message_label = tk.Label(root, text="", font=("Helvetica", 16, "bold"), fg="red")
message_label.pack()

root.mainloop()
