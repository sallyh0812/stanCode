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
            eles = line.split('@')
            username = eles[0]
            domain = eles[1].strip()
            email_dict[username] = domain
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
    for domain in email_dict.values():
        if domain not in domain_dict:
            domain_dict[domain] = []
    for username, domain in email_dict.items():
        domain_dict[domain].append(username)
    return domain_dict

def main():
    print(get_dict())
    print(popular_domains(get_dict()))
    

if __name__ == '__main__':
    main()
