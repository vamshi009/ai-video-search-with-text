from moviepy.editor import *
import os
import cv2
from ffpyplayer.player import MediaPlayer

def save_subclip_2(path, start_time, end_time):

    files_list = []
    for (root, dir, files) in os.walk(path):
        for f in files:
            files_list.append(f)
    video_file = files_list[0]
    final_path = path + "/"  + video_file

    print(f"path to video file s {final_path} ")

    video = VideoFileClip(final_path).subclip(start_time, end_time)

    # Make the text. Many more options are available.
    txt_clip = ( TextClip("Video Search",fontsize=70,color='white')
                .set_position('center')
                .set_duration(10) )

    result = CompositeVideoClip([video, txt_clip]) # Overlay text on video
    result.write_videofile("VideoResult/myvideo.mp4",fps=25) # Many options...

def save_subclip(path, start_time, end_time):

    files_list = []
    for (root, dir, files) in os.walk(path):
        for f in files:
            files_list.append(f)
    video_file = files_list[0]
    final_path = path + "/"  + video_file

    print(f"path to video file s {final_path} ")

    clip = VideoFileClip(final_path)
    
    # getting subclip as video is large
    clip = clip.subclip(start_time, end_time)
    
    # saving the clip
    clip.write_videofile("VideoResult/myvideo.mp4")
    
    # showing clip
    #clip.ipython_display(width = 480)



def play_video_from_file():
    # Open the video file
    print("Attempting to play video")
    video_file = 'VideoResult/myvideo.mp4'
    cap = cv2.VideoCapture(video_file)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    # Read until video is completed
    while cap.isOpened():
        # Capture frame-by-frame
        ret, frame = cap.read()

        if ret:
            # Display the frame
            cv2.imshow('Video', frame)

            # Press 'q' on keyboard to exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break

    # Release the video capture object and close all windows
    cap.release()
    cv2.destroyAllWindows()

def play_video_with_audio():
    print("Attempting to play video")
    video_file = 'VideoResult/myvideo.mp4'

    video=cv2.VideoCapture(video_file)
    player = MediaPlayer(video_file)
    while True:
        grabbed, frame=video.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            print("End of video")
            break
        if cv2.waitKey(28) & 0xFF == ord("q"):
            break
        cv2.imshow("Video", frame)
        if val != 'eof' and audio_frame is not None:
            #audio
            img, t = audio_frame
    video.release()
    #cv2.destroyAllWindows()

