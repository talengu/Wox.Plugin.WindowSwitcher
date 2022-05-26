Wox.Plugin.WindowSwitcher
============================

![demo](https://user-images.githubusercontent.com/10290923/170521354-cfd5387f-4591-4fd8-87e9-25b40057433a.gif)

## Wox.Plugin.WindowSwitcher

`Wox` is a windows launcher, just like the Alfred in the mac. You can use to search local programs, files. It can also search web content by using plugins, such as how is the weather today, what's the score of xxx movie and so on.

Wox is open sourced at: http://www.github.com/qianlifeng/wox

`WindowSwitcher` is created as a windows switch for Wox and it can search the opened windows.

WindowSwitcher is writed in python and open sourced at: https://github.com/talengu/Wox.Plugin.WindowSwitcher


`Realse` [v1.0](https://github.com/talengu/Wox.Plugin.WindowSwitcher/releases)


It also can support both `zh` and `en` and so on.

Done List:
- test ok  


## Install

`wpm install Window Switcher` 

## QAs:

### 1. you may find some windows not show

  you can add  app name in [window_searcher.py](https://github.com/talengu/Wox.Plugin.WindowSwitcher/blob/c6397c503cff234c489cc820dab29e35d9809b58/window_searcher.py#L23)

  such like: 
```
_l = ["VirtualBox", "Chrome", "Code", "obsidian","YOUR APP NAME"] # not case sensitive
```

  then add some icos to `images/...ico`, img name should be low case of "your app name"

  if bug, try one try please!
 


## Refs
For the respect of the great peoples and the internet.

Dev Wox.Plugin ref: http://doc.wox.one/zh/plugin/python_plugin.html  

Dev pinyin support ref: http://www.jb51.net/article/65496.htm

Python Dev need win32gui win32con.

Thank you !!! Enjoy

MIT LICENSE HERE
