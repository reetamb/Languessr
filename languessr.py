"""
Moran, Steven & McCloy, Daniel (eds.) 2019.
PHOIBLE 2.0.
Jena: Max Planck Institute for the Science of Human History.
(Available online at http://phoible.org, Accessed on 2023-05-25.)
"""

#this is supposed to be where the main stuff happens

import json

with open("languages.json", 'r') as file:
    langs = json.load(file)

print(langs.keys())