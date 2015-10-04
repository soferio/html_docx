# encoding: utf-8
from ..tag_dispatchers import TagDispatcher, replace_whitespaces, lists_overlap, get_parental_tags


class UnderlineDispatcher(TagDispatcher):
    def __init__(self):
        super(UnderlineDispatcher, self).__init__()

    @classmethod
    def append_head(cls, element, container):
        return cls._append_underline(element.text, element, container)

    @classmethod
    def append_tail(cls, element, container):
        return cls._append_underline(element.tail, element, container)

    @classmethod
    def _append_underline(cls, text, element, container):
        """
        <em> Creates an underline text run inside the paragraph container.
        Appends remainder of text as a additional run
        """
        text = replace_whitespaces(text)
        run = container.add_run(text=text)
        run.underline = True
        if lists_overlap(get_parental_tags(element), ('strong', 'b')):
            run.bold = True
        if lists_overlap(get_parental_tags(element), ('em', 'i')):
            run.italic = True
        return container