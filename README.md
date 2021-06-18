# Python module to extract features from media files with ffprobe (part of ffmpeg package)

- error handling
- one-liner
- easy to use JSON format
- may be used inside any project: Django, Tornado, Tryton, etc.

## How to use:

$ git clone https://github.com/TinKurbatoff/ffprobe-json

Then
```
    #python3
    from ffprobe_json import ffprobe

    ffprobe_result, error = ffprobe(file_path="/your/media_file.mp4", quiet=True)
    ## ffprobe_result — all info about media in JSON format

    ## Print in beauty format
    print(json.dumps(ffprobe_result, indent=2)) 

```

## To check how it works:

 $ git clone https://github.com/TinKurbatoff/ffprobe-json
 $ cd ffprobe-json
 $ python3 example.py -i "/your/media_file.mp4"

## Enjoy!
