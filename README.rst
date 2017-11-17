=========
rr.typing
=========

This module defines functions for checking object types (`check_type()`) and subclasses (`check_subclass()`). These functions take the same arguments as `isinstance()` and `issubclass()`, respectively. This is normally useful in functions where we want to enforce argument types. Example usage:

.. code-block:: python

    from rr import typing

    typing.check_type(3, int)
    typing.check_subclass(list, object)


Compatibility
=============

Developed and tested in Python 3.6+. The code may or may not work under earlier versions of Python 3 (perhaps back to 3.3).


Installation
============

From the github repo:

.. code-block:: bash

    pip install git+https://github.com/2xR/rr.typing.git


License
=======

This library is released as open source under the MIT License.

Copyright (c) 2017 Rui Rei
