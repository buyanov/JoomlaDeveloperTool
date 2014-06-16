# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import datetime
import shutil
import fnmatch
import xml.etree.ElementTree as xmlParser
import os
import sys
from jtools import utils

def check_do_rewrite(t_path):
    if os.path.exists(t_path):
        do_rewrite = input('File exist. Rewrite? (Y/n) ')
        if(do_rewrite != 'Y'):
            return 0
    return 1

def getInstallXmlFromRoot():
    files = os.listdir(os.curdir)
    xmls = filter(lambda x: fnmatch.fnmatch(x,'com_*.xml'), files) 
    if sys.version_info.major < 3:
        try:
            xml = xmls[0]
        except Exception:
            print('Must go to root component')
            sys.exit()    
    else:
        try:    
            xml = next(xmls)
        except Exception:
            print('Must go to root component')
            sys.exit()
    tree = xmlParser.parse(xml)
    root = tree.getroot()
    if root.get('type') == 'component':
        return os.path.abspath(xml)
    return 0

def create_component(name, author, description, ToolConf):
    vars_dict = dict(creation_date=datetime.date.today(), \
                    component_name=name.lower(), \
                    component_name_cap=name.capitalize(), \
                    component_name_upper=name.upper(), \
                    author_name=author.name, \
                    author_email=author.email, \
                    author_url=author.url, \
                    author_license=author.license, \
                    author_copyright=author.copyright, \
                    component_desc=description)

    src_dir = os.path.join(ToolConf['templates'],'component')
    dst_dir = os.path.abspath(os.path.join(os.curdir,'com_'+name))
    
    try:
        shutil.copytree(src_dir, dst_dir)
    except Exception as e:
        print(e)
    os.chdir(dst_dir)
    utils.remake_dir(os.curdir, vars_dict)

def create_table(name, author, ToolConf):
    xml = getInstallXmlFromRoot()
    tree = xmlParser.parse(xml)
    root = tree.getroot()
    comp_name = root.find('name').text
    comp_ver = root.find('version').text
    admin_dir = root.find('administration/files').get('folder')
    vars_dict = dict(name=name.lower(), \
                    name_cap=name.capitalize(), \
                    component_name=comp_name.lower(), \
                    component_name_cap=comp_name.capitalize(), \
                    component_name_upper=comp_name.upper(), \
                    version=comp_ver, \
                    author_name=author.name, \
                    author_email=author.email, \
                    author_url=author.url, \
                    author_license=author.license, \
                    author_copyright=author.copyright)
    
    src_dir = os.path.abspath(os.path.join(ToolConf['mvc'],'table'))
    dst_dir = os.path.abspath(os.path.join(os.curdir,admin_dir,'tables'))

    for t_file in os.listdir(src_dir):
        file_path = os.path.abspath(os.path.join(src_dir,t_file))
        do_rewrite = check_do_rewrite(os.path.join(dst_dir, utils.remake_string(t_file, vars_dict)))
        if not do_rewrite:
            sys.exit()
        try:
            shutil.copy(file_path, dst_dir)
        except Exception as e:
            print(e)
        utils.remake_dir(dst_dir, vars_dict)
    
def create_model(name, author, jclass, dst, ToolConf):
    jclass_list = ['JModelList', 'JModelAdmin', 'JModelForm']
    xml = getInstallXmlFromRoot()
    tree = xmlParser.parse(xml)
    root = tree.getroot()
    comp_name = root.find('name').text
    comp_ver = root.find('version').text
    if dst:
        dst_folder = root.find('files').get('folder')
    else:
        dst_folder = root.find('administration/files').get('folder')

    vars_dict = dict(name=name.lower(), \
                    name_cap=name.capitalize(), \
                    component_name=comp_name.lower(), \
                    component_name_cap=comp_name.capitalize(), \
                    component_name_upper=comp_name.upper(), \
                    version=comp_ver, \
                    author_name=author.name, \
                    author_email=author.email, \
                    author_url=author.url, \
                    author_license=author.license, \
                    author_copyright=author.copyright)
    
    src_dir = os.path.abspath(os.path.join(ToolConf['mvc'],'model', jclass_list[jclass]))
    dst_dir = os.path.abspath(os.path.join(os.curdir,dst_folder,'models'))

    for t_file in os.listdir(src_dir):
        file_path = os.path.abspath(os.path.join(src_dir,t_file))
        do_rewrite = check_do_rewrite(os.path.join(dst_dir, utils.remake_string(t_file, vars_dict)))
        if not do_rewrite:
            sys.exit()
        try:
            shutil.copy(file_path, dst_dir)
        except Exception as e:
            print(e)
        utils.remake_dir(dst_dir, vars_dict)

