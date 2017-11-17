import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
import imp
import os

### send emails with attachments using local keys ###

#import key file
if os.name == 'posix': root = "/home/pi/"    
elif os.name == 'nt': root = os.path.abspath(os.sep)
mykeys = imp.load_source('module.name', root+'pykeys.py')

fromaddr = mykeys.ojeto_email_user
toaddr = mykeys.david_email_user
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "test mail for david"
 
body = "this is a test"
 
msg.attach(MIMEText(body, 'plain'))
 
filename = "20171116-223337.jpg"
attachment = open("/home/pi/pypics/20171116-223337.jpg", "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, mykeys.ojeto_email_pass)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
