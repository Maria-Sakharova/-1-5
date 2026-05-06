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

class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        from calculator import Calculator
        self.assertEqual(Calculator.add(2, 3), 5)
        self.assertEqual(Calculator.add(-1, 1), 0)
    
    def test_subtract(self):
        from calculator import Calculator
        self.assertEqual(Calculator.subtract(5, 3), 2)
        self.assertEqual(Calculator.subtract(0, 5), -5)
    
    def test_multiply(self):
        from calculator import Calculator
        self.assertEqual(Calculator.multiply(2, 3), 6)
        self.assertEqual(Calculator.multiply(0, 5), 0)
    
    def test_divide(self):
        from calculator import Calculator
        self.assertEqual(Calculator.divide(6, 3), 2)
        with self.assertRaises(ValueError):
            Calculator.divide(5, 0)
