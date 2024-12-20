import smtplib
from email.message import EmailMessage  #mail format ki use chestam
def sendmail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465) #465  & 587 is a port number 
    server.login('srihari.lanke7780@gmail.com','kixp xgxq rhyu bpqv')
    msg=EmailMessage()
    msg['FROM']='srihari.lanke7780@gmail.com'
    msg['TO']=to
    msg['Subject']=subject
    msg.set_content(body)
    server.send_message(msg)
    server.close()