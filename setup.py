from setuptools import setup

APP = ['main.py']  # Cseréld le a scripted nevére
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['tkinter', 'requests'],  # Add hozzá a szükséges modulokat
    # Egyéb opciók, például a 'includes' lista, ha speciális modulokat kell belefoglalni
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)