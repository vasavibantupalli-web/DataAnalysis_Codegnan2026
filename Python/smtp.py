'''

import smtplib
from email.message import EmailMessage

msg = EmailMessage()
sender_email = 'vasavibantupalli@gmail.com'
sender_app_password = 'aauw cozv ksei vodv'
reciever_email = 'garikapatitejachowdary@gmail.com'

msg['from'] = sender_email
msg['to'] = reciever_email
msg['subject'] = 'python Mail'

msg.set_content("""
Hello,

welcome

regards,
python team
""")

with open('practiseprograms'.py,'rb')as file:
    file_content = file.read()
    msg.add_attachment(
    file_content,
    maintype='application',
    subtype='pdf',
    filename='practiseprograms.py'
  )
    
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender_email,sender_app_password)
server.send_message(msg)
server.quit()
print('Email sent successfully')
'''
import smtplib
from email.message import EmailMessage

msg = EmailMessage()
sender_email = 'vasavibantupalli@gmail.com'
sender_app_password = 'fkrl gvey adgk zvqa'
receiver_email = 'garikipatitejachowdhary@.com'

msg['from'] = sender_email
msg['to'] = receiver_email
msg['subject'] = 'python Mail'

msg.set_content("""
Hello,

This mail was sent Using python

Regards,
Python Team
""")

with open('practiseprograms.py','rb') as file:
    file_content = file.read()
    msg.add_attachment(
        file_content,
        maintype='application',
        subtype='pdf',
        filename='practiseprograms.py'
    )

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender_email,sender_app_password)
server.send_message(msg)
server.quit()
print('Email sent successfully')
