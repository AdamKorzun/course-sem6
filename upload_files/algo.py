import socket
from utils import Client
import time
user_list = {
    'user':'password',
    'test':'test',
    'hello':'world'
}
timeout_time = 60

if __name__ == '__main__':
    username = input('Username: ')
    password = input('Password: ')
    user = Client(username, password)
    #1
    timestamp = time.time()
    res = {username: user.hash().hexdigest()}
    print('1: ' + str(res))
    #2
    if res.keys()[0] in user_list:
        password = user_list[res.keys()[0]]
    else:
        print('user is not authenticated')
        return
