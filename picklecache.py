#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This program opens, reads, and writes to a file."""

import os
import pickle


class PickleCache(object):
    """Class object to manage file.

    """

    def __init__(self, filepath='datastore.pkl', autosync=False):
        """Constructor for PickleCache.

        Args:
            filepath(object): Accepts filename as argument.
            autosync(bool): Accepts boolean as argument.

        Example:
            >>> cacher = PickleCache()
            >>> print cacher._PickleCache__file_path
            'datastore.pkl'
            >>> print cacher._PickleCache__data
            {}

        """
        self.__file_path = filepath
        self.__data = {}
        self.autosync = autosync
        self.load()

    def __setitem__(self, key, value):
        """This function sets key-value pairs for storing.

        Args:
            key(string): A required argument.
            value(string): A required argument.

        Example:
            >>> pcache = PickleCache()
            >>> pcache['test'] = 'hello'
            >>> print pcache._PickleCache__data['test']
            'hello'
        """
        self.__data[key] = value

    def __len__(self):
        """This function returns the length of __data.

        Example:
            >>> len(pcache)
            1
        """
        return len(self.__data)

    def __getitem__(self, key):
        """This function gets values from __data.

        Args:
            key(str): A required input.

        Example:
            >>> pcache = PickleCache()
            >>> pcache['test'] = 'hello'
            >>> print pcache['test']
            'hello'
        """
        try:
            self.__data[key]

        except (TypeError, KeyError):
            raise Exception

    def __delitem__(self, key):
        """This function deletes values from __data.

        Args:
            key(str): A required argument.

        Example:
            >>> pcache = PickleCache()
            >>> pcache['test'] = 'hello'
            >>> print len(pcache)
            1
            >>> del pcache['test']
            >>> print len(pcache)
            0
        """
        del self.__data[key]

    def load(self):
        """This function loads a file provided it exists and > 0 byte.
        """
        if os.path.exists(self.__file_path) and \
        os.path.getsize(self.__file_path) > 0:
            myfile = open(self.__file_path, 'r')
            self.__data = pickle.load(myfile)
            myfile.close()

    def flush(self):
        """This function writes to and closes the file.
        """
        myfile = open(self.__file_path, 'w')
        pickle.dump(self.__data, myfile)
        myfile.close()
