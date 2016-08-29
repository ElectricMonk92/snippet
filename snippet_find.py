from tinydb import TinyDB, Query
import constants
import mdv
import re

## config like this:
#Mdv.term_columns = 60
#
## calling like this (all CLI options supported, check def main
#Formatted = mdv.main(my_raw_markdown, c_theme=...)

def find(args):
    print("find")

    print args
    name = args.name
    tags = args.tags
    content = args.content

    sanitized_name = re.escape(name)
    sanitized_content = re.escape(content)

    db = TinyDB('db.json')
    snippets = db.table(constants.SNIPPETS_TABLE)

    print "Searching for snippets where:"
    if not name == None: 
        print("its name matches: ", name)
    if not content == None: 
        print("its content matches: ", content)
    if not tags == None: 
        print("has tag(s): ", tags)

    query = Query()
    res = snippets.search(query.name.search(sanitized_name) & query.content.search(sanitized_content) & query.tags.any(tags))

    output = ""
    for r in res:
        output += "#" + r["name"] + "\n"
        output += "tags:\n\n" + "\n".join(["* " + x for x in r["tags"]]) + "\n\n"
        output += r["content"] + "\n"
        output += "\n"

    print mdv.main(output)

