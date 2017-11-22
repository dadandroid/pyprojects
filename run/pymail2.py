
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
 
 
fromaddr = "ojeto54@gmail.com"
toaddr = "davidandresbcn@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "OJETO ALERT!"
 
body = "This is an alert from ojetoPi"
msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "CosmoCarretero0604")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
