import sys
import os

# Adds the parent directory of the test directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from TJClean import extract_figures

# Test for daily rate
def test_extract_figures_daily_rate():
    text = "The daily rate is £100 per day"
    assert extract_figures(text) == "daily rate"

# Test for hourly rate
def test_extract_figures_hourly_rate():
    text = "The hourly rate is £50 per hour"
    assert extract_figures(text) == "hourly rate"

# Test with figures
def test_extract_figures_with_figures():
    text = "The project pays £40000 sdvdfgedghbfghb £20 lkhlhvjhvbjhbbkbh"
    assert extract_figures(text) == [40000.0, 20.0]

# Test when no match found
def test_extract_figures_no_match():
    text = "This text contains no payment information"
    assert extract_figures(text) == []

# Test with empty string
def test_extract_figures_empty_string():
    text = ''
    assert extract_figures(text) == []

# Test with invalid format
def test_extract_figures_invalid_format():
    text = "The price is £1.2.3.4"
    assert extract_figures(text) == [1.2]
