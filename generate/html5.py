import dominate
from dominate.tags import *
from generate import read


def build_html():
    doc = dominate.document(title='Dominate your HTML')

    with doc.head:
        link(rel='stylesheet', href='style.css')
        # script(type='text/javascript', src='script.js')
        with doc:
            with nav(cls='nav').add(ul()):
                for i in ['home', 'about', 'contact']:
                    li(a(i.title(), href='/%s.html' %i))

    with open(read.html, 'x') as f:
        f.write(doc.render())
