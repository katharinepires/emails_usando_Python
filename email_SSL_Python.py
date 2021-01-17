#!/usr/bin/env python
# coding: utf-8

# # Como enviar emails simples utilizando Python

# In[1]:


import smtplib as smtp


# In[2]:


def enviar_email(by, password, to, msg):
    by = 'kkathy1999.kp@gmail.com'
    password = 'xxxx'
    to = "katharinepires@outlook.com"
    msg = "Subject: A test \n\nA mail sent through Python. Let's see if it worked!"
    
    try:
        with smtp.SMTP_SSL('smtp.gmail.com', 465) as s:
            s.login(by, password) 
            s.sendmail(by, to, msg)
            s.close()
        print("Email successfelly sent!")
    except Exception as erro:
        print("It was not possible to send the email. Try again!", erro)
        
if __name__ == '__main__':
    enviar_email()

