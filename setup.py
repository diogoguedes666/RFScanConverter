from setuptools import setup

APP = ['RFSCANCONVERTER.py']
DATA_FILES = [('',['roadcase.gif'])]

OPTIONS = {
    'argv_emulation': True,
    'packages': ['tkinter'],
    'iconfile': 'roadcase.icns'
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
