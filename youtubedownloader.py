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

def download_media(media_url, total_media, current_media, download_progress, download_type='video'):
    try:
        media = YouTube(media_url)
        if download_type == 'video':
            stream = media.streams.filter(res="720p").first()
        elif download_type == 'audio':
            stream = media.streams.filter(only_audio=True).first()

        print(f"\n{download_type.capitalize()} {current_media}/{total_media}: {media.title}")
        print(f"Storage required: {stream.filesize / (1024**2):.2f} MB")

        # Use cleaned title as the filename
        cleaned_title = clean_filename(media.title)
        file_extension = 'mp4' if download_type == 'video' else 'mp3'
        file_name = f"./downloads/{cleaned_title}.{file_extension}"
        colors = [color_module.CRED2, color_module.CBLUE2, color_module.CGREEN2, color_module.CYELLOW2, color_module.CPURPLE2, color_module.CCYAN2]
        color = colors[(current_media - 1) % len(colors)]  # Cycle through colors

        with requests.get(stream.url, stream=True) as response, open(file_name, 'wb') as file, tqdm(
            desc=f"{download_type.capitalize()} {current_media}/{total_media}", total=stream.filesize,
            unit='B', unit_scale=True, unit_divisor=1024,
            ncols=100, mininterval=1,
            bar_format=f"{color}{{l_bar}}{{bar}}{{r_bar}}{color_module.ENDC}",
        ) as progress_bar:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
                    progress_bar.update(len(chunk))

        print(f"\nDownloading {download_type} {current_media}/{total_media}: {media.title}")

        download_progress.append(f"{download_type.capitalize()} {current_media}/{total_media}: {media.title} downloaded successfully.")
    except Exception as e:
        download_progress.append(f"Error downloading {download_type} {media.title}: {str(e)}")

# Modify the main function accordingly
def main():
    banner.show_banner()

    playlist_url = input("Enter the URL of the playlist or video: ")
    download_progress = []
    playlist = None  # Initialize playlist outside the try block

    try:
        download_type = input("Enter 'video' or 'audio' to download: ").lower()

        if 'playlist' in playlist_url.lower():
            playlist = Playlist(playlist_url)
            total_media = len(playlist.video_urls)
            print(f"{download_type.capitalize()} playlist detected with {total_media} {download_type}s.")
        else:
            total_media = 1  # Single video or audio
            print(f"Single {download_type} detected.")

        for i, media_url in enumerate(playlist.video_urls if playlist else [playlist_url]):
            download_media(media_url, total_media, i + 1, download_progress, download_type)

        print(f"Download completed successfully. {download_type.capitalize()}s saved in the 'downloads' folder.")
        for progress in download_progress:
            print(progress)
    except Exception as e:
        print(f"Error: {str(e)}")

# Run the program
if __name__ == '__main__':
    if not os.path.exists('./downloads'):
        os.makedirs('./downloads')

    main()


