#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Unit tests for refactored conversion function."""

import unittest
from conversions_refactored import convert, ConversionNotPossible


class TestRefactoredConversions(unittest.TestCase):
    
    def test_temperature_conversions(self):
        print("\nTesting temperature conversions:")
        
        test_cases = [
            # (value, fromUnit, toUnit, expected)
            (0.0, 'Celsius', 'Kelvin', 273.15),
            (100.0, 'Celsius', 'Fahrenheit', 212.0),
            (32.0, 'Fahrenheit', 'Celsius', 0.0),
            (98.6, 'Fahrenheit', 'Kelvin', 310.15),
            (273.15, 'Kelvin', 'Celsius', 0.0),
            (373.15, 'Kelvin', 'Fahrenheit', 212.0),
        ]
        
        for value, fromUnit, toUnit, expected in test_cases:
            result = convert(fromUnit, toUnit, value)
            print(f"{value} {fromUnit} should be {expected} {toUnit} - ", end="")
            print("PASS" if abs(result - expected) < 0.01 else "FAIL")
            self.assertAlmostEqual(result, expected, places=2)
    
    def test_distance_conversions(self):
        """Test all distance conversions."""
        print("\nTesting distance conversions:")
        
        test_cases = [
            # (value, fromUnit, toUnit, expected)
            (1.0, 'Miles', 'Yards', 1760.0),
            (1.0, 'Miles', 'Meters', 1609.344),
            (1760.0, 'Yards', 'Miles', 1.0),
            (1.0, 'Yards', 'Meters', 0.9144),
            (1609.344, 'Meters', 'Miles', 1.0),
            (0.9144, 'Meters', 'Yards', 1.0),
        ]
        
        for value
