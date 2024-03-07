import sys
import os

# Adds the parent directory of the test directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import unittest
from TJClean import extract_figures

class TestExtractFigures(unittest.TestCase):
    def test_extract_figures_daily_rate(self):
        text = "The daily rate is £100 per day"
        self.assertEqual(extract_figures(text), "daily rate")

    def test_extract_figures_hourly_rate(self):
        text = "The hourly rate is £50 per hour"
        self.assertEqual(extract_figures(text), "hourly rate")

    def test_extract_figures_with_figures(self):
        text = "The project pays £40000 sdvdfgedghbfghb £20 lkhlhvjhvbjhbbkbh"
        self.assertEqual(extract_figures(text), [40000.0, 20.0])

    def test_extract_figures_no_match(self):
        text = "This text contains no payment information"
        self.assertEqual(extract_figures(text), [])

    def test_extract_figures_empty_string(self):
        text = ''
        self.assertEqual(extract_figures(text), [])

    def test_extract_figures_invalid_format(self):
        text = "The price is £1.2.3.4"
        self.assertEqual(extract_figures(text), [1.2])

if __name__ == '__main__':
    unittest.main()
