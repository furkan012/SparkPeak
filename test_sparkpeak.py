# test_sparkpeak.py
"""
Tests for SparkPeak module.
"""

import unittest
from sparkpeak import SparkPeak

class TestSparkPeak(unittest.TestCase):
    """Test cases for SparkPeak class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SparkPeak()
        self.assertIsInstance(instance, SparkPeak)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SparkPeak()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
