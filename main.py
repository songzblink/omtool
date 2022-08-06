# coding:utf-8
"""
Entry of this project, 'shell' command will execute this file and transport some parameters.
"""

import argparse
from methods import integration, example

# registered methods
methods = integration.methods


parser = argparse.ArgumentParser(prog="omtool", description="control and manage tool")

# sub command
subparsers = parser.add_subparsers(title="Custom tools", help="Customize a tool to control and manage the system.")
parser_count = subparsers.add_parser("count", help="Get the number of objects in the current directory.")
# bind default method
parser_count.set_defaults(func=methods["count"])

args = parser.parse_args()
args.func()
