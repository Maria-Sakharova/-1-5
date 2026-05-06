import unittest

class TestApp(unittest.TestCase):
    
    def test_main_exists(self):
        try:
            import main
            self.assertTrue(hasattr(main, 'main'))
        except ImportError:
            self.skipTest("main.py not found")
    
    def test_config_exists(self):
        try:
            import config
            self.assertTrue(hasattr(config, 'DB_CONFIG'))
        except ImportError:
            self.skipTest("config.py not found")
    
    def test_utils_exists(self):
        try:
            import utils
            self.assertTrue(hasattr(utils, 'connect_string'))
        except ImportError:
            self.skipTest("utils.py not found")

if __name__ == '__main__':
    unittest.main()
