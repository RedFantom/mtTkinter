# mtTkinter 
[![Build status](https://ci.appveyor.com/api/projects/status/4r9796lwmrx2s2mx?svg=true)](https://ci.appveyor.com/project/RedFantom/mttkinter)
[![Build Status](https://travis-ci.org/RedFantom/mtTkinter.svg?branch=master)](https://travis-ci.org/RedFantom/mtTkinter)
[![codecov](https://codecov.io/gh/RedFantom/mtTkinter/branch/master/graph/badge.svg)](https://codecov.io/gh/RedFantom/mtTkinter)
[![PyPI version](https://badge.fury.io/py/mttkinter.svg)](https://badge.fury.io/py/mttkinter)
[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](http://www.gnu.org/licenses/lgpl-3.0)


#### A wrapper around Tkinter for multi-threading by Allen B. Taylor

This is the mtTkinter module written by Allen B. Taylor, originally published [here](http://tkinter.unpythonic.net/wiki/mtTkinter). 
This module was originally created to fix problems in a program that was not thread-safe, but I have found it to be useful in my
own programs as well. This GitHub repository is available for those who want to fork the code, but mostly I just created it to
get the module on PyPI. Publishing the module on PyPI was [suggested](http://grokbase.com/t/python/python-list/08aq5e9gp6/proposal-for-thread-safe-tkinter) quite a while ago.

### Installation
You can install mtTkinter by copying it directly into your project folder, install it Python-installation wide by copying the
`mtTkinter.py` file into `%PYTHONDIR%/Libs/lib-tk/mtTkinter.py` or you could use `pip install mttkinter`, a method for which this
repository was specifically created.

### License
Allen B. Taylor licensed this code under the GNU LGPL license from version 0.4 on.

### Development
Since I have not found any bugs or problems with the current code, there will be no further development of the module. If you want,
you can fork the repository and suggest changes through pull requests. You will be credited for your work.