def create_view(name, author, dst, ToolConf):
    xml = getInstallXmlFromRoot()
    tree = xmlParser.parse(xml)
    root = tree.getroot()
    comp_name = root.find('name').text
    comp_ver = root.find('version').text
    if dst:
        dst_folder = root.find('files').get('folder')
    else:
        dst_folder = root.find('administration/files').get('folder')

    vars_dict = dict(name=name.lower(), \
                    name_cap=name.capitalize(), \
                    component_name=comp_name.lower(), \
                    component_name_cap=comp_name.capitalize(), \
                    component_name_upper=comp_name.upper(), \
                    version=comp_ver, \
                    author_name=author.name, \
                    author_email=author.email, \
                    author_url=author.url, \
                    author_license=author.license, \
                    author_copyright=author.copyright)
    
    src_dir = os.path.abspath(os.path.join(ToolConf['mvc'],'view'))
    dst_dir = os.path.abspath(os.path.join(os.curdir,dst_folder,'views'))
    
    for t_file in os.listdir(src_dir):
        do_rewrite = check_do_rewrite(os.path.join(dst_dir, utils.remake_string(t_file, vars_dict)))
        if not do_rewrite:
            sys.exit()
        src_file_path = os.path.abspath(os.path.join(src_dir,t_file))
        dst_file_path = os.path.abspath(os.path.join(dst_dir,t_file))
        
        dst_remaked_name = utils.remake_string(dst_file_path, vars_dict)
        if(os.path.exists(dst_remaked_name)):
            shutil.rmtree(dst_remaked_name)
        
        try:
            shutil.copytree(src_file_path, dst_file_path)
        except Exception as e:
            print(e)
        utils.remake_dir(dst_file_path, vars_dict)
    
def create_controller(name, author, jclass, dst, ToolConf):
    jclass_list = ['JControllerLegacy', 'JControllerAdmin', 'JControllerForm']
    xml = getInstallXmlFromRoot()
    tree = xmlParser.parse(xml)
    root = tree.getroot()
    comp_name = root.find('name').text
    comp_ver = root.find('version').text
    if dst:
        dst_folder = root.find('files').get('folder')
    else:
        dst_folder = root.find('administration/files').get('folder')

    vars_dict = dict(name=name.lower(), \
                    name_cap=name.capitalize(), \
                    component_name=comp_name.lower(), \
                    component_name_cap=comp_name.capitalize(), \
                    component_name_upper=comp_name.upper(), \
                    version=comp_ver, \
                    author_name=author.name, \
                    author_email=author.email, \
                    author_url=author.url, \
                    author_license=author.license, \
                    author_copyright=author.copyright)
    
    src_dir = os.path.abspath(os.path.join(ToolConf['mvc'],'controller', jclass_list[jclass]))
    dst_dir = os.path.abspath(os.path.join(os.curdir,dst_folder,'controllers'))

    for t_file in os.listdir(src_dir):
        file_path = os.path.abspath(os.path.join(src_dir,t_file))
        do_rewrite = check_do_rewrite(os.path.join(dst_dir, utils.remake_string(t_file, vars_dict)))
        if not do_rewrite:
            sys.exit()
        try:
            shutil.copy(file_path, dst_dir)
        except Exception as e:
            print(e)
        utils.remake_dir(dst_dir, vars_dict)

def print_component():
    startpath = os.curdir
    print("Component structure:")
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = '.' * 3 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = '.' * 3 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))
