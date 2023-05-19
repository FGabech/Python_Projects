''' Steps to send emails with Gmail
1. Go to Gmail account and setup 2 factor autentication
2. Generate password
3. Create a function to send the email
'''

from email.message import EmailMessage #Pré instalado no Python
import ssl
import smtplib

email_sender = 'fgabech@gmail.com'
email_password = password #use here the gmail password

email_receiver = 'pgabech@gmail.com' #['fgabech@hotmail.com', 'lgabech@hotmail.com', 'dani_marreco@hotmail.com']

subject = "Teste email Python!"
body = '''
Teste de email enviado com bot em Python, 
Favor desconsiderar.
                        Desde já,
                        Obrigado
'''

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

