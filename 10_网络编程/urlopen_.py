#!/usr/bin/env python
# -*- coding: utf-8 -*-
# urlopen(url,data):
# data：想服务器发送的数据
import urllib.parse
from urllib.request import *


params = urllib.parse.urlencode({"name": "xyktl", "password": "c1635976271"})
url = "http://www.crazyit.org/index.php"
with urlopen(url=url, data=params.encode("utf-8")) as f:
    print(f.read().decode("utf-8"))
