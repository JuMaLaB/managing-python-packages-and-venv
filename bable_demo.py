""" 
# https://pypi.org/

PS C:\ws_vedana\[python]\managing-python-packages-and-venv> python
Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> sys.path
['', 'C:\\Python310\\python310.zip', 'C:\\Python310\\DLLs', 'C:\\Python310\\lib', 'C:\\Python310', 'C:\\Python310\\lib\\site-packages']

# https://pip.pypa.io/en/stable/user_guide/
PS C:\ws_vedana\[python]\managing-python-packages-and-venv>py -m pip install SomePackage            # latest version
PS C:\ws_vedana\[python]\managing-python-packages-and-venv>py -m pip install SomePackage==1.0.4     # specific version
PS C:\ws_vedana\[python]\managing-python-packages-and-venv>py -m pip install 'SomePackage>=1.0.4'   # minimum version

PS C:\ws_vedana\[python]\managing-python-packages-and-venv>py -m pip install -U SomePackage

# to install to my specific user and not to my system
PS C:\ws_vedana\[python]\managing-python-packages-and-venv>py -m pip install --user SomePackage
PS C:\ws_vedana\[python]\managing-python-packages-and-venv>py -m pip help

PS C:\ws_vedana\[python]\managing-python-packages-and-venv>py -m pip help list

PS C:\ws_vedana\[python]\managing-python-packages-and-venv> pip list
PS C:\ws_vedana\[python]\managing-python-packages-and-venv> pip show pip

# in a real command prompt
C:\ws_vedana\[python]\managing-python-packages-and-venv
λ ..\virtualenvs\mppav\Scripts\activate.bat

C:\ws_vedana\[python]\managing-python-packages-and-venv
(mppav) λ pip show babel
Name: babel
Version: 2.16.0
Summary: Internationalization utilities
Home-page: https://babel.pocoo.org/
Author: Armin Ronacher
Author-email: armin.ronacher@active-4.com
License: BSD-3-Clause
Location: c:\ws_vedana\[python]\virtualenvs\mppav\lib\site-packages
Requires:
Required-by:

C:\ws_vedana\[python]\managing-python-packages-and-venv
(mppav) λ py -m pip freeze > requirements.txt

C:\ws_vedana\[python]\managing-python-packages-and-venv
(mppav) λ py -m pip install -r requirements.txt
"""

from babel.numbers import format_number, format_decimal

number = 12345678
print("In the Netherlands we write",
    format_decimal(number, locale="en_US"),
    "as",
    format_decimal(number, locale="nl_NL"),
)