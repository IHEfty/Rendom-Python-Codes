import os
from pytube import YouTube
from tqdm import tqdm

SAVE_PATH = "./downloads"  

if not os.path.exists(SAVE_PATH):
    os.makedirs(SAVE_PATH)

link = input("Enter the YouTube link > ")

try:
    yt = YouTube(link)
    d_video = yt.streams.filter(file_extension='mp4').get_highest_resolution()

    print(f"Downloading '{yt.title}'...")
    with tqdm(total=d_video.filesize, desc="Downloading", ncols=100, unit="B", unit_scale=True) as pbar:
        d_video.download(output_path=SAVE_PATH, on_progress_callback=lambda stream, chunk, file_handle, bytes_remaining: pbar.update(len(chunk)))

    print('Video downloaded successfully!')

except Exception as e:
    print(f"Error: {e}")
    print("Please ensure the link is valid and try removing extra URL parameters.")
