#!/usr/bin/python3

##################################
#
#   Web: https://github.com/DesobedienteTecnologico
#   Authors: Jaime Roque
#
#   License: Unlicense
#
##################################


import os
import sys


# Variables
ffmpeg_options = '-vcodec libx264 -crf 24'
file_extension = '.mp4'
dir_files = sys.argv[1]

for dirpath, dirs, files in os.walk(dir_files):  # Using os.walk() with the argument received from the variable dir_files
  for filename in files: 
    fname = os.path.join(dirpath,filename) 
    if fname.endswith('.mp4'): # Get file that ends with .mp4
      fname_space = fname.replace(' ', '\ ') # Replace spaces with '\ '
      fname_extension = fname_space.replace(f'{file_extension}', 'NEW.mp4') # Replace the file_extension with 'NEW.mp4'
      os.system(f'ffmpeg -i {fname_space} {ffmpeg_options} {fname_extension}') # Execute the ffmpeg command
      os.system(f'rm {fname_space}') # Delete the old file
