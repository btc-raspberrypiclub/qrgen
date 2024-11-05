import unittest
import os
from PIL import Image, ImageColor
from helpers import resize_logo,change_logo_color
from unittest.mock import patch, MagicMock

class TestHelpers(unittest.TestCase):
    def setUp(self):
        # Create a simple test logo
        self.logo = Image.new('RGB', (100, 100), 'red')
        self.logo.save('test_logo.png')

    def tearDown(self):
        if os.path.exists('test_logo.png'):
            os.remove('test_logo.png')

    def test_resize_logo(self):
        basewidth = 200
        logo = resize_logo(self.logo, basewidth)
        
        self.assertEqual(logo.size[0], basewidth)
        self.assertEqual(logo.size[1], basewidth)
        
    def test_change_logo_color(self):
        color = "blue"
        logo= change_logo_color(self.logo, color)
        
        expected_rgb = ImageColor.getcolor(color, "RGB")
        
        self.assertEqual(logo.getcolors(1000)[0][1], expected_rgb)    

        
    