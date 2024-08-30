# ***********************************
# Authors:
# Andrea Alvaro Martin 100512694
# Diana Gallardo de Pedro 100406633
# Ines Martínez Hontecillas 100506592
# ***********************************
# Date: 2024-05-17
# last update: 2024-05-14
# ***********************************

import tkinter as tk
from tkinter import filedialog
import stegocode

# ***********************************
# Function to browse the audio file where we want to hide the secret message
# add also that mp3 files are accepted
#
# ***********************************
def browse_audio_file():
    global audio_path
    audio_path = filedialog.askopenfilename(filetypes=[('Audio Files', '*.wav')]) 
    audio_label.config(text=audio_path)


# ***********************************
# Function to browse the audio file with the hidden message
# ***********************************
def browse_audio_file2():
    global audio_path2
    audio_path2 = filedialog.askopenfilename(filetypes=[('Audio Files', '*.wav')])
    audio_label2.config(text=audio_path2)


# ***********************************
# Function when hide button clicked - hides message
# ***********************************
def hide_button_clicked():
    passw = key_entry.get()
    if isinstance(passw, int):
        result_label.config(text="Please, type a numeric password")
        return False
    msg = message_entry.get()
    # calls hide function in stegocode.py
    output_label = output_entry.get()
    stegocode.run_hide(audio_path, passw, msg, output_label)


# ***********************************
# Function when unhide button clicked - unhides message
# ***********************************
def unhide_button_clicked():
    passw = key_entry2.get()
    # calls unhide function in stegocode.py
    hidden_text = stegocode.run_unhide(audio_path2, passw)
    # shows hidden text
    result_label.config(text=hidden_text)        


# ***********************************
# Section - App title and window size
# ***********************************
root = tk.Tk()
root.title("Audio StegoTool")
root.geometry("500x780")

tk.Label(root, text="").pack()

tk.Label(root, text="Welcome to Wav Audio StegoTool !", font=("Helvetica", 16)).pack()
#tk.Label(root, text="").pack()

# ***********************************
# Section - Hide Interface 
# ***********************************

tk.Label(root, text="To hide text:", font=("Helvetica", 14)).pack()

#Browse audio file to hide message
tk.Label(root, text="1. Audio File:",font=("Helvetica", 10)).pack()
audio_label = tk.Label(root, text="")
audio_label.pack()

browse_audio_button = tk.Button(root, text="Browse Audio File",font=("Helvetica", 10), command=browse_audio_file)
browse_audio_button.pack()

tk.Label(root, text="").pack()

#Choose name of output file with hidden message
tk.Label(root, text="2. Output File Name:", font=("Helvetica", 10)).pack()
output_entry = tk.Entry(root)
output_entry.pack()

tk.Label(root, text="").pack()

#Choose password 
tk.Label(root, text="3. Numeric Password:",font=("Helvetica",10)).pack()
key_entry = tk.Entry(root, show='*')
key_entry.pack()

tk.Label(root, text="").pack()

#Message to hide
tk.Label(root, text="4. Message:",font=("Helvetica", 10)).pack()
message_entry = tk.Entry(root)
message_entry.pack()

#Triggers hide message function
hide_button = tk.Button(root, text="Hide",font=("Helvetica",10), command=hide_button_clicked)
hide_button.pack()


tk.Label(root, text="").pack()

# ***********************************
# Section - Unhide Interface 
# ***********************************
tk.Label(root, text="To unhide text:", font=("Helvetica", 14)).pack()

#Browse audio file with the hidden message
tk.Label(root, text="1. Audio File:", font=("Helvetica",10)).pack()
audio_label2 = tk.Label(root, text="")
audio_label2.pack()

#Browse audio file to unhide message
browse_audio_button2 = tk.Button(root, text="Browse Audio File",font=("Helvetica",10), command=browse_audio_file2)
browse_audio_button2.pack()

tk.Label(root, text="").pack()

#Write password
tk.Label(root, text="2. Numeric Password:",font=("Helvetica",10)).pack()
key_entry2 = tk.Entry(root,show='*')
key_entry2.pack()

#Triggers unhide function
unhide_button = tk.Button(root, text="Unhide", font=("Helvetica", 10),command=unhide_button_clicked)
unhide_button.pack()
tk.Label(root, text="").pack()

#Shows hidden message in the audio
tk.Label(root, text="Hidden text:", font=("Helvetica", 10)).pack()


result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
