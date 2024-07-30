from pytube import YouTube
import streamlit as st 

st.write("# Youtube Video Downloader")

yt = None
video_stream = None

video_link = st.text_input("Paste the video link here to download video")

# Check if the video link is provided
if video_link:
    try:
        # Create a YouTube object
        yt = YouTube(video_link)
        
        # Display video details
        st.write(f"**Video Title:** {yt.title}")
        st.image(f"{yt.thumbnail_url}", caption=f"{yt.title}")
    except Exception as e:
        st.write(f"Error: {e}")
else:
    st.write("Please enter a valid YouTube URL.")

resolution_options = st.radio("Resolution", ["144p", "360p", "480p", "720p", "1080p"], horizontal=True)
# Function to download video
def download_video(resolution):
    try:
        video_stream = yt.streams.filter(res=resolution, file_extension="mp4").first()
        if video_stream:
            video_stream.download()
            st.write(f"Download complete for {resolution} resolution.")
        else:
            st.write(f"Resolution {resolution} is not available for this video.")
    except Exception as e:
        st.write(f"Error: {e}")

# Buttons to trigger download for each resolution
if st.button("Download Video"):
    if yt:
        download_video(resolution_options)
    else:
        st.write("Please enter a valid YouTube URL first.")

st.divider()

# Button to download audio (MP3)
if st.button("Download MP3"):
    if yt:
        try:
            audio_stream = yt.streams.filter(only_audio=True).first()
            if audio_stream:
                audio_stream.download()
                st.write("Audio download complete.")
            else:
                st.write("No audio stream available.")
        except Exception as e:
            st.write(f"Error: {e}")
    else:
        st.write("Please enter a valid YouTube URL first.")