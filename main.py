from __future__ import unicode_literals
import youtube_dl



def download(link : str = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley", format : str = "mp3", quality : str = "best"):
        if format =="mp3":#https://stackoverflow.com/questions/27473526/download-only-audio-from-youtube-video-using-youtube-dl-in-python-script
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }       
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])    
        
        
        
        
    
        
        
        
        
        
        
        


def convert_wav(link:str):
    pass