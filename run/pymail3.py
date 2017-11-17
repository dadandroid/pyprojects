import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
 
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
