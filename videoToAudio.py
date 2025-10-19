import os
from moviepy.editor import VideoFileClip

def convert_video_to_mp3(video_path):
    # Ensure temp directory exists
    temp_dir = "temp"
    os.makedirs(temp_dir, exist_ok=True)

    # Extract base name and define output path
    base_name = os.path.splitext(os.path.basename(video_path))[0]
    output_path = os.path.join(temp_dir, f"{base_name}.mp3")

    # Convert video to audio
    try:
        video = VideoFileClip(video_path)
        audio = video.audio
        audio.write_audiofile(output_path)
        audio.close()
        video.close()
        return output_path
    except Exception as e:
        raise RuntimeError(f"Failed to convert video to MP3: {e}")