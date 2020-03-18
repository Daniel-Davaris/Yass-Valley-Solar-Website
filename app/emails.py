# from threading import Thread
# from flask import render_template
# from flask_mail import Message
# from app import app, mail
# from config import ADMINS




# def send_email(subject, sender, recipients, text_body, html_body):
#     msg = Message(subject, sender=sender, recipients=recipients)
#     msg.body = text_body
#     msg.html = html_body
#     mail.send(msg)

# def email_activation(name, email, subject, message):
#     print(name)
#     print(email)
#     send_email("Test email !!!!!!!!!", ADMINS[0], [ADMINS[0]],render_template("email.html", name=name, email=email, subject=subject, message=message), render_template("email.html", name=name, email=email, subject=subject, message=message))
    

