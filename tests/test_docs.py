"""
Documentation testing

Inspired by: https://github.com/cprogrammer1994/ModernGL/blob/master/tests/test_documentation.py
by Szabolcs Dombi

This version is simplified:

* Only test if the attribute or method/function is present in the class. Parameters are not inspected.
* Include ignore pattern in the implemented set
"""
import os
import re
import types
import unittest
from importlib import import_module


class DocTestCase(unittest.TestCase):
    """
    Test reference docs
    """
    def validate(self, filename, module, classname=None, ignore=None):
        """
        Finds all automethod and autoattribute statements in an rst file
        comparing them to the attributes found in the actual class
        """
        if ignore is None:
            ignore = []

        with open(os.path.normpath(os.path.join('docs', 'reference', filename))) as f:
            docs = f.read()

        module = import_module(module)

        # Inspect class
        if classname:
            methods = re.findall(r'^\.\. automethod:: ([^\(\n]+)', docs, flags=re.M)
            attributes = re.findall(r'^\.\. autoattribute:: ([^\n]+)', docs, flags=re.M)

            documented = set(filter(lambda x: x.startswith(classname), [a for a in methods] + attributes))
            implemented = set(classname + '.' + x for x in dir(getattr(module, classname))
                              if not x.startswith('_') or x == '__init__')
            ignored = set(classname + '.' + x for x in ignore)
        # Inspect module
        else:
            # Only inspect functions for now
            functions = re.findall(r'^\.\. autofunction:: ([^\(\n]+)', docs, flags=re.M)
            documented = set(functions)
            ignored = set(ignore)
            implemented = set(func for func in dir(module) if isinstance(getattr(module, func), types.FunctionType))

        self.assertSetEqual(implemented - documented - ignored, set(), msg='Implemented but not Documented')
        self.assertSetEqual(documented - implemented - ignored, set(), msg='Documented but not Implemented')

    def test_opengl_registry_reader(self):
        self.validate(
            'reader.rst',
            'opengl_registry.reader',
            classname='RegistryReader',
            ignore=[],
        )
