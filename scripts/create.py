#!/usr/bin/env python

"""
create the pyclassifiers main file
"""

import requests
import re

url = 'https://pypi.python.org/pypi?%3Aaction=list_classifiers'
r = requests.get(url)
assert r.status_code == 200
remove_re = re.compile("[ .,']")
replace_with_underscore = re.compile("[-/()+]")
replace_with_double_underscore = re.compile(" :: ")
replace_hash_with_sharp = re.compile("[#]")
replace_quote_with_backslash_quote = re.compile("'")
with open("pyclassifiers/values.py", "w") as file_handle:
    for x in r.content.decode().split("\n"):
        if not x:
            continue
        name = x
        name = replace_with_double_underscore.sub("__", name)
        name = remove_re.sub('', name)
        name = replace_with_underscore.sub("_", name)
        name = replace_hash_with_sharp.sub("sharp", name)
        value = x
        value = replace_quote_with_backslash_quote.sub("\\'", value)
        full_string = "{} = '{}'\n".format(name, value) 
        if len(full_string) >= 120:
            full_string = "{} = \\\n    '{}'\n".format(name, value)
        file_handle.write(full_string)
