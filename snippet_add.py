from tinydb import TinyDB, Query
import constants

def add(args):
    print args
    name    = args.name
    tags    = args.tags
    content = args.content

    print("Name {}".format(name))
    print("Tags {}".format(tags))
    print("Content {}".format(content))

    snippet_to_insert = {
        constants.NAME_FIELD    : name,
        constants.TAGS_FIELD    : tags,
        constants.CONTENT_FIELD : content
    }

    db = TinyDB('db.json')
    snippets = db.table(constants.SNIPPETS_TABLE)
    snippets.insert(snippet_to_insert)

    print "Sucessfully inserted snippet: ", name
