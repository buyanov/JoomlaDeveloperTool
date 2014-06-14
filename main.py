#!/usr/bin/python3
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import sys
if sys.version_info.major < 3:
    import ConfigParser as configparser
    # import the old module with the name of the new one
    import optparse as argparse
else:
    import configparser
    import argparse
from os import path
import jauthor.author as jauthor
import jtools.jcomponent as jcomponent

if sys.version_info.major < 3:
    # make sure the class name is available like in python 3.3
    argparse.ArgumentParser = argparse.OptionParser
    # same for the add methods:
    argparse.ArgumentParser.add_argument = argparse.ArgumentParser.add_option
    # save a reference to the old parse method
    argparse.ArgumentParser.__parse_args__ = argparse.ArgumentParser.parse_args
    # override the parse method:
    def parseargs(self):
        return self.__parse_args__()[0]
    argparse.ArgumentParser.parse_args = parseargs

def get_tool_conf():
    config_parser = configparser.RawConfigParser()
    tool_path = path.split(path.realpath( __file__ ))[0]
    try:
        config_parser.read(path.join(tool_path, 'toolconf.conf'))
    except Exception:
        print("Tool's config not found")

    tool_conf = {\
                'userconfig': path.expanduser(config_parser.get('main', 'userconfig')), \
                'templates': path.join(tool_path, path.normpath(config_parser.get('main', 'templates'))), \
                'mvc': path.join(tool_path, path.normpath(config_parser.get('main', 'mvc')))
                }
    return tool_conf

def main():
    tool_conf = get_tool_conf()

    parser = argparse.ArgumentParser(description="Joomla Developer Tool", epilog="Created by Rogachev Sergey", usage="%(prog)s [--init] | [--print] | [--create [options]]")
    
    parser.add_argument("--init", "-i", \
                        const=True, \
                        action="store_const", \
                        help="Create user config file")
    
    parser.add_argument("--create", "-c", \
                        const=True, \
                        action="store_const", \
                        help="Create new element or structure.")

    parser.add_argument("--struct", "-S", \
                        const=True, \
                        action="store_const", \
                        help="Create structure component")

    parser.add_argument("--model", "-M", \
                        const=True, \
                        action="store_const", \
                        help="Create model")

    parser.add_argument("--view", "-V", \
                        const=True, \
                        action="store_const", \
                        help="Create view")

    parser.add_argument("--controller", "-C", \
                        const=True, \
                        action="store_const", \
                        help="Create model")

    parser.add_argument("--table", "-T", \
                        const=True, \
                        action="store_const", \
                        help="Create table")
    
    parser.add_argument("--name", "-n", \
                        type=str, \
                        default="name", \
                        action="store", \
                        help="Name of new element or component")

    parser.add_argument("--description", "-d", \
                        type=str, \
                        default='Component description', \
                        action="store", \
                        help="Takes component description")

    parser.add_argument("-L", \
                        const=0, \
                        action="store_const", \
                        help="Class JControllerLegacy for controller or JModelList for model")

    parser.add_argument("-A", \
                        const=1, \
                        action="store_const", \
                        help="Class JControllerAdmin for controller or JModelAdmin for model")

    parser.add_argument("-F", \
                        const=2, \
                        action="store_const", \
                        help="Class JControllerForm for controller or JModelForm for model")

    parser.add_argument("--backend", "-b", \
                        const=0, \
                        action="store_const", \
                        help="Add MVC element to back-end (admin folder)")

    parser.add_argument("--frontend", "-f", \
                        const=1, \
                        action="store_const", \
                        help="Add MVC element to front-end (site folder)")

    parser.add_argument("--print", "-p", \
                        const=True, \
                        action="store_const", \
                        help="Infomation about component.")

    args = parser.parse_args()
    args_vars = vars(args)

    if args_vars['init']:
        jauthor.make_conf(tool_conf['userconfig'])
        return 1

    elif args_vars['print']:
        jcomponent.print_component()
        return 1

    elif args_vars['create']:
        author = jauthor.make_author_from_conf(tool_conf['userconfig'])
        if(not author):
            print("Configuration file does not exist. Run tool with '-i' option")
            return 0

        if args_vars['struct']:
            jcomponent.create_component(args_vars['name'], author, args_vars['description'], tool_conf)
            return 1
        
        if args_vars['model'] or args_vars['view'] or args_vars['controller']:
            dst = filter(lambda x: x is not None, [args_vars['backend'], args_vars['frontend']])
            if sys.version_info.major < 3:
                try:
                    dst = dst[0]
                except Exception:
                    print("Select destination: -b for back-end, -f for front-end")
                    return 0
            else:
                try:
                    dst = next(dst)
                except Exception:
                    print("Select destination: -b for back-end, -f for front-end")
                    return 0

        if args_vars['model'] or args_vars['controller']:
            jclass = filter(lambda x: x is not None, [args_vars['L'], args_vars['A'], args_vars['F']])
            if sys.version_info.major < 3:
                try:
                    jclass = jclass[0]
                except Exception:
                    print("Select class model: -L for JModelList/JControllerLegacy, -F for JModelForm/JControllerForm or -A for JModelAdmin/JControllerAdmin")
                    return 0
            else:
                try:
                    jclass = next(jclass)
                except Exception:
                    print("Select class model: -L for JModelList/JControllerLegacy, -F for JModelForm/JControllerForm or -A for JModelAdmin/JControllerAdmin")
                    return 0

        if args_vars['model']:
            jcomponent.create_model(args_vars['name'], author, jclass, dst, tool_conf)
        
        elif args_vars['view']:
            jcomponent.create_view(args_vars['name'], author, dst, tool_conf)

        elif args_vars['controller']:
            jcomponent.create_controller(args_vars['name'], author, jclass, dst, tool_conf)
                
        elif args_vars['table']:
            jcomponent.create_table(args_vars['name'], author, tool_conf)

    else:
        parser.print_help()

if __name__ == '__main__':
    main()