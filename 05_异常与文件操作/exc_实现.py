#!/usr/bin/env python
# -*- coding: utf-8 -*-
import traceback
import sys
try:
    print(30 / 0)
except:
	#多种方式
    # traceback.print_exc()
    # print(sys.exc_info())
    # traceback.print_tb(sys.exc_info()[2])
    traceback.print_exc(file=open("log1.txt","a"))


