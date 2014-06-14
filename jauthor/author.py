# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import sys
if sys.version_info.major < 3:
    import ConfigParser as configparser
else:
    import configparser
import os.path as path

if sys.version_info < (3,0):
    input = raw_input
else:
    input = input

class Author:
    def __init__(self, name, email, url, license, copyright):
        self.name = name
        self.email = email
        self.url = url
        self.license = license
        self.copyright = copyright

def make_conf(confpath):
    try:
        conffile = open(confpath, 'w')
    except Exception as e:
        print(e)

    var_name = input('Enter you name: ')
    var_email = input('Enter you email: ')
    var_url = input('Enter you url: ')
    var_license = input('Enter license: ')
    var_copyright = input('Enter copyright: ')

    config = configparser.RawConfigParser()
    config.add_section('Author')
    config.set('Author', 'name', var_name)
    config.set('Author', 'email', var_email)
    config.set('Author', 'url', var_url)
    config.set('Author', 'license', var_license)
    config.set('Author', 'copyright', var_copyright)

    config.write(conffile)
    conffile.close()

def make_author_from_conf(confpath):
    if path.exists(confpath):
        config = configparser.RawConfigParser()
        try:
            config.read(confpath)
        except Exception as e:
            print(e)
            return 0

        authorName = config.get('Author', 'name')
        authorEmail = config.get('Author', 'email')
        authorUrl = config.get('Author', 'url')
        authorLicense = config.get('Author', 'license')
        authorCopyright = config.get('Author', 'copyright')
        author = Author(authorName, authorEmail, authorUrl, authorLicense, authorCopyright)
        return author
    else:
        return 0