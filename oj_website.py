"""
The project is used to create a .html file as the user's OJ annual report.

This module is the OJ_Website class, which is used to get the user's information from the OJ website, and save the information to a .json file.

requirements:
+ requests
+ json

file related:
+ [read] config.json:               read the user's serviceid and auth_token
+ [write if main] data.json:        save the user's information

"""

import json
import requests


class OJ_Website:
    """
    The class is used to get the user's information from the OJ website.
    """
    def __init__(self):
        """
        Initialize the class.
        :param serviceid: The user's serviceid.
        :param auth_token: The user's auth_token.
        """
        self.serviceid = None
        self.auth_token = None
        try:
            with open('config.json', 'r') as f:
                config = json.load(f)
                self.serviceid = config['serviceid']
                self.auth_token = config['Auth-Token']
        except FileNotFoundError:
            self.serviceid = input("Please input your serviceid: ")
            self.auth_token = input("Please input your Auth-Token: ")
            with open('config.json', 'w') as f:
                json.dump({'serviceid': self.serviceid, 'Auth-Token': self.auth_token}, f, ensure_ascii=False, indent=4)
        self.response = None
        self.url = 'https://oj.ee.tsinghua.edu.cn/api/my/submits/?page=1&page_size=800'
        self.headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Authorization': f'TOKEN {self.auth_token}',
            'Priority': 'u=1, i',
            'Referer': 'https://oj.ee.tsinghua.edu.cn/',
            'Sec-Ch-Ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edg/131.0.0.0',
        }
        self.cookies = {
            'serviceid': self.serviceid,
            'Auth-Token': self.auth_token,
        }

    def get_data(self):
        """
        Get the user's information from the OJ website.

        :return:    The user's information in json format.

        """
        print(f"Requesting {self.url} ...")
        self.response = requests.get(self.url, headers=self.headers, cookies=self.cookies)
        print(f"Response Status Code: {self.response.status_code}")
        return self.response.json()
    

if __name__ == '__main__':
    # create an OJ_Website object
    oj_website = OJ_Website()
    print(f"Serviceid: {oj_website.serviceid}")
    print(f"Auth-Token: {oj_website.auth_token}")

    # get the user's information from the OJ website
    data = oj_website.get_data()

    # save the user's information to "data.json" file
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
