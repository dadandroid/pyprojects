#!/usr/bin/env python
# -*- coding: utf-8 -*-
import dropbox
import sys 

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

    access_token = 'YsKVw9rI3lYAAAAAAACERn2NWdh-91mKsF6q6oB5AiDsYm3dDCu1Msv7c0dtjlVk'
    
    file_from = sys.argv[1]
    file_to= '/' + file_from
    writeFile("\n upload event "+ file_from, "/home/pi/uplaodlog.txt")
    transferData = TransferData(access_token)
    transferData.upload_file(file_from, file_to)
    writeFile(" >>> succesful!!", "/home/pi/uploadlog.txt")
    print("******* file uploaded! *******")
   
if __name__ == '__main__':
    main()
