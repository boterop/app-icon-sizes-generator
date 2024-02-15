from PIL import Image


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
