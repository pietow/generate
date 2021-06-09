from configparser import ConfigParser

# instantiate
config = ConfigParser()

# parse existing file
config.read('config.ini')

# read values from a section
html = config.get('files', 'html')
css = config.get('files', 'css')
