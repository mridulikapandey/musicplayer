import tkinter as tk
from tkinter import filedialog
import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Create the main window
window = tk.Tk()
window.title("Music Player")

# Function to open and play a music file
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
    if file_path:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

# Function to stop playback
def stop_music():
    pygame.mixer.music.stop()

# Create buttons for open and stop
open_button = tk.Button(window, text="Open", command=open_file)
stop_button = tk.Button(window, text="Stop", command=stop_music)

open_button.pack(pady=20)
stop_button.pack(pady=10)

# Start the GUI application
window.mainloop()
