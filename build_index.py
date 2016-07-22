#!/usr/bin/env python2
# -*- coding: utf-8

import os
import urllib


def build_index():
    root_path = "drop"
    for file_name in sorted(os.listdir(root_path)):
        print('<a href=/drop/{0}>{1}</a><br />'.format(urllib.quote(file_name), file_name))


def main():
    build_index()


if __name__ == "__main__":
    main()