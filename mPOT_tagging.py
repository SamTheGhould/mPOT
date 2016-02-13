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
import tkFileDialog
import os
import unicodedata


def meta_data_map(meta_data):
    u = unicodedata.normalize
    m = meta_data
    meta_data_dict = dict(album=u('NFKD', m.album).encode('ascii', 'ignore'),
                          artist=u('NFKD', m.artist).encode('ascii', 'ignore'),
                          audio_offset=m.audio_offset,
                          bitrate=m.bitrate,
                          disc=m.disc,
                          duration=m.duration,
                          filesize=m.filesize,
                          genre=u('NFKD', m.genre).encode('ascii', 'ignore'),
                          samplerate=m.samplerate,
                          title=u('NFKD', m.title).encode('ascii', 'ignore'),
                          track=m.track,
                          track_total=m.track_total,
                          year=m.year)
    return meta_data_dict


def derive_name(meta_data):
    # print meta_data.artist
    f = open('name', 'r')
    name_temp = f.read()
    file_name_temp = Template(name_temp)
    key = meta_data_map(meta_data)
    file_name = file_name_temp.substitute(key)
    return file_name




def move_mass(input_folder, output_folder):
    tag = TinyTag
    for (a, b, c) in os.walk(input_folder):
        for x in c:
            # print x
            file_type = x.split('.')[1]
            # print file_type
            song_loc = input_folder + "\\" + x
            file_meta = tag.get(song_loc)
            name = derive_name(file_meta)
            artist = unicodedata.normalize('NFKD', file_meta.artist).encode('ascii','ignore')
            album = unicodedata.normalize('NFKD', file_meta.album).encode('ascii','ignore')
            out_path = output_folder + "\\" + artist + "\\" + album
            # print name
            final_name = out_path + "\\" + name + '.' + file_type
            if not os.path.exists(out_path):
                os.makedirs(out_path)
                if not os.path.isfile(final_name):
                    os.rename(song_loc, out_path + "\\" + name + '.' + file_type)
                else:
                    os.remove(song_loc)
            else:
                if not os.path.isfile(final_name):
                    os.rename(song_loc, out_path + "\\" + name + '.' + file_type)
                else:
                    os.remove(song_loc)


def main():
    input = tkFileDialog.askdirectory( initialdir="/", title="select unorganized media")
    output = tkFileDialog.askdirectory( initialdir="/", title="select output")
    move_mass(input, output)

main()
