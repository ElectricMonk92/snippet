from tinydb import TinyDB, Query
from argparse import ArgumentParser
from snippet_find import find
from snippet_remove import remove
from snippet_add import add

parser = ArgumentParser()
group = parser.add_mutually_exclusive_group()

group.add_argument('-v', '--verbose', help='Verbose (debug) logging', action='store_true')
group.add_argument('-q', '--quiet', help='Silent mode, only log warnings', action='store_true')
parser.add_argument('--dry-run', help='No-op, do not write anything', action='store_true')
subparsers = parser.add_subparsers(help='sub-command help')

parser_add = subparsers.add_parser('add', help='add help')
parser_add.add_argument('-n', '--name',  help='The Snippets Name', required=True)
parser_add.add_argument('-t', '--tags',  help='The Snippets comma separated tags', nargs='+')
parser_add.add_argument('-c', '--content',  help='The Snippets content', required=True)
parser_add.set_defaults(func=add)

parser_remove = subparsers.add_parser('remove', help='remove help')
parser_remove.add_argument('-n', '--name',  help='The Snippets Name')
parser_remove.set_defaults(func=remove)

parser_find = subparsers.add_parser('find', help='find help')
#parser_find.add_argument('search_term', help='find snippet containing \'searchterm\'')
parser_find.add_argument('-n', '--name',  help='find by name')
parser_find.add_argument('-t', '--tags',  help='find by snippets tag', nargs='+')
parser_find.add_argument('-c', '--content',  help='find by snippets content')
parser_find.set_defaults(func=find)

args = parser.parse_args()

args.func(args)
