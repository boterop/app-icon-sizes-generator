from bin.android import Android


class GUI:
    def __init__(self):
        path = input("Image path: ").replace("'", "")
        Android(path).create()
