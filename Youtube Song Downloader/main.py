import urllib.request
import re
from pytube import YouTube





def searchFilter(songName):
    brokenSong = songName.split(" ")
    print(brokenSong)
    finalSongName = ''
    for x in range(len(brokenSong)):
        
        if(x==0):
            finalSongName += brokenSong[x]
        else:
            finalSongName+="+"+ brokenSong[x]

        
    return finalSongName


def getVideoUrl(songName):
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + songName)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    print("https://www.youtube.com/watch?v=" + video_ids[0])
    return "https://www.youtube.com/watch?v=" + video_ids[0]

def downloadTheVideoSong(songURL):
    youtube_video_url = songURL
    try:
        yt_obj = YouTube(youtube_video_url)
        
        print(f'Video Title is {yt_obj.title}')
        print(f'Video Length is {yt_obj.length} seconds')
        print(f'Video Description is {yt_obj.description}')
        print(f'Video Rating is {yt_obj.rating}')
        print(f'Video Views Count is {yt_obj.views}')
        print(f'Video Author is {yt_obj.author}')
    
    
        yt_obj.streams.get_audio_only().download(output_path='downloads/audio', filename=yt_obj.title)
        print('YouTube video audio downloaded successfully')
    except Exception as e:
        print(e)

def downloadVideo(songURL):
    youtube_video_url = songURL
    try:
        yt_obj = YouTube(youtube_video_url)

        print(f'Video Title is {yt_obj.title}')
        print(f'Video Length is {yt_obj.length} seconds')
        print(f'Video Description is {yt_obj.description}')
        print(f'Video Rating is {yt_obj.rating}')
        print(f'Video Views Count is {yt_obj.views}')
        print(f'Video Author is {yt_obj.author}')
    
        filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')
    
        # download the highest quality video
        filters.get_highest_resolution().download(output_path='downloads/video',filename=yt_obj.title)
        print('Video Downloaded Successfully')
    except Exception as e:
        print(e)

def getSongsFromText():
    f = open('songList/songs.txt',"r")
    songsList = []
    for lines in f:
        newLine = lines.replace("\n","")
        songNameFromLine = searchFilter(newLine)
        songsList.append(songNameFromLine)
    
    print('Emptying the file')
    w = open('songList/songs.txt',"w")
    w.write("")

    print(songsList)
    return songsList

def downloadSongFromList(songList):
   
    for x in songList:
        y = getVideoUrl(x)
        downloadTheVideoSong(y)
       

def downloadVideoFromList(songList):

    for x in songList:
        y = getVideoUrl(x)
        downloadVideo(y)


if __name__=="__main__":
    songsList = getSongsFromText()
    #Enter name of songs line by line in songList/songs.txt
    #Uncomment one for required purpose
    # downloadSongFromList(songsList)
    downloadVideoFromList(songsList)


    








