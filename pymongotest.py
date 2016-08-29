from pymongo import MongoClient
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
parser_add.add_argument('-n', '--name',  help='The Snippets Name')
parser_add.set_defaults(func=add)

parser_remove = subparsers.add_parser('remove', help='remove help')
parser_remove.add_argument('-n', '--name',  help='The Snippets Name')
parser_remove.set_defaults(func=remove)

parser_find = subparsers.add_parser('find', help='find help')
parser_find.add_argument('search_term', help='find snippet containing \'searchterm\'')
parser_find.add_argument('-n', '--name',  help='find by name')
parser_find.add_argument('-t', '--tag',  help='find by snippets tag')
parser_find.add_argument('-c', '--content',  help='find by snippets content')
parser_find.set_defaults(func=find)

args = parser.parse_args()

args.func(args)

# client = MongoClient("mongodb://mongodb0.example.net:27017")
client = MongoClient()

snippets_collection = client.snippets.snippets


for num in range(10):
    snippets_collection.insert({'title':"snippet" + str(num), 'text':'snippet text' + str(num)})

cursor = snippets_collection.find()

for document in cursor:
    print(document)

# cleanup after test
snippets_collection.delete_many({})
