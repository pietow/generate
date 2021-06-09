from setuptools import setup

setup(
    name = 'generate',
    version = '0.1',
    description = '',
    author = 'piet',
    url = '',
    license = 'MIT',
    packages = ['generate'],
    entry_points = {'console_scripts': ['mak = generate.command_line:main',],},
)
