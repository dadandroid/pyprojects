import smtplib
import time
import imaplib
import email

# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------

def read_email_from_gmail():
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('inbox')

        type, data = mail.search(None, 'ALL')
        mail_ids = data[0]

        id_list = mail_ids.split()   
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])


        for i in range(latest_email_id,first_email_id, -1):
            typ, data = mail.fetch(i, '(RFC822)' )

            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_string(response_part[1])
                    email_subject = msg['subject']
                    email_from = msg['from']
                    print 'From : ' + email_from + '\n'
                    print 'Subject : ' + email_subject + '\n'

    except Exception, e:
        print str(e)




def checkmail():
    IMAP_server = #IMAP SERVER
    user = #username
    pass = #password

    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    (retcode, capabilities) = mail.login(user,pass)
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
                 typ, data = mail.store(num,'+FLAGS','\\Seen')

    print (n)

