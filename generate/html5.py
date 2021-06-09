import dominate
from dominate.tags import *
from dominate import tags as tags
from generate import read


def build_html():
    doc = dominate.document(title='Dominate your HTML')

    with doc.head:
        tags.meta(charset='UTF-8')
        tags.meta(name='viewport', content='width=device-width, initial-scale=1.0')
        link(rel='stylesheet', href='style.css')
        # script(type='text/javascript', src='script.js')
        with doc:
            with nav(cls='nav').add(ul()):
                for i in ['home', 'about', 'contact']:
                    li(a(i.title(), href='/%s.html' %i))

    with open(read.html, 'x') as f:
        f.write(doc.render())
