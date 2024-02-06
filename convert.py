from moviepy.editor import *
import os

# Directory containing the MP4 files
mp4_directory = "./"

# Directory to save the MP3 files
mp3_directory = "./mp3"

# Check if the output directory exists, if not, create it
if not os.path.exists(mp3_directory):
    os.makedirs(mp3_directory)

# Loop through each file in the directory
for filename in os.listdir(mp4_directory):
    if filename.endswith(".mp4"):
        # Load the MP4 video file
        video_path = os.path.join(mp4_directory, filename)
        video = VideoFileClip(video_path)

        # Extract the audio and save it as MP3
        audio_path = os.path.join(mp3_directory, os.path.splitext(filename)[0] + ".mp3")
        video.audio.write_audiofile(audio_path)

        # Close the video file
        video.close()

print("Conversion complete.")
