"""
SMTP: Simple Mail Transfer Protocol


provider                        SMTP server domain name

Gmail(needs app password)       smtp.gmail.com
Yahoo mail                      smtp.mail.yahoo.com
Outlook/Hotmail                 smtp.mail.outlook.com
AT&T                            smtp.mail.att.net (use port 465)
"""


############ sending email
# import smtplib
# import getpass # to get input password as dots instead of letters for privacy
# # password = getpass.getpass('Password Please: ') # not working

# smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
# smtp_object.ehlo() # connect to server and establish the connection
# smtp_object.starttls()


# # Note for Gmail Users, you need to generate an app password instead of your normal email password. 
# # https://support.google.com/accounts/answer/185833?sjid=9824805264479621536-EU#app-passwords
# # https://myaccount.google.com/apppasswords?pli=1&rapt=AEjHL4OwcIObBZjq-bep082CIQoATiEOJvKe6ArmyTNYaBgwRaadAOHOw1cvEOCQwvQ0KRfysnixOSOLgbbL6S7ajsDgTxL8ncUQvcbLv5pQO5WZtgA3NRI
# # This also requires enabling 2-step authentication.

# email = input("Enter your email: ") # abdowahbah@gmail.com
# password = input('Password please: ') # gnuf eeps nkdo lprt
# smtp_object.login(email,password)

# from_address = email
# to_address = email
# subject = 'Bye Bye'
# message = "This is to inform you bye bye"
# msg = 'Subject: '+subject+'\n'+message
# smtp_object.sendmail(from_address, to_address, msg)





############ receiving emails

import imaplib

M = imaplib.IMAP4_SSL('imap.gmail.com') # 'imap.gmail.com': imap server for gmail
# user = input("Enter your email: ") # abdowahbah@gmail.com
# password = input('Password please: ') # gnuf eeps nkdo lprt
user = 'abdowahbah@gmail.com'
password = 'gnuf eeps nkdo lprt'
M.login(user,password)
# print(M.list())
M.select('inbox')
# print(M.select('inbox'))
# typ, data = M.search(None,'SUBJECT "this is a test email for python"')
typ, data = M.search(None,'FROM "Indeed"')
print(data)

result, email_data = M.fetch(data[0],"(RFC822)")
raw_email = email_data[0][1]
raw_email_string = raw_email.decode('utf-8')
print(raw_email_string)

# We can use the built in email library to help parse this raw string.


import email
email_message = email.message_from_string(raw_email_string)
for part in email_message.walk():
    if part.get_content_type() == "text/plain":
        body = part.get_payload(decode=True)
        print(body)