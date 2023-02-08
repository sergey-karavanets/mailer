# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.mail import EmailMessage, get_connection
from django.conf import settings
from string import Template


# Create your views here.


def data_acquisition(request):
    data_from_form = request.POST.get('email')
    user_info = open('user_info.txt', 'w')
    for user in data_from_form:
        user_info.write(user)
    user_info.close()


def template_loading(request):
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
        return Template(handle_uploaded_file(request.FILES['file']))


def handle_uploaded_file(template):
    with open('mail_sender/mail/new_template.txt', 'w') as new_template:
        for chunk in template.chunks():
            new_template.write(chunk)
    with open('mail_sender/mail/message.txt', 'r') as new_template:
        message = new_template.read()
    return message


def send_emails(request):
    if request.method == "POST":
        with get_connection(
                host=settings.EMAIL_HOST,
                port=settings.EMAIL_PORT,
                username=settings.EMAIL_HOST_USER,
                password=settings.EMAIL_HOST_PASSWORD,
                use_tls=settings.EMAIL_USE_TLS
        ) as connection:
            subject = request.POST.get('subject')
            email_from = settings.EMAIL_HOST_USER
            data_acquisition(request)
            with open('mail_sender/mail/message.txt', 'r') as message_file:
                message = Template(message_file.read())
                with open('user_info.txt', 'r') as users_file:
                    for user_info in users_file:
                        email = [user_info.split()[0]]
                        first_name = user_info.split()[1]
                        last_name = user_info.split()[2]
                        birthday = user_info.split()[3]
                        personalized_message = message.substitute(USER_FIRST_NAME=first_name.title(),
                                                                  USER_LAST_NAME=last_name.title(),
                                                                  USER_BDAY=birthday)
                        msg = EmailMessage(subject, personalized_message, email_from, email, connection=connection)
                        msg.content_subtype = 'html'
                        msg.send()

    return render(request, 'mail/send_emails.html')
