# encoding: utf-8
from ..tag_dispatchers import TagDispatcher, replace_whitespaces


class DivDispatcher(TagDispatcher):
    def __init__(self):
        super(DivDispatcher, self).__init__()

    @classmethod
    def append_head(cls, element, container):
        paragraph = cls.get_new_paragraph(container)
        return cls._append_div(element.text, element, paragraph)

    @classmethod
    def append_tail(cls, element, container):
        paragraph = cls.get_current_paragraph(container)
        return cls._append_div(element.tail, element, paragraph)

    @classmethod
    def _append_div(cls, text, element, container):
        """
        <div> does nothing.
        """
        text = replace_whitespaces(text)
        if not text:
            return container

        style = None
        if element.getparent().tag == 'blockquote':
            style = 'IntenseQuote'

        container.add_run(text=text, style=style)
        return container