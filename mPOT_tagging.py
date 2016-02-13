"""
Name: Tagging
Version: 1.0
Dependencies: TinyTag
Author: Samuel Steiner
Initial Release: February 12th 2016
Last: February 12th 2016
License: GPL
Description: A system which uses music files' (MP3, OGG, FLAC, and Wave) tags to rename and move files to be organized.
"""
from tinytag import TinyTag
from string import Template
import os

def meta_data_map(meta_data):
    m = meta_data
    meta_data_dict = dict(album = m.album, artist = m.artist, audio_offset = m.audio_offset, bitrate = m.bitrate,
                          disc = m.disc, disc_total = m.disk_total, duration = m.duration, filesize = m.filesize,
                          genre = m.genre, samplerate = m.samplerate, title = m.title, track = m.track,
                          track_total = m.track_total, year = m.year)
    return meta_data_dict


def derive_name(meta_data):
    try:
        f = open('name', 'r')
        name_temp = f.read()
        file_name_temp = Template(name_temp)
        key = meta_data_map(meta_data)
        file_name = file_name_temp.substitute(key)
        return file_name
    except:
        if os._exists('name'):
            print("Unkown Error")
        else:
            print("Name file missing")



def move_mass(input_folder, output_folder):
    tag = TinyTag
    for (a,b,c) in os.walk(input_folder):
        for x in c:
            song_loc = input_folder + "\\" + x
            file_meta = tag.get(song_loc)
            name = derive_name(file_meta)
