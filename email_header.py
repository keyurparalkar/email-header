#!/usr/bin/env python

import imaplib,getpass

mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)
USER = raw_input("email address:")
PASSWORD = getpass.getpass()
		

mail.login(USER, PASSWORD)
mail.select('Inbox')

status, data = mail.search(None, 'ALL')
for num in data[0].split():
    status, data = mail.fetch(num, '(RFC822)')
    print 'Message %s\n%s\n' % (num, data[0][1])
   
mail.close()
mail.logout()
