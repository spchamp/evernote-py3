# Evernote API (Unofficial)

import os

def get_version() -> str:
    src = os.path.join(os.path.dirname(__file__),
                       "edam/userstore/constants.py")
    versions = [mmv.split("=")[1].lstrip() for mmv in open(
        src).read().split("\n") if mmv.startswith('EDAM_VERSION')]
    return ".".join(versions)


VERSION: str = get_version()
