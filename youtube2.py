import yt_dlp
import streamlit as st

st.write("# YouTube Video Downloader")

# Text input for the video link
video_link = st.text_input("Paste the video link here to download video", value="https://youtu.be/-pSf9_MgsZ4")

# Radio buttons for resolution options
resolution_options = st.radio("Select Resolution", ["144p", "360p", "480p", "720p", "1080p"], horizontal=True)

def download_video(url, resolution):
    ydl_opts = {
        'format': f'bestvideo[height<={resolution[:-1]}]+bestaudio/best[height<={resolution[:-1]}]',
        'outtmpl': '%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if st.button("Download Video"):
    if video_link:
        download_video(video_link, resolution_options)
    else:
        st.write("Please enter a valid YouTube URL first.")

st.divider()

if st.button("Download MP3"):
    if video_link:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_link])
    else:
        st.write("Please enter a valid YouTube URL first.")
