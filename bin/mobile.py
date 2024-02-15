from bin.image_transform import ImageTransform
import os

BUILD_FOLDER = "build"
IMAGE_EXT = ".png"


class Mobile:
    def __init__(
        self,
        transformer: ImageTransform | str,
        os: str,
        dpi: list,
        image_name: str,
        folder_name: str,
        dpi_name: str,
    ):
        self.os = os.lower()
        self.dpi = dpi
        self.image_name = image_name
        self.folder_name = folder_name
        self.dpi_name = dpi_name
        if isinstance(transformer, str):
            self.transformer = ImageTransform(transformer)
        elif isinstance(transformer, ImageTransform):
            self.transformer = transformer

    def create(self):
        build_path = self.create_build_folder()
        for dpi in self.dpi:
            name, image_name, size = dpi
            dpi_path = build_path + self.folder_name + name + self.dpi_name + "/"

            if not os.path.exists(dpi_path):
                os.mkdir(dpi_path)
            self.transformer.resize(size, size)
            self.transformer.save(dpi_path + self.image_name + image_name + IMAGE_EXT)

    def create_build_folder(self):
        path = self.transformer.path
        image_name = self.transformer.image_name
        build_path = path + "/" + BUILD_FOLDER + "/" + image_name + "/" + self.os + "/"

        bread = ""
        for folder in build_path.split("/"):
            bread += folder + "/"
            if not os.path.exists(bread):
                os.mkdir(bread)
        return build_path
