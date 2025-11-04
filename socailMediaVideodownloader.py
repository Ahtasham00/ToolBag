#isAWW
import requests
def tiktok_downloader(url):
    output_file = 'temp/tiktok_video.mp4'
    # Send a GET request to the URL
    response = requests.get(url, stream=True)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Open a file in binary write mode to save the video
        with open(output_file, 'wb') as f:
            # Iterate over the response content in chunks and write to the file
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)
        print("Video downloaded successfully!")
    else:
        print("Failed to download video. Status code:", response.status_code)
        # Example usage