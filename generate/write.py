ini = '''[files]
html = index.html
css = style.css
assets = image
'''

def create_ini():
    with open('config.ini', 'x') as f:
        f.write(ini)



