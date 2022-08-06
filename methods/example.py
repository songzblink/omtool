# coding:utf-8
from methods.integration import method_register


@method_register
def count():
    print("count is running")
