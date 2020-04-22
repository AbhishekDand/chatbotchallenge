import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from wsgiref import simple_server
#from flask import Flask, request
#from flask import Response
import os
#from flask_cors import CORS, cross_origin

def lambda_handler(event, context):
    # TODO implement
    toaddr=event['currentIntent']['slots']['email']
    #toaddr = "abhi080497@gmail.com " ## email id of the user

    fromaddr = "pandaspython420@gmail.com"   ## the email id from where we are going to send the mail
    #mobile_number = request.json['mobile']
    #name = request.json['name']

            # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr
    # storing the receivers email address
    msg['To'] = ",".join(toaddr)
    # msg['To'] = toaddr
    # storing the subject
    msg['Subject'] = "CORONA SE DARONA"
    # string to store the body of the mail
    body = "Stay Home Stay Safe"
    #email_file = open("corona.html", "r")
    #email_message = email_file.read()

    # attach the body with the msg instance
    #msg.attach(MIMEText(email_message, 'html'))

    # open the file to be sent
    #filename = "projects.txt"
    #attachment = open(filename, "rb")

    # instance of MIMEBase and named as p
    #p = MIMEBase('application', 'octet-stream')

    # To change the payload into encoded form
    #p.set_payload((attachment).read())

    # encode into base64
    #encoders.encode_base64(p)

    #p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    # attach the instance 'p' to instance 'msg'
    #msg.attach(p)

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()
    # Authentication
    s.login(fromaddr,"pythonpandas420") # give your password here

    # Converts the Multipart msg into a string
    text = msg.as_string()
    # sending the mail
    s.sendmail(fromaddr, toaddr, text)

    # terminating the session
    s.quit()
    response={
        "dialogAction":{
            "type":"Close",
            "fulfillmentState":"Fulfilled",
            "message":{
                "contentType":"SSML",
                "content":"We have sent you the mail. Please let us know if you want any other details."
                
            },
        }
    }
    return response
