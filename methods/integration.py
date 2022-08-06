# coding:utf-8

methods = {}


def method_register(method):
    """Method register which can register methods to the dict 'methods'. And then we can easily use these methods."""
    methods[method.__name__] = method
    return method
