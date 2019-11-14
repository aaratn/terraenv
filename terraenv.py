#!/usr/bin/env python
import argparse
from commands import list_local, list_remote, install, use, uninstall
from sys import exit

class Parser(argparse.ArgumentParser):
    def error(self, message):
        self.print_help()
        exit(1)

parser = Parser(description='Manage Terraform and Terragrunt versions')
parser.add_argument('program', choices=['terraform', 'terragrunt'], help='program')

commands = parser.add_subparsers(title='commands', dest='commands')
commands.required = True


# list
list_cmd_parser = commands.add_parser('list', help='List Versions')

list_cmds = list_cmd_parser.add_subparsers(dest='location')
list_cmds.required = True

list_local_cmd = list_cmds.add_parser('local', help='List Local Versions')
list_local_cmd.set_defaults(func=list_local)

list_remote_cmd = list_cmds.add_parser('remote', help='List Remote Versions')
list_remote_cmd.set_defaults(func=list_remote)

# Install
install_cmd_parser = commands.add_parser('install', help='Install specific version or version defined in .terraenv file')
install_cmd_parser.add_argument('version', type=str, help='Version to install', nargs="?", default="")
install_cmd_parser.set_defaults(func=install)

# Uninstall
uninstall_cmd_parser = commands.add_parser('uninstall', help='Uninstall specific version')
uninstall_cmd_parser.add_argument('version', type=str, help='Version to install', nargs="?", default="")
uninstall_cmd_parser.set_defaults(func=uninstall)

# Use
use_cmd_parser = commands.add_parser('use', help='Use program version')
use_cmd_parser.add_argument('version', type=str, help='Version to use', nargs="?", default="")
use_cmd_parser.set_defaults(func=use)

args = parser.parse_args()
args.func(args)