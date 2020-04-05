# -*- coding: utf-8 -*-
from __future__ import print_function
import ctypes
import sys
import os


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin():
    os.startfile("C:\\Users\\Hasse\\Desktop\\py project\\12_阿里云\\madir_day.py")
else:
    if sys.version_info[0] == 3:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        os.startfile("C:\\Users\\Hasse\\Desktop\\py project\\12_阿里云\\madir_day.py")
    else:  # in python2.x
        ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)
