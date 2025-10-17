#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Unit tests for refactored conversion function."""

import unittest
from conversions_refactored import convert, ConversionNotPossible


class TestRefactoredConversions(unittest.TestCase):
    
    def test_temperature_conversions(self):
        """Test all temperature conversions."""
        print("\nTesting temperature conversions:")
        
        test_cases = [
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
            (1.0, 'Miles', 'Yards', 1760.0),
            (1.0, 'Miles', 'Meters', 1609.344),
            (1760.0, 'Yards', 'Miles', 1.0),
            (1.0, 'Yards', 'Meters', 0.9144),
            (1609.344, 'Meters', 'Miles', 1.0),
            (0.9144, 'Meters', 'Yards', 1.0),
        ]
        
        for value, fromUnit, toUnit, expected in test_cases:
            result = convert(fromUnit, toUnit, value)
            print(f"{value} {fromUnit} should be {expected} {toUnit} - ", end="")
            print("PASS" if abs(result - expected) < 0.01 else "FAIL")
            self.assertAlmostEqual(result, expected, places=2)
    
    def test_same_unit_conversions(self):
        """Test that converting to the same unit returns the same value."""
        print("\nTesting same unit conversions:")
        
        test_cases = [
            (100.0, 'Celsius', 'Celsius'),
            (100.0, 'Fahrenheit', 'Fahrenheit'),
            (100.0, 'Kelvin', 'Kelvin'),
            (100.0, 'Miles', 'Miles'),
            (100.0, 'Yards', 'Yards'),
            (100.0, 'Meters', 'Meters'),
        ]
        
        for value, fromUnit, toUnit in test_cases:
            result = convert(fromUnit, toUnit, value)
            print(f"{value} {fromUnit} to {toUnit} - ", end="")
            print("PASS" if result == value else "FAIL")
            self.assertEqual(result, value)
    
    def test_conversion_not_possible(self):
        """Test that mixing unit types raises ConversionNotPossible."""
        print("\nTesting invalid conversions:")
        
        invalid_conversions = [
            ('Celsius', 'Miles'),
            ('Fahrenheit', 'Meters'),
            ('Kelvin', 'Yards'),
            ('Miles', 'Celsius'),
            ('Yards', 'Fahrenheit'),
            ('Meters', 'Kelvin'),
        ]
        
        for fromUnit, toUnit in invalid_conversions:
            print(f"Converting {fromUnit} to {toUnit} should raise exception - ", end="")
            with self.assertRaises(ConversionNotPossible):
                convert(fromUnit, toUnit, 100.0)
            print("PASS")
    
    def test_negative_values(self):
        """Test conversions with negative values."""
        print("\nTesting negative value conversions:")
        
        test_cases = [
            (-40.0, 'Celsius', 'Fahrenheit', -40.0),
            (-273.15, 'Celsius', 'Kelvin', 0.0),
            (0.0, 'Kelvin', 'Celsius', -273.15),
        ]
        
        for value, fromUnit, toUnit, expected in test_cases:
            result = convert(fromUnit, toUnit, value)
            print(f"{value} {fromUnit} should be {expected} {toUnit} - ", end="")
            print("PASS" if abs(result - expected) < 0.01 else "FAIL")
            self.assertAlmostEqual(result, expected, places=2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
