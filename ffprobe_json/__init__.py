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
        # out.read()
        # err.read()
        return result, err_json
    else:
        return {},{'error':'File not found'}

def ffprobe_thumbnail(file_path, output_image=None, seconds=0):
    if os.path.isfile(file_path):
        if not output_image:
            # output_image = f"{file_path}.jpg"    
            output_image = f"{file_path}.gif"    
        print('[FFTHUMB] output_image path:',output_image)
        if (seconds < 3):
            cl_length = seconds
        else:
            cl_length = 3
        command_line = ['ffmpeg',
                    '-nostdin',
                    '-ss', f'{seconds}' ,
                    '-v','quiet',
                    '-t', f'{cl_length}' ,
                    '-i', file_path, 
                    '-vf', "fps=10,scale=320:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" ,
                    '-loop', '0',
                    output_image]
        print(command_line)
        # p = subprocess.Popen(['ffmpeg', '-i', file_path,'-v','quiet', '-an', '-ss', f'{seconds}', '-vframes', '1', output_image])
        p = subprocess.Popen(command_line)
        out, err =  p.communicate()
        # out.read()
        # err.read()
        # print("====== OUT ======")
        # print(out)        
        # print("====== ERR ======")
        # print(err)
        return output_image
    else:
        return {'error':'File not found'}

if __name__ == '__main__':
    print("This is the module for ffprobing media files" )