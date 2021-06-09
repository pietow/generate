from generate import write
from generate import ignore
write.create_ini()    
from generate import html5
from generate import css


def main():
    html5.build_html()
    print('**************index.html*********')
    css.build_css()
    print('**************css/style.css******')
    ignore.create_ignore()
    print('**************.gitignore******')
