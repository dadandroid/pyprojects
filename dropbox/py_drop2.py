#!/usr/bin/env python
# -*- coding: utf-8 -*-
import dropbox
import sys 

file_name = sys.argv[1] #receive file name as an argument in command
file_from = '/home/pi/timelapse/' + file_name # The full path to upload the file to, including the root directory
file_to = '/timelapse/' + file_name  # The full path to upload the file to, including the file name


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

    access_token = 'access token here'
    print(file_name)
    writeFile("\n CRON event "+ file_name, "/home/pi/timelapse/cronlog.txt")
    transferData = TransferData(access_token)
    transferData.upload_file(file_from, file_to)
    writeFile(" >>> succesful!!", "/home/pi/timelapse/cronlog.txt")
   
if __name__ == '__main__':
    main()
