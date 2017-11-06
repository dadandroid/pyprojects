#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H%M")

fswebcam -r 960x720 --no-banner /home/pi/timelapse/$DATE.jpg
#fswebcam /home/pi/timelapse/$DATE.jpg
python /home/pi/david/dropbox/py_drop2.py $DATE.jpg
