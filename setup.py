from setuptools import setup

setup(
    name='mttkinter',
    packages=['mttkinter'],
    version='0.5.0',
    description='A thread-safe wrapper around Tkinter for Python 2.x',
    author='mtTkinter authors',
    author_email='redfantom@outlook.com',
    url='https://github.com/RedFantom/mtTkinter',
    download_url='https://github.com/RedFantom/mtTkinter/releases',
    license="LGPLv3",
    keywords=['tkinter', 'threading'],
    classifiers=["Programming Language :: Python :: 2 :: Only",
                 "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)"],
    include_package_data=True
)
