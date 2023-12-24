FILENAME = 'nctu_emails.txt'


# The text file that contains many email addresses on e3

def get_dict():
    """
    Returns:
    email_dict (dict{str: str}): Dictionary holding username as key,
     domain name as value
    """
    email_dict = {}
    with open(FILENAME, 'r') as f:
        for line in f:
            email = line.split('@')
            username = email[0]
            domain_name = email[1].strip()
            email_dict[username] = domain_name
    return email_dict


def popular_domains(email_dict):
    """
    Input:
    email_dict (dict{str: str}): Dictionary holding username as key,
     domain name as value
    Returns:
    domain_dict (dict{str: List[str]}): Dictionary holding domain name
     as key, list of usernames as value
    """
    domain_dict = {}
    for username, domain_name in email_dict.items():
        if domain_name in domain_dict:
            domain_dict[domain_name].append(username)
        else:
            domain_dict[domain_name] = [username]
    return domain_dict


def main():
    print(get_dict())
    print(popular_domains(get_dict()))


if __name__ == '__main__':
    main()
