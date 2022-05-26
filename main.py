# encoding=utf8

"""
Wox支持使用Python进行插件的开发。Wox自带了一个打包的Python及其标准库，所以使用Python 插件的用户不必自己再安装Python环境。
同时，Wox还打包了requests和beautifulsoup4两个库， 方便用户进行网络访问与解析。
ref: http://doc.getwox.com/zh/plugin/python_plugin.html
"""

import webbrowser
from wox import Wox, WoxAPI
from  window_searcher import window_searcher
import win32gui
import win32con


class BSearcher(Wox):

    # 必须有一个query方法，用户执行查询的时候会自动调用query方法
    def query(self, query):
        mSearcher = window_searcher()
        res = mSearcher.do_search(query)
        results = []
        if query != '':
            for item in res:
                hwnd = item[0]
                cls= item[1]
                title = item[2]
                results.append({
                    "Title": title,
                   # "SubTitle": "{}".format(url),
                    "IcoPath": "images/%s.ico"%cls,
                    "JsonRPCAction": {
                        # 这里除了自已定义的方法，还可以调用Wox的API。调用格式如下：Wox.xxxx方法名
                        # 方法名字可以从这里查阅https://github.com/qianlifeng/Wox/blob/master/Wox.Plugin/IPublicAPI.cs 直接同名方法即可
                        "method": "openWindows",
                        # 参数必须以数组的形式传过去
                        "parameters": [hwnd],
                        # 是否隐藏窗口
                        "dontHideAfterAction": True}
                })
            if results == []:
                results.append({
                    "Title": "None",
                    "SubTitle": "Query: {}".format(query),
                    "IcoPath": "images/default.ico"
                })
        return results

    def openWindows(self, hwnd):
        # open the browser
        # SW_HIDE 最小化
        win32gui.SetForegroundWindow(hwnd)
        win32gui.SendMessage(hwnd, win32con.WM_SYSCOMMAND, win32con.SC_RESTORE, 0)
        #win32gui.ShowWindow(hwnd, win32con.SW_HIDE)
        # todo:doesn't work when move this line up
        #WoxAPI.change_query(hwnd)


if __name__ == "__main__":
    BSearcher()
# https://baike.baidu.com/item/ShowWindow/5279029?fr=aladdin