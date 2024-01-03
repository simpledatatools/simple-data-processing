import string
import random

def line(top=0, bottom=0, length=50, symbol='-'):
    
    for x in range(top):
        print('\n')
    text = ''
    for x in range(length):
        text = text + symbol
    print(text)
    for x in range(bottom):
        print('\n')


def check_status(response):
    status_code = response.status_code
    
    print('Response: ' + str(status_code))

    if status_code == 400:
        errors = response.json()
        print('Errors:')
        print('----------------')
        for error in errors['errors']:
            print(error)
        print('----------------')
        return False
    
    if status_code == 404:
        print('Errors:')
        print('----------------')
        print('Invalid url')
        print('----------------')
        return False

    if status_code == 405:
        print('Errors:')
        print('----------------')
        print('Wrong request type')
        print('----------------')
        return False
    
    if status_code == 500:
        print('Errors:')
        print('----------------')
        print('Server error')
        print('----------------')
        return False
    
    if status_code == 200:
        return True


def randomstr():
    return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k = 16))