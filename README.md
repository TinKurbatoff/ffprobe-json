# Python module to extract features from media files with ffprobe (part of ffmpeg package)

- error handling
- one-liner
- easy to use JSON format
- may be used inside any project: Django, Tornado, Tryton, etc.
- making video thumbnails

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
    
    ## Create a 3 sec thumbnail from the middle of the video
    video_duration_in_seconds = int(round(float(video_data['format']['duration']),0))
    thumbnail_file = ffprobe_thumbnail(file_path="/your/media_file.mp4", 
                    output_image="/foo/bar.gif",
                    seconds=int(round(video_duration_in_seconds/2,0)),
                    )

```

## To check how it works:

```
$ git clone https://github.com/TinKurbatoff/ffprobe-json
$ cd ffprobe-json
$ python3 example.py -i "/your/media_file.mp4"
```

## Enjoy!
