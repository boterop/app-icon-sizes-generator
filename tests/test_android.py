from bin.image_transform import ImageTransform
from bin.android import Android
import unittest
import os

FILE_FOLDER = "tests/"
FILE_NAME = "image"
FILE_EXT = ".jpg"
FILE_PATH = FILE_FOLDER+FILE_NAME+FILE_EXT
BUILD_FOLDER = "build/"+FILE_NAME+"/android/"
RESULT_FOLDER = "mipmap-"
DPI = "dpi/"
RESULT_NAME = "ic_launcher.png"
ROUND_RESULT_NAME = "ic_launcher_round.png"

class TestAndroid(unittest.TestCase):
    
    def test_init_with_transform(self):
        transform = ImageTransform(FILE_PATH)
        android = Android(transform)
        self.assertEqual(android.transformer.image.filename, FILE_PATH)
    
    def test_init_with_path(self):
        android = Android(FILE_PATH)
        self.assertEqual(android.transformer.image.filename, FILE_PATH)
    
    def test_create(self):
        Android(FILE_PATH).create()
        self.assertTrue(os.path.exists(FILE_FOLDER+BUILD_FOLDER))
        self.assertTrue(os.path.exists(FILE_FOLDER+BUILD_FOLDER+RESULT_FOLDER+"h"+DPI))
        self.assertTrue(os.path.exists(FILE_FOLDER+BUILD_FOLDER+RESULT_FOLDER+"m"+DPI))
        self.assertTrue(os.path.exists(FILE_FOLDER+BUILD_FOLDER+RESULT_FOLDER+"xh"+DPI))
        self.assertTrue(os.path.exists(FILE_FOLDER+BUILD_FOLDER+RESULT_FOLDER+"xxh"+DPI))
        self.assertTrue(os.path.exists(FILE_FOLDER+BUILD_FOLDER+RESULT_FOLDER+"xxxh"+DPI))
        
        self.assertTrue(os.path.exists(FILE_FOLDER+BUILD_FOLDER+RESULT_FOLDER+"h"+DPI+RESULT_NAME))
        self.assertTrue(os.path.exists(FILE_FOLDER+BUILD_FOLDER+RESULT_FOLDER+"m"+DPI+RESULT_NAME))
        self.assertTrue(os.path.exists(FILE_FOLDER+BUILD_FOLDER+RESULT_FOLDER+"xh"+DPI+RESULT_NAME))
        self.assertTrue(os.path.exists(FILE_FOLDER+BUILD_FOLDER+RESULT_FOLDER+"xxh"+DPI+RESULT_NAME))
        self.assertTrue(os.path.exists(FILE_FOLDER+BUILD_FOLDER+RESULT_FOLDER+"xxxh"+DPI+RESULT_NAME))
    
    def test_create_build_folder(self):
        build_folder = Android(FILE_PATH).create_build_folder()
        self.assertEqual(build_folder, FILE_FOLDER+BUILD_FOLDER)
        self.assertTrue(os.path.exists(FILE_FOLDER+BUILD_FOLDER))
    
    def test_create_round(self):
        Android(FILE_PATH).create()
        self.assertTrue(os.path.exists(FILE_FOLDER+BUILD_FOLDER+RESULT_FOLDER+"h"+DPI+ROUND_RESULT_NAME))
        self.assertTrue(os.path.exists(FILE_FOLDER+BUILD_FOLDER+RESULT_FOLDER+"m"+DPI+ROUND_RESULT_NAME))
        self.assertTrue(os.path.exists(FILE_FOLDER+BUILD_FOLDER+RESULT_FOLDER+"xh"+DPI+ROUND_RESULT_NAME))
        self.assertTrue(os.path.exists(FILE_FOLDER+BUILD_FOLDER+RESULT_FOLDER+"xxh"+DPI+ROUND_RESULT_NAME))
        self.assertTrue(os.path.exists(FILE_FOLDER+BUILD_FOLDER+RESULT_FOLDER+"xxxh"+DPI+ROUND_RESULT_NAME))

if __name__ == '__main__':
    unittest.main()
