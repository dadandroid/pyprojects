#!/usr/bin/env python
# -*- coding: utf-8 -*-
import dropbox
import picamera
import time

def writeFile(something, text_file):

    with open(text_file,'a') as f:
        f.write(something)


class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
   
    picname = time.strftime("%Y%m%d-%H%M%S")+ '.jpg'
    picpath = '/home/pi/pypics/'+picname 
    print picpath

    cam = picamera.PiCamera()
    # cam.meter_mode = 'spot'
    cam.start_preview()
    time.sleep(2)
    cam.resolution = (2592, 1944)    
    cam.capture(picpath)
    cam.stop_preview()

    access_token = 'YsKVw9rI3lYAAAAAAACERn2NWdh-91mKsF6q6oB5AiDsYm3dDCu1Msv7c0dtjlVk'
    
    file_from = picpath
    file_to= '/' + picname
    writeFile("\n upload event "+ file_from, "/home/pi/uplaodlog.txt")
    transferData = TransferData(access_token)
    transferData.upload_file(file_from, file_to)
    writeFile(" >>> succesful!!", "/home/pi/uploadlog.txt")
    print("******* file uploaded! *******")
   
if __name__ == '__main__':
    main()
