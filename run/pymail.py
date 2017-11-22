import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("ojeto54@gmail.com", "CosmoCarretero0604")
 
msg = "TEST MESSAGE"
server.sendmail("ojeto54@gmail.com", "davidandresbcn@gmail.com", msg)
server.quit()
