import time

import requests
from bs4 import BeautifulSoup


def return_time():
    a = time.localtime()
    return a.tm_year*10000+a.tm_mon*100+a.tm_mday


def from_txt():
    with open('a.txt', 'r') as f:
        id = f.readline().split('\n')[0]
        pw = f.readline()
    args = {'id': id, 'pw': pw}
    return args


print(from_txt())
