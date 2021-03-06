# encoding: utf-8
from ..tag_dispatchers import TagDispatcher, replace_whitespaces, lists_overlap, get_parental_tags


class EmphasisDispatcher(TagDispatcher):
    def __init__(self):
        super(EmphasisDispatcher, self).__init__()

    @classmethod
    def append_head(cls, element, container):
        return cls._append_emphasis(element.text, element, container)

    @classmethod
    def append_tail(cls, element, container):
        return cls._append_emphasis(element.tail, element, container)

    @classmethod
    def _append_emphasis(cls, text, element, container):
        """
        <em> Creates an italic text run inside the paragraph container.
        Appends remainder of text as a additional run
        """
        text = replace_whitespaces(text)
        run = container.add_run(text=text)
        run.italic = True
        if lists_overlap(get_parental_tags(element), ('strong', 'b')):
            run.bold = True
        if lists_overlap(get_parental_tags(element), ('u',)):
            run.underline = True
        return container