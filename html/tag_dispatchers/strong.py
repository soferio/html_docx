# encoding: utf-8
from ..tag_dispatchers import TagDispatcher, replace_whitespaces, lists_overlap, get_parental_tags


class StrongDispatcher(TagDispatcher):
    def __init__(self):
        super(StrongDispatcher, self).__init__()

    @classmethod
    def append_head(cls, element, container):
        return cls._append_strong(element.text, element, container)

    @classmethod
    def append_tail(cls, element, container):
        return cls._append_strong(element.tail, element, container)

    @classmethod
    def _append_strong(cls, text, element, container):
        """
        <strong> Creates a bold text run inside the paragraph container.
        Appends remainder of text as a additional run
        """
        text = replace_whitespaces(text)
        run = container.add_run(text=text)
        run.bold = True
        if lists_overlap(get_parental_tags(element), ('em', 'i')):
            run.italic = True
        if lists_overlap(get_parental_tags(element), ('u',)):
            run.underline = True
        return container