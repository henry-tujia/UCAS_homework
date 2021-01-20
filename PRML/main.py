# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from urllib.parse import urlparse

import requests


def login_wifi(stuid, password):
    try:
        query_string = urlparse(requests.get("http://210.77.16.21").url).query
        payload = {
            "userId": stuid,
            "password": password,
            "service": "",
            "queryString": query_string,
            "operatorPwd": '',
            "operatorUserId": '',
            "validcode": '',
        }
        res = requests.post("http://210.77.16.21/eportal/InterFace.do?method=login", data=payload)
        res.encoding = 'u8'
    except (requests.exceptions.ConnectionError,
            requests.exceptions.ConnectTimeout,
            requests.exceptions.ReadTimeout):
        return None
    else:
        return {
            'result': res.json().get("result"),
            'msg': res.json().get("message"),
            'query_string': query_string
        }


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(login_wifi('2020E8013282037', '10741X'))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
