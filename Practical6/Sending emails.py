# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 18:14:00 2019

@author: KANG Jianning
"""


#define the function of sending e-mails
def send(x, y, z, content,mail_pass):
    import smtplib
    from email.mime.text import MIMEText
    from email.header import Header

    mail_host="smtp.zju.edu.cn"  
    mail_user="3180112702"      
 
    sender = '3180112702@zju.edu.cn'
    receivers = y  
 

    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = Header('Edison', 'utf-8')   
    message['To'] =  Header(x, 'utf-8')        
 
    subject = z
    message['Subject'] = Header(subject, 'utf-8')
 
 
    try:
        smtpObj = smtplib.SMTP() 
        smtpObj.connect(mail_host, 25)
        smtpObj.login(mail_user,mail_pass)  
        smtpObj.sendmail(sender, receivers, message.as_string())
        print ('Mail sent successfully!')
    except smtplib.SMTPException:
        print ("Error: Mail failed to send")


#define legeal e-mail address and send e-mails
import re
import pandas as pd
data=pd.read_csv('address_information.csv')
with open ('body.txt', 'r')as show:
    show=show.read()
mail_pass=input('Password:')
for line in data.values:
    if not re.match(r'\S+@\S+\.com$', line[1]):
        print(line[1], ':Wrong Address!')
        continue
    print (line[1], ':Correct Address!')
    display=re.sub(r'User', line[0], show)
    send(line[0], line[1], line[2], display,mail_pass)





