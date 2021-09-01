from NetworkInterface import NetworkInterface
import hashlib
import sys


# get password from user
if len(sys.argv) < 2:
    print('error input! exec format: main.py <password>')
    exit()
real_pwd = sys.argv[1]


# check if its pwned
# 1. get hashed real-pwd and the first 5 digit
hashed_pwd = hashlib.sha1(real_pwd.encode('utf-8')).hexdigest().upper()
first_5_hashed_pwd = hashed_pwd[0:5]

# 2. send to api and retrieve same prefix data set
pwd_dict = {}
try:
    ni = NetworkInterface()
    res = ni.get('https://api.pwnedpasswords.com/range/', first_5_hashed_pwd)
except:
    # display only : by network module
    exit()
else:
    pwd_dict = {item.split(':')[0]: item.split(':')[1]
                for item in res.text.split('\r\n')}
    # print(pwd_dict)

# show the result to user
if pwd_dict.get(hashed_pwd[5:]) is not None:
    print(
        f'the passowrd has been pwned for {pwd_dict.get(hashed_pwd[5:])} times')
else:
    print('this password is safe!')
