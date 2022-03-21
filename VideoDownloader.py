from pytube import YouTube
def videodownload(link):
    my_video = YouTube(link)
    # print("********************Download video*************************")
    # #get all the stream resolution for the 
    # '''for stream in my_video.streams:
    #     print(stream)
    # '''
    # #set stream resolution
    my_video = my_video.streams.get_highest_resolution()
    my_video.download()
    print("Download Complete")