#-*- coding: utf-8 -*-

import os

'''
    settings
'''

settings = {
    "static_path": os.path.join(os.path.abspath(__file__), "templates"),
    "cookie_secret": "YzlhMGI2NTMxNTVhMjc4ZGFkMzE3MjJiZGY1ZGE2YjM4YzJjODU0Zg==",
    "xsrf_cookies": True,
}
