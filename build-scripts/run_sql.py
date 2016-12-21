#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: cody
# @Date:   2016-12-21 11:44:44
# @Last Modified 2016-12-21
# @Last Modified time: 2016-12-21 12:08:12

""" sublime build system for sqlite dbs """

from os import popen
from sys import argv
from veripy import veripy


def print_example(message="invalid usage"):
    """ prints example and exits """
    veripy.str(message)
    print "error: {}".format(message)
    print "recieved: python {}".format(" ".join(argv))
    exit("usage example: python run_sql.py tmp.db tmp.sql")

assert len(argv) is 3, print_example('not enough args')


def run_script(db_path, sql_file):
    """ runs a sql script on a sqlite db """
    veripy.str(db_path, sql_file)
    veripy.file_path(db_path, sql_file)
    assert sql_file.endswith(".sql"), print_example()
    command = 'sqlite3 "{}" < "{}"'.format(
        db_path,
        sql_file
    )
    print "running: {}".format(command)
    return popen(command).read()


if __name__ == '__main__':
    print run_script(argv[-2], argv[-1])
