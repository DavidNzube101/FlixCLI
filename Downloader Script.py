import requests
import os
from urllib.parse import unquote
from tqdm import tqdm

def download_file(url, directory=None):
    try:
        # Send a GET request to the URL
        response = requests.get(url, stream=True)
        
        # Raise an exception for bad status codes
        response.raise_for_status()
        
        # Get the filename from the URL and decode it
        filename = unquote(url.split('/')[-1])
        
        # If directory is provided, join it with the filename
        if directory:
            if not os.path.exists(directory):
                os.makedirs(directory)
            filename = os.path.join(directory, filename)
        
        # Get the total file size
        total_size = int(response.headers.get('content-length', 0))
        
        # Open the file in binary write mode
        with open(filename, 'wb') as file, tqdm(
            desc=filename,
            total=total_size,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024,
        ) as progress_bar:
            for data in response.iter_content(chunk_size=1024):
                size = file.write(data)
                progress_bar.update(size)
        
        print(f"\nFile downloaded successfully: {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading file: {e}")
    except PermissionError:
        print(f"Permission denied. Unable to save file to: {filename}")
        print("Try running the script with administrator privileges or choose a different directory.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
url = "https://ia801601.us.archive.org/20/items/arcane-eng-dub-01-720p-hq-netflix/Arcane_Eng_Dub_-_01_720p_HQ_Netflix.mp4" # S1E1
#url = "https://ia801601.us.archive.org/20/items/arcane-eng-dub-01-720p-hq-netflix/Arcane_Eng_Dub_-_02_720p_HQ_Netflix.mp4" # S1E2
#url = "https://ia801601.us.archive.org/20/items/arcane-eng-dub-01-720p-hq-netflix/Arcane_Eng_Dub_-_03_720p_HQ_Netflix.mp4" # S1E3
#url = "https://ia801601.us.archive.org/20/items/arcane-eng-dub-01-720p-hq-netflix/Arcane_Eng_Dub_-_04_720p_HQ_Netflix.mp4" # S1E4
#url = "https://ia801601.us.archive.org/20/items/arcane-eng-dub-01-720p-hq-netflix/Arcane_Eng_Dub_-_05_720p_HQ_Netflix.mp4" # S1E5
#url = "https://ia801601.us.archive.org/20/items/arcane-eng-dub-01-720p-hq-netflix/Arcane_Eng_Dub_-_06_720p_HQ_Netflix.mp4" # S1E6
#url = "https://ia801601.us.archive.org/20/items/arcane-eng-dub-01-720p-hq-netflix/Arcane_Eng_Dub_-_07_720p_HQ_Netflix.mp4" # S1E7
#url = "https://ia801601.us.archive.org/20/items/arcane-eng-dub-01-720p-hq-netflix/Arcane_Eng_Dub_-_08_720p_HQ_Netflix.mp4" # S1E8
#url = "https://ia801601.us.archive.org/20/items/arcane-eng-dub-01-720p-hq-netflix/Arcane_Eng_Dub_-_09_720p_HQ_Netflix.mp4" # S1E9

download_directory = os.path.join(os.path.expanduser("~"), "Downloads/ArcaneS1")
download_file(url, download_directory)