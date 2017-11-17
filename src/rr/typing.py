"""This module defines some functions that make it easier to check types of objects and
subclasses and provide good informative error messages when the types don't match.
"""

__version__ = "0.1.0"
__author__ = "Rui Rei"
__copyright__ = "Copyright 2017 {author}".format(author=__author__)
__license__ = "MIT"


def check_type(obj, cls):
    """Raise a TypeError if `obj` is not as instance of `cls`.

    The parameter `cls` has the same semantics as the built-in `isinstance()`.

    Returns `obj` if the type check passes.
    """
    if not isinstance(obj, cls):
        raise not_an_instance(obj, cls)
    return obj


def check_subclass(cls, super_cls):
    """Similar to check_type(), but for checking if a class is a subclass of another."""
    if not issubclass(cls, super_cls):
        raise not_a_subclass(cls, super_cls)
    return cls


def not_an_instance(obj, cls):
    """Creates a TypeError instance with a helpful description of the error."""
    name = [c.__name__ for c in cls] if isinstance(cls, tuple) else cls.__name__
    return _unexpected_type(expected=name, actual=type(obj).__name__)


def not_a_subclass(cls, super_cls):
    """Creates a TypeError instance with a helpful description of the error."""
    name = [c.__name__ for c in super_cls] if isinstance(super_cls, tuple) else super_cls.__name__
    return _unexpected_type(expected="subclass of {}".format(name), actual=cls.__name__)


def _unexpected_type(expected, actual):
    return TypeError("expected {}, got {} instead".format(expected, actual))
