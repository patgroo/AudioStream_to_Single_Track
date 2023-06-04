import psutil,random
from pywinauto import Desktop
from time import sleep as s
import datetime

def get_song_name():
    try:
        mylist=[]
        for proc in psutil.process_iter():
            if proc.name() == 'Spotify.exe':
                mylist.append(proc.as_dict(attrs=['pid','num_threads'])) #windows only: 'num_handles'
        song_name_raw=[w.window_text() for w in Desktop(backend='uia').windows(process=int(max(mylist, key=lambda x: x['num_threads'])['pid']))][0]
    except:
        input('Spotify not found; Press Enter once you have started Spotify back up...')
    if song_name_raw not in ('Spotify Free', 'Spotify Premium'):
        song_name=str(song_name_raw)
        print(song_name, datetime.datetime.now())
        with open('textfiles/song_name.txt', 'w', encoding='utf-8') as o:o.write(song_name)
        return song_name

def convert_str_datetime(str):
    date_format = "%Y-%m-%d %H:%M:%S.%f"
    datetime_obj = datetime.datetime.strptime(str, date_format)
    return datetime_obj
    
def get_duration(t1,t2):
    dur = t2 - t1
    return dur
           
def write_txt_files(song_name):
    print(datetime.datetime.now())
    with open('textfiles/current_song.txt', 'w', encoding='utf-8') as o:
        o.write(song_name)
    with open('textfiles/song_list.txt', 'a', encoding='utf-8') as o:
        o.write(song_name+"§"+str(datetime.datetime.now())+'\n')
    
def get_song_duration_from_txt(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            if song_name in line:
                print(song_name)

def get_list_from_txt(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        return lines
                
def get_info_from_string(string):
    dash_index = string.index(" - ")
    section_index = string.index("§")
    artist = string[:dash_index]
    songname = string[dash_index+3:section_index-1]
    timestamp = string[section_index+1:]
    return artist, songname, timestamp


#print(convert_str_datetime("2023-06-04 23:53:22.440893"))
#"2023-06-04 23:53:32.579881"
write_txt_files(get_song_name())
#get_song_duration_from_txt('song_list.txt')
#print(get_info_from_string("French 79 - Memories§2023-06-05 00: 12: 51.797745"))
f = 'textfiles/song_list.txt'

def song_list_to_clean_list(txt):
    def add_to_clean_list(artist, line_songname, timestamp):
        with open('textfiles/clean_song_list.txt', 'a', encoding='utf-8') as o:
            o.write(artist + line_songname +'\n')
            
    for line in get_list_from_txt(txt):
        artist, line_songname, timestamp = get_info_from_string(line)
        
        if "old_songname" in locals():
            if line_songname != old_songname:
                old_songname = line_songname
                add_to_clean_list(artist, line_songname, timestamp)
            
        elif "old_songname" not in locals():
            old_songname = line_songname
            add_to_clean_list(artist, line_songname, timestamp)

song_list_to_clean_list(f)