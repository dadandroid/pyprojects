import imp
import os 
### send emails with attachments using local keys ###

if os.name == 'posix': root = "/home/pi/"    
elif os.name == 'nt': root = os.path.abspath(os.sep)
mykeys = imp.load_source('module.name', root+'pykeys.py')

print(mykeys.clients['david'])

server_mail_user = mykeys.ojeto_email_user
client_email_user = mykeys.clients['david']