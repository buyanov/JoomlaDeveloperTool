# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import sys
import os
from string import Template
import fnmatch

if sys.version_info.major < 3:
    reload(sys)
    sys.setdefaultencoding('utf-8')

class ExtTemplate(Template):
    delimiter = '%'
    idpattern = r'[a-z][_a-z0-9]*(\.[a-z][_a-z0-9]*)*'

def remake_string(str, vars_dict):
    temp = ExtTemplate(str)
    return temp.safe_substitute(vars_dict)

def remake_dir(dir_path, vars_dict):
    tree = os.walk(os.path.abspath(dir_path))

    for root, dirs, files in tree:
        for f in files:
            path_file = os.path.join(root, f)
            if os.path.getsize(path_file)>0:
                cur_file = open(path_file, 'r+')
                file_content = cur_file.read()
                new_file_content = remake_string(file_content, vars_dict)
                cur_file.seek(0)
                cur_file.write(new_file_content)
                cur_file.truncate()
                cur_file.close()
            new_filename = remake_string(f, vars_dict)
            os.rename(os.path.join(root, f), os.path.join(root, new_filename))
        if fnmatch.fnmatch(root,'*%{*}*'):
            new_dirname = remake_string(root, vars_dict)
            os.rename(root, new_dirname)
