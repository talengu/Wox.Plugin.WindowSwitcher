# -*- coding: utf-8 -*-
import os
from pinyin.pinyin import PinYin

import win32gui
import win32con


# for test
def check1(clsname, title):
    if clsname == None or clsname == "":
        return False
    if title == None or title == "":
        return False
    _l = ["MSCTFIME UI", "IME"]
    if clsname in _l:
        return False
    if clsname[:2] == "##":
        return False
    return True


_l = ["VirtualBox", "Chrome", "Code", "obsidian"]
_l = [x.lower() for x in _l]


def check(clsname, title):
    if clsname == None or clsname == "":
        return False, "default"
    if title == None or title == "":
        return False, "default"
    if clsname == "CASCADIA_HOSTING_WINDOW_CLASS":  # windows termianl
        return True, "windows_termianl"
    if clsname == "OrpheusBrowserHost":  # 网易云
        return True, "netease"
    for item in _l:
        if item in title.lower():
            return True, item

    return False, "default"


class window_searcher(object):
    def __init__(self):
        self.lis = []
        self.make_list()  # 将windows数据准备好
        self.pinyin_item()  # 将pinyin准备好

    def make_list(self):
        hWndList = []
        win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hWndList)
        c = 0
        for hwnd in hWndList:
            clsname = win32gui.GetClassName(hwnd)
            title = win32gui.GetWindowText(hwnd)

            ischeck, cls = check(clsname, title)
            if ischeck:
                c = c+1
                # print("%03d:"%c+clsname+'@'+title)
                weight = 0
                newItem = [hwnd, cls, title, weight, '']
                self.lis.append(newItem)

    def pinyin_item(self):
        # pinyin dict
        self.py = PinYin('pinyin/word.data')
        self.py.load_word()
        for i, item in enumerate(self.lis):
            # 拼音化
            han_item = ''
            all_pin = first_pin = ''

            [_, cls, title, _, _] = item

            for x in title.split(' '):
                han_item += x
            item_pinyin = self.py.hanzi2pinyin_split(
                string=han_item, split=" ")
            for x in item_pinyin.split(' '):
                if x != '':
                    all_pin += x
                    first_pin += x[0]
            res_pin = item_pinyin + ' ' + all_pin + ' ' + first_pin
            self.lis[i][4] = res_pin + ' ' + cls

    def do_search(self, key):
        result_lis = []
        for item in self.lis:
            # 将单词变为low 方便索引
            [_, _, title, _, res_pin] = item
            if title.lower().find(key) != -1 or title.lower().find(key.lower()) != -1\
                    or res_pin.find(key) != -1:
                result_lis.append(item)
        # weight
        search_result = sorted(result_lis, key=lambda x: x[3], reverse=True)
        return [x[:3] for x in search_result]


# start = time.time()
# ....code
# end = time.time()
# print('Runs %0.2f seconds.' % (end - start))


if __name__ == "__main__":
    n = window_searcher()

    key = 'code'
    res = n.do_search(key)
    print(res)
    print(len(res))
