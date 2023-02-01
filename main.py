def get_users(file_name):
    names = []
    emails = []
    with open(file_name, 'r') as user_file:
        for user_info in user_file:
            names.append(user_info.split()[0])
            emails.append(user_info.split()[1])
    return names, emails

