import string
import getpass

def check_pwd(password):
    strength = 0
    remarks = ''
    lower_count = 0
    upper_count = 0
    num_count = 0
    special_count = 0
    wspace_count = 0

    for char in password:
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits: 
            num_count += 1
        elif char in string.punctuation:
            special_count += 1
        elif char == ' ':
            wspace_count += 1
    
    # Count types of characters
    if lower_count >= 1:
        strength += 1
    if upper_count >= 1:
        strength += 1
    if num_count >= 1:
        strength += 1
    if special_count >= 1:
        strength += 1

    # Length
    length = len(password)
    if length < 8:
        remarks = ' Very Bad Password'
    elif length < 10:
        remarks = ' Bad Password'
    elif length < 12:
        remarks = ' Medium Password'
    elif length < 14:
        remarks = ' Good Password'
    else:
        remarks = ' Very Good Password'

    # Feedback
    print('Your Password has: ')
    print(f"{upper_count} uppercase characters")
    print(f"{lower_count} lowercase characters")
    print(f"{num_count} numeric characters")
    print(f"{special_count} special characters")
    print(f"{wspace_count} whitespace characters")
    print(f"Password Strength: {strength} / 4")
    print(f"Length: {length} characters")
    print(f"Remarks: {remarks}")

def ask_pwd():
    while True:
        password = getpass.getpass('Enter the Password: ')
        check_pwd(password)
        choice = input('Do You Want to Enter another Password (Yes/No): ')
        if choice.lower() != 'y':
            break

if __name__ == '__main__':
    print('++ Welcome to Password checker +++')
    ask_pwd()
