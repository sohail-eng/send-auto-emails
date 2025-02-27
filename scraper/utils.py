def get_valid_email(profile):
    email_file = f"emails-{profile}.txt"
    try:
        with open(email_file, "r") as file:
            emails_data = file.read()
    except FileNotFoundError:
        emails_data = ""
    emails_data = emails_data.split("\n")
    emails_data = [
        email_data.strip() for email_data in emails_data if email_data.strip()
    ]
    email_data = emails_data[0] if emails_data else ""
    emails_data = emails_data[1:]
    temp_data = emails_data
    emails_data = []
    for item in temp_data:
        if item.strip() != "":
            emails_data.append(item)
    emails_data = "\n".join(emails_data)
    with open(email_file, "w") as file:
        file.write(emails_data)
    return email_data


def remove_valid_email(profile, email: str):
    email_file = f"emails-{profile}.txt"
    try:
        with open(email_file, "r") as file:
            emails_data = file.read()
    except FileNotFoundError:
        emails_data = ""
    emails_data = emails_data.split("\n")
    emails_data.remove(email)
    temp_data = emails_data
    emails_data = []
    for item in temp_data:
        if item.strip() != "":
            emails_data.append(item)
    emails_data = "\n".join(emails_data)
    with open(email_file, "w") as file:
        file.write(emails_data)


def __write_email(email: str, file_path: str):
    try:
        with open(file_path, "r") as file:
            emails_data = file.read()
    except FileNotFoundError:
        emails_data = ""
    emails_data = emails_data.split("\n")
    emails_data.append(email)
    temp_data = emails_data
    emails_data = []
    for item in temp_data:
        if item.strip() != "":
            emails_data.append(item)
    emails_data = "\n".join(emails_data)
    with open(file_path, "w") as file:
        file.write(emails_data)


def write_used_email(profile, email):
    __write_email(email=email, file_path=f"emails_used-{profile}.txt")
