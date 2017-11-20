#!/usr/bin/python
import imaplib
import smtplib
import email
import imp
import os
import picamera
import time

### send emails with attachments using local keys ###
if os.name == 'posix': root = "/home/pi/"    
elif os.name == 'nt': root = os.path.abspath(os.sep)
mykeys = imp.load_source('module.name', root+'pykeys.py')

server_mail_user = mykeys.ojeto_email_user
client_email_user = mykeys.clients['david']

current_time = None
isPicTaken = False
client_email = None
client_name = None
picname = None
picpath = None

def checkmail():
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    (retcode, capabilities) = mail.login(server_mail_user, mykeys.ojeto_email_pass)
    mail.list()
    mail.select('inbox')
    (retcode, messages) = mail.search(None, '(UNSEEN)')
    n = 0
    if retcode == 'OK':
       for num in messages[0].split() :
          print('you got new mail!... ')
          n=n+1
          typ, data = mail.fetch(num,'(RFC822)')
          for response_part in data:
             if isinstance(response_part, tuple):
                 original = email.message_from_string(response_part[1])
                 print(original['From'])
                 print (original['Subject'])
                 from_= original['From']
                 from_email = from_.split('<')[-1].split('>')[0]
                 typ, data = mail.store(num,'+FLAGS','\\Seen')
                 
                 if original['Subject'] == "damefoto":                     
                    if from_email in mykeys.clients.values():
                        client_name = list(mydict.keys())[list(mydict.values()).index(from_email)]
                        client_email = from_email
                        print('new request from %d')%(client_name)                  
                        if take_pic(): 
                            print(picfile)
                            sendpic(client_email, picfile)
                            print('all done')
                        #else: sendMsg("sorry no pic available")
     

    if n == 0: print('sorry, no new mail')  


def sendpic():
    current_time = time.strftime("%Y%m%d%H%M%S")
    msg = email.MIMEMultipart.MIMEMultipart()
    msg['From'] = server_mail_user
    msg['To'] = client_email
    msg['Subject'] ='foto para {0}'.format(client_name)
 
    body = "Hola %d. Aqui tienes la foto que me pediste"%(client_name)
 
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
    server.login(server_mail_user, mykeys.ojeto_email_pass)
    text = msg.as_string()
    server.sendmail(server_mail_user, client_email_user, text)
    server.quit()

    print('email sent to {0}'.format(client_name))


def take_pic():
    picname = current_time + '.jpg'
    picpath = '/home/pi/pypics/'
    picfile = picpath + picname
    cam = picamera.PiCamera()
    cam.start_preview()
    time.sleep(2)
    cam.resolution = (2592, 1944)
    cam.vflip = True
    cam.hflip = True
    cam.capture(picpath+picname)
    cam.stop_preview()
    print('pic taken!')
    return True


def sendMsg(message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(server_mail_user, mykeys.ojeto_email_pass)
    msg = message
    server.sendmail(server_mail_user, mykeys.ojeto_email_pass, msg)
    server.quit()



checkmail()
