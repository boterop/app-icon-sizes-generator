from bin.image_transform import ImageTransform
import os

BUILD_FOLDER = "build"
FOLDER_NAME = "mipmap"
IMAGE_NAME = "ic_launcher"
IMAGE_EXT = ".png"
DPI = [("h", 72), ("m", 48), ("xh", 96), ("xxh", 144), ("xxxh", 192)]


class Android:
    def __init__(self, transformer: ImageTransform | str):
        if isinstance(transformer, str):
            self.transformer = ImageTransform(transformer)
        elif isinstance(transformer, ImageTransform):
            self.transformer = transformer

    def create(self):
        build_path = self.create_build_folder()
        for dpi in DPI:
            name, size = dpi
            dpi_path = build_path + FOLDER_NAME + "-" + name + "dpi/"

            if not os.path.exists(dpi_path):
                os.mkdir(dpi_path)
            self.transformer.resize(size, size)
            self.transformer.save(dpi_path + IMAGE_NAME + IMAGE_EXT)

    def create_build_folder(self):
        path = self.transformer.path
        image_name = self.transformer.image_name
        build_path = path + "/" + BUILD_FOLDER + "/" + image_name + "/"

        bread = ""
        for folder in build_path.split("/"):
            bread += folder + "/"
            if not os.path.exists(bread):
                os.mkdir(bread)
        return build_path
