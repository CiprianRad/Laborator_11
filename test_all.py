import unittest
from unittest import TextTestRunner

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir = 'tests')
    runner = TextTestRunner(verbosity = 2)
    runner.run(suite)
