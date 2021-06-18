#!/usr/bin/python3
import subprocess
import json
import os
"""
   Parsing video parameters from ffprobe
"""

def ffprobe(file_path, quiet=True):
    if os.path.isfile(file_path):
        v_option = 'quiet' if quiet else ''  # turn on quiet 
        command_line = ['ffprobe', '-v', v_option, '-print_format', 'json', '-show_format', '-show_streams', f"{file_path}"] 
        p = subprocess.Popen(command_line, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # print(file_path) # * Sanity check *
        out, err =  p.communicate()
        if len(out)>0:
            result = json.loads(out)
        else:
            result = {}
        err_json = {'error':err} if err else {'error':None}
        return result, err_json
    else:
        return {},{'error':'File not found'}

if __name__ == '__main__':
    print("This is the module for ffprobing media files" )