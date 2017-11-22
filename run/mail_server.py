import imaplib
import email
import picamera
import time
import smtplib

#datos del la cuenta servidor
server_mail_user= "ojeto54@gmail.com"
server_mail_pass= "CosmoCarretero0604"

#datos del cliente
client_email_user='davidandresleon@gmail.com'


#global variables
current_time = None
picname = None
picpath = None
isPicTaken = False

def checkmail():
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    (retcode, capabilities) = mail.login(server_mail_user,server_mail_pass)
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
                 #print(original['From'])
                 #print (original['Subject'])
                 from_= original['From']
                 from_email = from_.split('<')[-1].split('>')[0]
                 typ, data = mail.store(num,'+FLAGS','\\Seen')

                 if original['Subject'] == "damefoto":                     
                    if from_email == client_email_user: 
                        print('its david')
                        take_pic()
                        if isPicTaken: send_pic(picname, picpath)
                        print("done")
                        #else: send_msg("sorry no pic available")
                 #else: send_msg("you don't know the password!") 
                           
    if n == 0: print('sorry, no new mail')  


def take_pic():
    
    current_time = time.strftime("%Y%m%d-%H%M%S")
    picname = current_time + '.jpg'
    picpath = '/home/pi/pypics/'
    cam = picamera.PiCamera()
    # cam.meter_mode = 'spot'
    cam.start_preview()
    time.sleep(2)
    cam.resolution = (2592, 1944)
    cam.vflip = True
    cam.hflip = True
    cam.capture(picpath+picname)
    cam.stop_preview()
    time.sleep(2)
    print ("picture " + picpath+picname + " taken!") 
    isPicTaken = True


def send_pic(pic_name, pic_path):
    fromaddr = server_mail_user
    toaddr = client_email_user

    email_subj = "toma tu foto " + current_time
    email_text =  "foto tomada: " + current_time

    msg = email.MIMEMultipart()
 
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = email_subj
 
    body = email_text
 
    msg.attach(email.MIMEText(body, 'plain'))
 
    filename = pic_name
    attachment = open(pic_path+pic_name, "rb")
 
    part = email.MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    email.encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
    msg.attach(part)
 
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.login(fromaddr, server_mail_pass)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    print("picture sent!")


def send_msg(message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(server_mail_user, server_mail_pass)
    msg = message
    server.sendmail(server_mail_user, server_mail_pass, msg)
    server.quit()
   
def send_pic2():

    fromaddr = "ojeto54@gmail.com"
    toaddr = "davidandresbcn@gmail.com"

    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
msg['Subject'] = "ojetomail test with attachment"

body = "ojetomail test message"

msg.attach(MIMEText(body, 'plain'))

filename = "uploadlog.txt"
attachment = open("/home/pi/uploadlog.txt", "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "CosmoCarretero0604")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()





    
checkmail()

