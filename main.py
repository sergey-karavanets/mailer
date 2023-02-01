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