from NetworkInterface import NetworkInterface
import hashlib
import sys
import getpass


def get_input():
    return getpass.getpass('your desired password, [q] to quit > ')


def main():
    try:
        # get password from user
        real_pwd = get_input()

        while real_pwd.lower() != 'q':
            # check on user input
            if len(real_pwd) == 0:
                print("your password is empty!")
                real_pwd = get_input()
                continue

            # check if its pwned
            # 1. get hashed real-pwd and the first 5 digit
            hashed_pwd = hashlib.sha1(
                real_pwd.encode('utf-8')).hexdigest().upper()
            first_5_hashed_pwd = hashed_pwd[0:5]

            # 2. send to api and retrieve same prefix data set
            pwd_dict = {}
            try:
                ni = NetworkInterface()
                res = ni.get('https://api.pwnedpasswords.com/range/',
                             first_5_hashed_pwd)
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

            real_pwd = get_input()
    except KeyboardInterrupt:
        print('\r\n user exit')
        return


if __name__ == '__main__':
    main()
