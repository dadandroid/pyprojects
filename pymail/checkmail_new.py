import imaplib
import email

IMAP_server = 'imap.gmail.com'
user = 'ojeto54@gmail.com'
passw  = 'CosmoCarretero0604'

mail = imaplib.IMAP4_SSL('imap.gmail.com')
(retcode, capabilities) = mail.login(user,passw)
mail.list()
mail.select('inbox')

n=0
(retcode, messages) = mail.search(None, '(UNSEEN)')
if retcode == 'OK':

   for num in messages[0].split() :
      print('Processing ')
      n=n+1
      typ, data = mail.fetch(num,'(RFC822)')
      for response_part in data:
         if isinstance(response_part, tuple):
             original = email.message_from_bytes(response_part[1])
             print(original['From'])
             print (original['Subject'])
             print (original['Body'])
             typ, data = mail.store(num,'+FLAGS','\\Seen')

print (n)


