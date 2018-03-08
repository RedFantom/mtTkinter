"""
Thread-safe version of Tkinter

Copyright (c) 2009, Allen B. Taylor
Copyright (c) 2017, baldk
Copyright (c) 2018, RedFantom
"""
import sys
import threading
from unittest import TestCase
if sys.version_info[0] == 2:
    import Tkinter as tk
    from Queue import Queue
else:
    import tkinter as tk
    from queue import Queue


class TestMTTkinter(TestCase):
    """
    Test the in-memory modification of the Tkinter class and mtTkinter
    functionality.
    """
    def test_mttkinter_import(self):
        """In-memory modification test"""
        orig_init = tk.Tk.__init__
        orig_destroy = tk.Tk.destroy
        from mttkinter import mtTkinter
        self.assertNotEqual(orig_init, id(tk.Tk.__init__))
        self.assertNotEqual(orig_destroy, id(tk.Tk.destroy))
        self.assertTrue(hasattr(tk.Tk(), "_tk"))

    def test_threading_normal(self):
        """
        Test running commands on a window in another thread. This is
        *not* a fool-proof test. Threading issues in Tkinter are
        complicated, and usually not easily reproducible.
        """
        from mttkinter import mtTkinter
        root = tk.Tk()
        queue = Queue(1)
        root.after(1000, lambda: DummyThread(root, queue, 1).start())
        while queue.empty():
            root.update()
        # If exit with 0, then clearly the test succeeded

    def test_threading_exception(self):
        """
        Test running a command that will raise an error in a Thread to
        test exception handling.
        """
        from mttkinter import mtTkinter
        root = tk.Tk()
        queue = Queue(1)
        root.after(1000, lambda: DummyThread(root, queue, 2).start())
        while queue.empty():
            root.update()
        # If exit with 0, then clearly the test succeeded


class DummyThread(threading.Thread):
    def __init__(self, root, queue, mode):
        threading.Thread.__init__(self)
        self.root = root
        self.queue = queue
        self.mode = mode

    def run(self):
        if self.mode == 1:  # Normal
            tk.Button(self.root, background="blue").pack()
            self.queue.put(True)
        elif self.mode == 2:  # Error:
            try:
                tk.Button(self.root, background="nonexistent").pack()
            except tk.TclError:
                self.queue.put(True)
                return True
            self.queue.put(True)
            raise ValueError("Exception not correctly raised.")
