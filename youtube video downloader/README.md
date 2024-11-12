# YouTube Video Downloader

This Python script allows you to download YouTube videos easily using the `pytube` library. The script supports downloading single videos, multiple videos, and multiple videos using a file containing video links.

## Prerequisites

1. Install `pytube`:
   ```bash
   pip install pytube
   ```

2. Ensure you have an active internet connection for downloading videos.

## Features

- **Download a single video:** Download a video by specifying the link and resolution.
- **Download multiple videos:** Download multiple videos by providing a list of links.
- **Download from a file:** Use a text file containing video links for bulk downloads.

## Usage

### 1. Downloading a Single Video

The `YouTube` module from `pytube` allows you to create an object with the video URL. You can filter streams to download videos in a desired format and resolution.

```python
from pytube import YouTube 

SAVE_PATH = "/path/to/your/download/directory"
link = "https://youtube.com/shorts/akL53YfPTfI?si=ju1ohfkBdFSInLNj"

try: 
    yt = YouTube(link)
    d_video = yt.streams.filter(file_extension='mp4').get_highest_resolution()
    d_video.download(output_path=SAVE_PATH)
    print('Video downloaded successfully!')
except Exception as e:
    print(f"Error: {e}")
```

### 2. Downloading Multiple Videos

You can download multiple videos by looping through a list of links and applying the same download function for each.

```python
from pytube import YouTube

SAVE_PATH = "/path/to/your/download/directory"
links = ["https://www.youtube.com/watch?v=xWOoBJUqlbI",
         "https://www.youtube.com/watch?v=xWOoBJUqlbI"]

for link in links:
    try:
        yt = YouTube(link)
        d_video = yt.streams.filter(file_extension='mp4').get_highest_resolution()
        d_video.download(output_path=SAVE_PATH)
        print('Video downloaded successfully!')
    except Exception as e:
        print(f"Error: {e}")

print('Task Completed!')
```

### 3. Downloading Multiple Videos Using File Handling

This method uses a text file (e.g., `links_file.txt`) containing a list of video links. The script reads each line, treating each as a download link.

```python
from pytube import YouTube

SAVE_PATH = "/path/to/your/download/directory"

with open('links_file.txt', 'r') as link_file:
    for link in link_file:
        try:
            yt = YouTube(link.strip())
            d_video = yt.streams.filter(file_extension='mp4').get_highest_resolution()
            d_video.download(output_path=SAVE_PATH)
            print('Video downloaded successfully!')
        except Exception as e:
            print(f"Error: {e}")

print('Task Completed!')
```

## Important Notes

- **Internet Connection:** Ensure you have an active connection; interruptions can raise errors.
- **File Naming:** Avoid using `set_filename()` in loops, as it may result in only one file being downloaded. Use unique names if needed.
- **Error Handling:** Connection interruptions or format mismatches may raise exceptions.
- **File Handling:** To download multiple videos in bulk, use a text file containing URLs for easy management.
