import tkinter as tk
from tkinter import *
from controller import *

def process_url():
    url = e1.get()
    url_processor(url)
    
def search_video_using_text():
    text = e2.get()
    audio_key_list, search_result_list = search_audio_using_text(text)
    for dict_val in search_result_list:
        val = dict_val['text']
        result_box_title.insert(END, f"{val:<6s}")
        result_box_title.insert(END,"\n")
    play_audio_using_path(audio_key_list[0])
    play_video_using_time_indices(search_result_list[0])


master = Tk()
master.title("Video Search - DEV")
master.geometry("1600x800")
Label(master, text='Video URL').grid(row=0, column=1)
e1 = Entry(master)
e1.grid(row=0, column=2)
    
# Create three buttons
button1 = tk.Button(master, text="AI Processing", command = process_url).grid(row=0, column=3)


Label(master, text=' Search Text').grid(row=1, column=1)
e2 = Entry(master)
e2.grid(row=1, column=2)
button2 = tk.Button(master, text="Video Search", command = search_video_using_text).grid(row=1, column=3)

result_box_title = Text(master, height = 40, width = 400, bg='#293241',fg='#ecfcff', relief=FLAT, font=('verdana 10', 10))
result_box_title.place(x= 3 , y= 100)

mainloop()