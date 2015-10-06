Extract from discussion at: https://github.com/python-openxml/python-docx/issues/49#issuecomment-63951331

What it does: It takes an element tree, representing the HTML structure of your markdown (using https://github.com/waylan/Python-Markdown to convert) and creates the corresponding docx elements inside a paragraph. Obviously it uses python-docx to to that.

paragraph = document.add_paragraph()
html_tree = markdown(markdown_string)
add_html(paragraph, html_tree)

How it works:
It's basically a module you put inside your sources and import the interface method add_html. This method takes your container element (paragraph) and recursively steps through the html element tree. This happens in _append_docx_elements inside the DocxBuilder class. It maps the HTML tag to a dispatcher class from the tag_dispatchers directory, hands over the tag content, recursively calls its children and hands over the tag tail after doing so.
The dispatcher classes call the python-docx functions to create the appropriate objects. They share some helper methods which figure out which kind of container we are in and provide fitting paragraph objects.

This won't be able to handle all kind of HTML input, but the basic output of markdown is mapped pretty OK to docx.
