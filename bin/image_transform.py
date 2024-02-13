from PIL import Image

class ImageTransform():
    def __init__(self, path):
        file = path.split("/")[-1]
        self.path = "/".join(path.split("/")[0:-1])
        self.image_name = file.split(".")[0:-1]
        self.image_extension = file.split(".")[-1]
        self.image = Image.open(path)

    def resize(self, width, height):
        self.new_image = self.image.resize((width, height))
        
    def save(self, path):
        self.new_image.save(path)
    
    def show_original(self):
        self.image.show()
    
    def show_result(self):
        self.new_image.show()
