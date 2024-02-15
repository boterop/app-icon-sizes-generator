from bin.image_transform import ImageTransform
from bin.mobile import Mobile

OS = "ANDROID"
FOLDER_NAME = "mipmap-"
IMAGE_NAME = "ic_launcher"
DPI_NAME = "dpi"
DPI = [("h", "", 72), ("m", "", 48), ("xh", "", 96), ("xxh", "", 144), ("xxxh", "", 192)]


class Android(Mobile):
    def __init__(self, transformer: ImageTransform | str):
        Mobile.__init__(self, transformer, OS, DPI, IMAGE_NAME, FOLDER_NAME, DPI_NAME)
