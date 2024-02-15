from bin.mobile import Mobile
from bin.image_transform import ImageTransform

OS = "IOS"
IMAGE_NAME = "AppIcon"
DPI = [
    ("AppStore", "x1", 1024),
    ("20", "x2", 40),
    ("20", "x3", 60),
    ("29", "x2", 58),
    ("29", "x3", 87),
    ("40", "x2", 80),
    ("40", "x3", 120),
    ("60", "x2", 120),
    ("60", "x3", 180),
]

class IOS(Mobile):
    def __init__(self, transformer: ImageTransform | str):
        Mobile.__init__(self, transformer, OS, DPI, IMAGE_NAME, "", "")
