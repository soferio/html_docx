# encoding: utf-8

"""
Wrapper methods used for mapping HTML to docx objects
Obtained from: https://github.com/fokoenecke/html_docx
"""

import re

from lxml.html import fromstring
from converter import DocxBuilder


def add_html(container, html_string):
    
    # NOTE: Added for backward compatibility with line breaks in text
    html_string = re.sub('\n', '<br>', html_string)
    
    root = fromstring(html_string)
    builder = DocxBuilder(container=container)
    builder.from_html_tree(root=root)