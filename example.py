"""
Thread-safe version of Tkinter

Copyright (c) 2009, Allen B. Taylor
Copyright (c) 2017, baldk
Copyright (c) 2018, RedFantom
"""
import sys
if sys.version_info[0] == 2:
    from Tkinter import *
else:
    from tkinter import *
from mttkinter import mtTkinter


# Test thread entry point.
def _test_thread(root):
    text = "This is Tcl/Tk version %s" % TclVersion
    try:
        if root.globalgetvar('tcl_platform(threaded)'):
            text = text + "\nTcl is built with thread support"
        else:
            raise RuntimeError
    except:
        text = text + "\nTcl is NOT built with thread support"
    text = text + "\nmtTkinter works with or without Tcl thread support"
    label = Label(root, text=text)
    label.pack()
    button = Button(root, text="Click me!",
                    command=lambda root=root: root.button.configure(
                        text="[%s]" % root.button['text']))
    button.pack()
    root.button = button
    quit = Button(root, text="QUIT", command=root.destroy)
    quit.pack()
    # The following three commands are needed so the window pops
    # up on top on Windows...
    root.iconify()
    root.update()
    root.deiconify()
    # Simulate button presses...
    button.invoke()
    root.after(1000, _press_ok, root, button)


# Test button continuous press event.
def _press_ok(root, button):
    button.invoke()
    try:
        root.after(1000, _press_ok, root, button)
    except TclError:
        pass  # Likely we're exiting


# Test. Mostly borrowed from the Tkinter module, but the important bits moved
# into a separate thread.
if __name__ == '__main__':
    import threading

    root = Tk(mt_debug=1)
    thread = threading.Thread(target=_test_thread, args=(root,))
    thread.start()
    root.mainloop()
    thread.join()

