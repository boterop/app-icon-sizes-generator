from bin.image_transform import ImageTransform
from bin.ios import IOS
import unittest
import os

FILE_FOLDER = "tests/"
FILE_NAME = "image"
FILE_EXT = ".jpg"
FILE_PATH = FILE_FOLDER+FILE_NAME+FILE_EXT
BUILD_FOLDER = "build/"+FILE_NAME+"/ios/"
RESULT_FOLDER = "AppStore/"
RESULT_NAME = "AppIconx1.png"

class TestIOS(unittest.TestCase):
    
    def test_init_with_transform(self):
        transform = ImageTransform(FILE_PATH)
        ios = IOS(transform)
        self.assertEqual(ios.transformer.image.filename, FILE_PATH)
    
    def test_init_with_path(self):
        ios = IOS(FILE_PATH)
        self.assertEqual(ios.transformer.image.filename, FILE_PATH)
    
    def test_create(self):
        IOS(FILE_PATH).create()
        self.assertTrue(os.path.exists(FILE_FOLDER+BUILD_FOLDER))
        self.assertTrue(os.path.exists(FILE_FOLDER+BUILD_FOLDER+RESULT_FOLDER))
        self.assertTrue(os.path.exists(FILE_FOLDER+BUILD_FOLDER+RESULT_FOLDER+RESULT_NAME))
    
    def test_create_build_folder(self):
        build_folder = IOS(FILE_PATH).create_build_folder()
        self.assertEqual(build_folder, FILE_FOLDER+BUILD_FOLDER)
        self.assertTrue(os.path.exists(FILE_FOLDER+BUILD_FOLDER))

if __name__ == '__main__':
    unittest.main()
