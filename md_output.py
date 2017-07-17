"""
A sphinx extension to output markdown files.
"""


from sphinx.builders import Builder


def setup(app):
    "sphinx setup function"
    pass


class MdBuilder(Builder):
    "a markown-outputting Builder"
