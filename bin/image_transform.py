import numpy as np
from PIL import Image, ImageDraw


class ImageTransform:
    def __init__(self, path: str):
        file = path.split("/")[-1]
        self.path = "/".join(path.split("/")[0:-1])
        self.image_name = ".".join(file.split(".")[0:-1])
        self.image_extension = file.split(".")[-1]
        self.image = Image.open(path)

    def resize(self, width: int, height: int):
        self.new_image = self.image.resize((width, height))

    def save(self, path: str):
        self.new_image.save(path)

    def round(self):
        img = self.image if self.new_image == None else self.new_image
        img = img.convert("RGB") if self.image_extension != "jpg" else img
        npImage = np.array(img)
        height, width = img.size

        alpha = Image.new("L", img.size, 0)
        draw = ImageDraw.Draw(alpha)
        draw.pieslice([0, 0, height, width], 0, 360, fill=255)

        npAlpha = np.array(alpha)

        npImage = np.dstack((npImage, npAlpha))

        self.new_image = Image.fromarray(npImage)
