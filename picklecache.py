#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 module"""

import os
import pickle


class PickleCache(object):
    """Class object docstring.

    """

    def __init__(self, filepath='datastore.pkl', autosync=False):
        """Constructor.

        Args:
        filepath(object): Accepts filename as argument.
        autosync(bool): Accepts boolean as argument.

        """
        self.__file_path = filepath
        self.__data = {}
        self.autosync = autosync
        self.load()

    def __setitem__(self, key, value):
        """Docstring.
        """
        self.__data[key] = value

    def __len__(self):
        """Docstring.
        """
        return len(self.__data)
        
    def __getitem__(self, key):
        """Docstring.
        """
        try:
            self.__data[key]

        except (TypeError, KeyError):
            raise Exception

    def __delitem__(self, key):
        """Docstring.
        """
        del self.__data[key]

    def load(self):
        """Docstring.
        """
        if os.path.exists(self.__file_path) and \
        os.path.getsize(self.__file_path) > 0:
            myfile = open(self.__file_path, 'r')
            __self.data = pickle.load(myfile)
            myfile.close()

    def flush(self):
        """Docstring.
        """
        myfile = open(self.__file_path, 'w')
        pickle.dump(self.__data, myfile)
        myfile.close()
