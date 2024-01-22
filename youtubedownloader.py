import os
from pytube import YouTube, Playlist
import requests
from tqdm import tqdm
import re
import banner
from util.color import Color as color_module
def clean_filename(title):
    # Remove invalid characters from the title
    cleaned_title = re.sub(r'[\\/:"*?<>|]+', '', title)
    return cleaned_title

def download_video(video_url, total_videos, current_video, download_progress):
    try:
        video = YouTube(video_url)
        stream = video.streams.filter(res="720p").first()

        print(f"\nVideo {current_video}/{total_videos}: {video.title}")
        print(f"Storage required: {stream.filesize / (1024**2):.2f} MB")

        # Use cleaned title as the filename
        cleaned_title = clean_filename(video.title)
        file_name = f"./downloads/{cleaned_title}.mp4"
        colors = [color_module.CRED2, color_module.CBLUE2, color_module.CGREEN2, color_module.CYELLOW2, color_module.CPURPLE2, color_module.CCYAN2]
        color = colors[(current_video - 1) % len(colors)]  # Cycle through colors

        with requests.get(stream.url, stream=True) as response, open(file_name, 'wb') as file, tqdm(
        desc=f"Video {current_video}/{total_videos}", total=stream.filesize,
        unit='B', unit_scale=True, unit_divisor=1024,
        ncols=100, mininterval=1,
        bar_format=f"{color}{{l_bar}}{{bar}}{{r_bar}}{color_module.ENDC}",
        ) as progress_bar:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
                    progress_bar.update(len(chunk))

        print(f"\nDownloading video {current_video}/{total_videos}: {video.title}")

        download_progress.append(f"Video {current_video}/{total_videos}: {video.title} downloaded successfully.")
    except Exception as e:
        download_progress.append(f"Error downloading {video.title}: {str(e)}")



def main():
    banner.show_banner()

    playlist_url = input("Enter the URL of the playlist or video: ")
    download_progress = []
    playlist = None  # Initialize playlist outside the try block

    try:
        if 'playlist' in playlist_url.lower():
            playlist = Playlist(playlist_url)
            total_videos = len(playlist.video_urls)
            print(f"Playlist detected with {total_videos} videos.")
        else:
            total_videos = 1  # Single video
            print("Single video detected.")

        for i, video_url in enumerate(playlist.video_urls if playlist else [playlist_url]):
            download_video(video_url, total_videos, i + 1, download_progress)

        print("Download completed successfully.")
        for progress in download_progress:
            print(progress)
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == '__main__':
    if not os.path.exists('./downloads'):
        os.makedirs('./downloads')

    main()
