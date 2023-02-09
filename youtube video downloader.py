import pytube

# Get the YouTube URL
url = input("Enter the YouTube URL: ")

# Create a YouTube object
yt = pytube.YouTube(url)

# Get the highest resolution video available
video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
# Download the video
video.download()

print("Video downloaded successfully!")
