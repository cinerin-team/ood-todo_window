from setuptools import setup

APP = ['main.py']  # Cseréld le a scripted nevére
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['tkinter', 'requests', 'lxml', 'importlib', 'config'],  # Add hozzá a szükséges modulokat
    'includes': ['dashboard', 'cinerin_tc', 'config']# Egyéb opciók, például a 'includes' lista, ha speciális modulokat kell belefoglalni
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)