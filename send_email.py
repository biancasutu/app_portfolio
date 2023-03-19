import smtplib
import ssl
import os

# used to write scripts to send emails
# needs parameters: host, port


def send_email(message):
    host = 'smtp.gmail.com'
    port = 465
    username = 'bianca.andreea.sutu@gmail.com'
    password = os.getenv('PASSWORD')   # access the operating system and gets the pwd from the environment variable
    receiver = 'akrasia04@gmail.com'
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


# SMTP = Simple Mail Transfer Protocol -> used to send and receive email
# SSL = Secure Socket Layer -> establish an encrypted link between a server and the client

# ENVIRONMENT VARIABLES -> for password security
# Steps: import os, create environment variable
# Create ENVIRONMENT VARIABLE steps:
# - start, search: environment variables, env var,
# -user variables: new, var name = 'PASSWORD', var value = the actual pwd
# lecture 232
