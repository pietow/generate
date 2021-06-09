import os
from generate import read

def build_css():
    current_directory = os.getcwd()
    final_directory = os.path.join(current_directory, 'css')
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)

    final_file = os.path.join(final_directory, read.css)

    css = ''':root {
        box-sizing: border-box;
    }

    *,
    ::before,
    ::after {
        box-sizing: inherit;
    }

    body {
        margin: 0;
    }
    '''

    with open(final_file,'x') as f:
        f.write(css)





