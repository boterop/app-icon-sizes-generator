from bin.android import Android
from bin.ios import IOS


class GUI:
    def __init__(self):
        path = input("Image path: ").replace("'", "")
        Android(path).create()
        IOS(path).create()
