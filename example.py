#!/usr/bin/python3
import json
import argparse
import os

from ffprobe_json import ffprobe


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='View ffprobe output in json format')
    parser.add_argument('-i', '--input', help='File Name', required=True)
    args = parser.parse_args()
    if not os.path.isfile(args.input):
        print("could not read file: " + args.input)
        exit(1)
    print(f'File: {args.input}')
    # (quiet=True) —suppress error output of ffprobe
    ffprobe_result, error = ffprobe(file_path=args.input, quiet=False)

    ## Print beauty format
    print(json.dumps(ffprobe_result, indent=2)) 
    print(error)



