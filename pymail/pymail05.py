import smtplib
import email
import imp
import os

### send emails with attachments using local keys ###

#import key file
if os.name == 'posix': root = "/home/pi/"    
elif os.name == 'nt': root = os.path.abspath(os.sep)
mykeys = imp.load_source('module.name', root+'pykeys.py')

fromaddr = mykeys.ojeto_email_user
toaddr = mykeys.david
 
msg = email.MIMEMultipart.MIMEMultipart()


msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] ='foto para {0}'.format(toaddr)
 
body = "Hola Belen soy el OjetoBot me podrias confirmar si te llego una imagen?"
 
msg.attach(email.MIMEText.MIMEText(body, 'plain'))
 
filename = "20171116-223337.jpg"
attachment = open("/home/pi/pypics/20171116-223337.jpg", "rb")
 
part = email.MIMEBase.MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
email.encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, mykeys.ojeto_email_pass)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

print('email sent to {0}'.format(toaddr))
