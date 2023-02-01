def get_users(file_name):
    names = []
    emails = []
    with open(file_name, 'r') as user_file:
        for user_info in user_file:
            names.append(user_info.split()[0])
            emails.append(user_info.split()[1])
    return names, emails


def parse_template(file_name):
    with open(file_name, 'r') as msg_template:
        msg_template_content = msg_template.read()
    return Template(msg_template_content)


def main():
    names, emails = get_users('contacts.txt')
    message_template = parse_template('message.txt')

    smtp_server = smtplib.SMTP(host='host_address', port=port_here)
    smtp_server.starttls()
    smtp_server.login(my_mail, my_password)