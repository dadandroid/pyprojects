#!/usr/bin/python
import imaplib
import smtplib
import email
import imp
import os
import picamera
import time

### send emails with attachments using local keys ###

#get local keys
if os.name == 'posix': root = "/home/pi/"
elif os.name == 'nt': root = os.path.abspath(os.sep)
mykeys = imp.load_source('module.name', root+'pykeys.py')

#client_email_user = mykeys.clients['david']


server_email = mykeys.ojeto_email_user
client_emails = []
client_names = []
current_time = time.strftime("%Y%m%d%H%M%S")
picname = None
picpath = None
ispictaken = False
isrequest = False

def checkmail():
    global isrequest
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    (retcode, capabilities) = mail.login(server_email, mykeys.ojeto_email_pass)
    mail.list()
    mail.select('inbox')
    (retcode, messages) = mail.search(None, '(UNSEEN)')
    n = 0
    if retcode == 'OK':

       for num in messages[0].split() :
          n=n+1
          typ, data = mail.fetch(num,'(RFC822)')
          ##do this for each message received
          for response_part in data:
             if isinstance(response_part, tuple):
                 if os.name == 'posix': original = email.message_from_string(response_part[1])
                 else: original = email.message_from_bytes(response_part[1])
                 from_email = original['From'].split('<')[-1].split('>')[0]
                 typ, data = mail.store(num,'+FLAGS','\\Seen')
                 if original['Subject'] == "damefoto":
                    if from_email in mykeys.clients.values():
                        isrequest = True
                        client_names.append(list(mykeys.clients.keys())[list(mykeys.clients.values()).index(from_email)])
                        client_emails.append(from_email)
    if n == 0: pass


def sendpic(client_email, client_name):

    msg = email.MIMEMultipart.MIMEMultipart()
    msg['From'] = server_email
    msg['To'] = client_email
    msg['Subject'] ='peticion de foto para {0} a las {1}'.format(client_name, current_time)

    body = "Hola %s. Aqui tienes tu foto"%(client_name)

    msg.attach(email.MIMEText.MIMEText(body, 'plain'))

    filename = picname
    attachment = open(picpath+picname, "rb")

    part = email.MIMEBase.MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    email.encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(server_email, mykeys.ojeto_email_pass)
    text = msg.as_string()
    server.sendmail(server_email, client_email, text)
    server.quit()

def take_pic():
    global picname
    global picpath
    picname = current_time + '.jpg'
    picpath = '/home/pi/pypics/'
    cam = picamera.PiCamera()
    cam.start_preview()
    time.sleep(2)
    cam.resolution = (2592, 1944)
    cam.vflip = True
    cam.hflip = True
    cam.capture(picpath+picname)
    cam.stop_preview()
    global ispictaken
    ispictaken = True



def sendMsg(email, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(server_email, mykeys.ojeto_email_pass)
    msg = message
    server.sendmail(server_email, email, msg)
    server.quit()

checkmail()
if isrequest:
    take_pic()
    if ispictaken:
        for i in range(len(client_emails)):
            try: sendpic(client_emails[i], client_names[i])
            except:
                msg = 'No he podido enviarte la foto. por favor intentalo nuevamente'
                sendmsg(client_emails[i], msg)
