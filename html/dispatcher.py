# encoding: utf-8

"""
Returns corresponding objects to call for creating
the different docx elements.
"""

from tag_dispatchers.blockquote import BlockquoteDispatcher
from tag_dispatchers.code import CodeDispatcher
from tag_dispatchers.emphasis import EmphasisDispatcher
from tag_dispatchers.heading import HeadingDispatcher
from tag_dispatchers.linebreak import LineBreakDispatcher
from tag_dispatchers.link import LinkDispatcher
from tag_dispatchers.list_item import ListItemDispatcher
from tag_dispatchers.paragraph import ParagraphDispatcher
from tag_dispatchers.strong import StrongDispatcher
from tag_dispatchers.underline import UnderlineDispatcher
from tag_dispatchers.div import DivDispatcher


def get_tag_dispatcher(html_tag):
    """
    Returning the object creating OOXML for the given HTML tag
    """
    return _dispatch_html.get(html_tag)


# map of HTML tags and their corresponding objects
heading_dispatcher = HeadingDispatcher()

_dispatch_html = dict(
    p=ParagraphDispatcher(),
    a=LinkDispatcher(),
    li=ListItemDispatcher(),
    br=LineBreakDispatcher(),
    div=DivDispatcher(),
    code=CodeDispatcher(),
    strong=StrongDispatcher(),
    b=StrongDispatcher(),
    i=EmphasisDispatcher(),
    u=UnderlineDispatcher(),
    em=EmphasisDispatcher(),
    h1=heading_dispatcher,
    h2=heading_dispatcher,
    h3=heading_dispatcher,
    h4=heading_dispatcher,
    h5=heading_dispatcher,
    h6=heading_dispatcher,
    blockquote=BlockquoteDispatcher(),
)
