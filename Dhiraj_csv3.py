import pandas as pd
import requests
import os
from tkinter import Tk, filedialog, messagebox, StringVar, Frame, Label
from tkinter import ttk  # Use ttk for better styling
from threading import Thread

# Function to download and rename .wav files
def download_and_rename(row, save_directory, index):
    called_number = row['called_number']
    recording_url = row['recording']
    
    wav_file_name = f"{called_number}.wav"
    wav_file_path = os.path.join(save_directory, wav_file_name)
    
    try:
        response = requests.get(recording_url)
        if response.status_code == 200:
            with open(wav_file_path, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded and saved as {wav_file_name}")
        else:
            print(f"Failed to download {recording_url}")
    except Exception as e:
        print(f"Error downloading {recording_url}: {e}")

# Function to process the CSV and download voice files
def process_csv_file(csv_file_path, save_directory, status_label):
    try:
        df = pd.read_csv(csv_file_path)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to read the CSV file: {e}")
        return
    
    # Update UI status label to show processing
    status_label.set("Processing... Downloading files")

    # Process each row and download files
    for index, row in df.iterrows():
        download_and_rename(row, save_directory, index)

    # Update UI status label after completion
    status_label.set("Task completed successfully!")
    messagebox.showinfo("Completed", "All recordings have been downloaded and saved!")

# Function to select the CSV file
def select_csv_file(csv_label):
    csv_file_path = filedialog.askopenfilename(title="Select CSV File", filetypes=[("CSV files", "*.csv")])
    if csv_file_path:
        csv_label.set(csv_file_path)

# Function to select the directory for saving the files
def select_save_directory(directory_label):
    save_directory = filedialog.askdirectory(title="Select Directory to Save WAV Files")
    if save_directory:
        directory_label.set(save_directory)

# Function to start the processing with threading to avoid freezing UI
def start_processing(csv_file_path, save_directory, status_label):
    if not csv_file_path.get() or not save_directory.get():
        messagebox.showerror("Error", "Please select both CSV file and directory.")
        return
    # Use threading to run the process without freezing the UI
    Thread(target=process_csv_file, args=(csv_file_path.get(), save_directory.get(), status_label)).start()

# Create the main Tkinter window with styling
def create_ui():
    root = Tk()
    root.title("Voice File Downloader")
    root.geometry("800x450")
    root.configure(bg='#2C3E50')  # Set a modern dark background color
    
    # Define styling for ttk widgets
    style = ttk.Style(root)
    style.theme_use('clam')  # Use a more modern theme
    style.configure("TButton", font=('Arial', 12), background="#e6e9f7", foreground="black", padding=10)
    style.configure("TLabel", background="#2C3E51", foreground="white", font=('Arial', 10, 'bold'))
    style.configure("TFrame", background="#2C3E50")

    # Variables to store selected file paths
    csv_file_path = StringVar()
    save_directory = StringVar()
    status_label = StringVar()

    # Create a frame to hold the UI elements
    frame = ttk.Frame(root, padding=20)
    frame.pack(pady=20)

    # Label Title
    ttk.Label(frame, text="Voice File Downloader", font=("Arial", 16, 'bold'), background="#2C3E50", foreground="white").grid(row=0, column=0, columnspan=2, pady=10)

    # Button and label to select the CSV file
    ttk.Button(frame, width=20, text="Select CSV File", command=lambda: select_csv_file(csv_file_path)).grid(row=1, column=0, padx=10, pady=10)
    ttk.Label(frame, textvariable=csv_file_path, wraplength=300).grid(row=1, column=1)

    # Button and label to select the directory
    ttk.Button(frame, width=20, text="Select Save Directory", command=lambda: select_save_directory(save_directory)).grid(row=2, column=0, padx=10, pady=10)
    ttk.Label(frame, textvariable=save_directory, wraplength=300).grid(row=2, column=1)

    # Button to start the process
    ttk.Button(frame, width=20, text="Start Downloading", command=lambda: start_processing(csv_file_path, save_directory, status_label)).grid(row=3, column=0, columnspan=2, pady=20)

    # Label to display the status
    ttk.Label(frame, textvariable=status_label).grid(row=4, column=0, columnspan=2, pady=10)
    status_label.set("Ready to start...")

    root.mainloop()

# Run the UI
if __name__ == "__main__":
    create_ui()
