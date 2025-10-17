#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Unit conversion module with temperature and distance conversions."""


class ConversionNotPossible(Exception):
    """Exception raised when conversion between units is not possible."""
    pass


def convert(fromUnit, toUnit, value):
    """
    Convert a value from one unit to another.
    
    Supports temperature conversions: Celsius, Fahrenheit, Kelvin
    Supports distance conversions: Miles, Yards, Meters
    
    Args:
        fromUnit (str): The unit to convert from
        toUnit (str): The unit to convert to
        value (float): The value to convert
        
    Returns:
        float: The converted value
        
    Raises:
        ConversionNotPossible: If the conversion is not supported
    """
    temperature_units = {'Celsius', 'Fahrenheit', 'Kelvin'}
    distance_units = {'Miles', 'Yards', 'Meters'}
    
    if fromUnit in temperature_units and toUnit in temperature_units:
        return convert_temperature(fromUnit, toUnit, value)
    elif fromUnit in distance_units and toUnit in distance_units:
        return convert_distance(fromUnit, toUnit, value)
    else:
        raise ConversionNotPossible(
            f"Cannot convert from {fromUnit} to {toUnit}"
        )


def convert_temperature(fromUnit, toUnit, value):
    """Convert between temperature units."""
    if fromUnit == toUnit:
        return value
    
    if fromUnit == 'Celsius':
        celsius = value
    elif fromUnit == 'Fahrenheit':
        celsius = (value - 32) * 5/9
    elif fromUnit == 'Kelvin':
        celsius = value - 273.15
    else:
        raise ConversionNotPossible(f"Unknown temperature unit: {fromUnit}")
    
    if toUnit == 'Celsius':
        return celsius
    elif toUnit == 'Fahrenheit':
        return celsius * 9/5 + 32
    elif toUnit == 'Kelvin':
        return celsius + 273.15
    else:
        raise ConversionNotPossible(f"Unknown temperature unit: {toUnit}")


def convert_distance(fromUnit, toUnit, value):
    """Convert between distance units."""
    if fromUnit == toUnit:
        return value
    
    if fromUnit == 'Miles':
        meters = value * 1609.344
    elif fromUnit == 'Yards':
        meters = value * 0.9144
    elif fromUnit == 'Meters':
        meters = value
    else:
        raise ConversionNotPossible(f"Unknown distance unit: {fromUnit}")
    
    if toUnit == 'Meters':
        return meters
    elif toUnit == 'Miles':
        return meters / 1609.344
    elif toUnit == 'Yards':
        return meters / 0.9144
    else:
        raise ConversionNotPossible(f"Unknown distance unit: {toUnit}")
