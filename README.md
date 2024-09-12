# Bulk Voice Fatcher

## Project Description

**Bulk Voice Downloader** is a Python-based tool designed to automate the downloading and renaming of voice recordings listed in a CSV file. The CSV contains columns such as the phone number and the corresponding recording URL. The tool processes a large number of entries and downloads the voice recordings, renaming each file with the respective number from the same row for easy identification.

## Features

- Downloads voice recordings from URLs listed in a CSV file.
- Renames the downloaded files according to the associated number in the CSV.
- Handles bulk data efficiently, processing large amounts of records.
- User-friendly interface to select CSV files and the save directory.
- Real-time status updates during the download process.

## How It Works

1. **CSV File Input**: The tool reads a CSV file where each row contains a phone number and a corresponding voice recording URL.
2. **Download and Rename**: It downloads the voice file from the provided URL and renames the file to the number mentioned in the same row of the CSV.
3. **Save to Directory**: The renamed files are saved in the directory specified by the user.

## Requirements

- Python 3.x
- pandas
- requests
- tkinter
- threading

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/Dhirajkumar908/bulk_voice_downloader.git
    ```
2. Install the required dependencies:
    ```bash
    pip install pandas requests pydub tkinter
    ```

## Usage

1. Run the Python script:
    ```bash
    python voice_downloader.py
    ```
2. Select the CSV file and the directory to save the downloaded voice recordings.
3. Click the "Start Downloading" button to begin the process. The tool will show real-time status updates and notify when the task is completed.

## Example CSV Format

```csv
called_number,recording
8869021459,http://example.com/recording1.wav
8958703556,http://example.com/recording2.wav
