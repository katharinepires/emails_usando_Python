#!/usr/bin/env python
# coding: utf-8

# In[1]:


import smtplib as smtp


# In[2]:


def enviar_email(by, password, to, msg):
    by = 'kkathy1999.kp@gmail.com'
    password = '****'
    to = 'katharinepires@outlook.com'
    msg = "Subject: Enviando usando criptografia TSL \n\nEmail enviado do Python e cripitografado!"
    
    try:
        with smtp.SMTP('smtp.gmail.com', 587) as s:
            s.starttls()
            s.login(by, password) 
            s.sendmail(by, to, msg)
            s.close()
        print("Email successfelly sent!")
    except Exception as erro:
        print("It was not possible to send the email. Try again!", erro)
        
if __name__ == '__main__':
    by = 'kkathy1999.kp@gmail.com'
    password = '****'
    to = 'katharinepires@outlook.com'
    msg = "Subject: Enviando usando criptografia TSL \n\nEmail enviado do Python e cripitografado!"
    enviar_email(by, password, to, msg)

