from bin.image_transform import ImageTransform
from bin.android import Android
import unittest
import os

FILE_FOLDER = "tests/"
FILE_NAME = "image"
ICON_NAME = "icon"
FILE_EXT = ".jpg"
PNG = ".png"
FILE_PATH = FILE_FOLDER + FILE_NAME + FILE_EXT
BUILD_FOLDER = f"build/{FILE_NAME}/android/"
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
        self._check_folder_exist(RESULT_NAME)

    def test_create_build_folder(self):
        build_folder = Android(FILE_PATH).create_build_folder()
        self.assertEqual(build_folder, FILE_FOLDER + BUILD_FOLDER)
        self.assertTrue(os.path.exists(FILE_FOLDER + BUILD_FOLDER))

    def test_create_round(self):
        Android(FILE_PATH).create()
        self._check_folder_exist(ROUND_RESULT_NAME)

    def test_round_in_png(self):
        Android(FILE_FOLDER + ICON_NAME + PNG).create()
        self._check_folder_exist(ROUND_RESULT_NAME)

    def _check_folder_exist(self, arg0):
        result_absolute_folder = FILE_FOLDER + BUILD_FOLDER + RESULT_FOLDER
        dpi = DPI + arg0
        self.assertTrue(os.path.exists(f"{result_absolute_folder}h{dpi}"))
        self.assertTrue(os.path.exists(f"{result_absolute_folder}m{dpi}"))
        self.assertTrue(os.path.exists(f"{result_absolute_folder}xh{dpi}"))
        self.assertTrue(os.path.exists(f"{result_absolute_folder}xxh{dpi}"))
        self.assertTrue(os.path.exists(f"{result_absolute_folder}xxxh{dpi}"))


if __name__ == "__main__":
    unittest.main()
