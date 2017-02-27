# mtTkinter [![PyPI version](https://badge.fury.io/py/mttkinter.svg)](https://badge.fury.io/py/mttkinter)
#### A wrapper around Tkinter for multi-threading by Allen B. Taylor

This is the mtTkinter module written by Allen B. Taylor, originally published [here](http://tkinter.unpythonic.net/wiki/mtTkinter). 
This module was originally created to fix problems in a program that was not thread-safe, but I have found it to be useful in my
own programs as well. This GitHub repository is available for those who want to fork the code, but mostly I just created it to
get the module on PyPI. Publishing the module on PyPI was [suggested](http://grokbase.com/t/python/python-list/08aq5e9gp6/proposal-for-thread-safe-tkinter) quite a while ago.

### Usability
This code is basically only useful when you're running Python 2.7 and you would like to call functions of Tkinter widgets from
a thread other than the `MainThread`. This issue is not existent in Python 3.x, so if you're using that, you can safely use
threads in a Tkinter application with the `threading` module.

### Installation
You can install mtTkinter by copying it directly into your project folder, install it Python-installation wide by copying the
`mtTkinter.py` file into `%PYTHONDIR%/Libs/lib-tk/mtTkinter.py` or you could use `pip install mttkinter`, a method for which this
repository was specifically created.

### License
Allen B. Taylor licensed this code under the GNU LGPL license from version 0.4 on.

### Development
Since I have not found any bugs or problems with the current code, there will be no further development of the module. If you want,
you can fork the repository and suggest changes through pull requests. You will be credited for your work.
