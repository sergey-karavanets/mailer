import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template


FROM_EMAIL = 'good.test.man@gmail.com'
MY_PASSWORD = 'pejgekmfantjrsle'


def get_users(file_name):
    first_names = []
    last_names = []
    emails = []
    birthday = []
    with open(file_name, 'r') as user_file:
        for user_info in user_file:
            first_names.append(user_info.split()[0])
            last_names.append(user_info.split()[1])
            emails.append(user_info.split()[2])
            birthday.append(user_info.split()[3])
    return first_names, last_names, emails, birthday


def parse_template(file_name):
    with open(file_name, 'r') as msg_template:
        msg_template_content = msg_template.read()
    return Template(msg_template_content)


def main():
    first_names, last_names, emails, birthdays = get_users('contacts.txt')
    message_template = parse_template('message.txt')

    smtp_server = smtplib.SMTP(host=email_host, port=email_port)
    smtp_server.starttls()
    smtp_server.login(FROM_EMAIL, MY_PASSWORD)

    for first_name, last_name, email, birthday in zip(first_names, last_names, emails, birthdays):
        multipart_msg = MIMEMultipart()

        message = message_template.substitute(USER_FIRST_NAME=first_name.title(),
                                              USER_LAST_NAME=last_name.title(),
                                              USER_BDAY=birthday)

        multipart_msg['From'] = FROM_EMAIL
        multipart_msg['To'] = email
        multipart_msg['Subject'] = 'Subject'

        multipart_msg.attach(MIMEText(message, 'plain'))

        smtp_server.sendmail(multipart_msg['From'], multipart_msg['To'], multipart_msg.as_string())
        del multipart_msg

    smtp_server.quit()


if __name__ == '__main__':
    main()