ignore = 'config.ini'

def create_ignore():
    with open('.gitignore', 'x') as f:
        f.write(ignore)



