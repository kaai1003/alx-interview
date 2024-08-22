#!/usr/bin/python3
"""UTF-8 check Module"""


def check_byte(byte):
    """check number of bytes"""
    if (byte >> 5) == 0b110:
        return 1
    if (byte >> 4) == 0b1110:
        return 2
    if (byte >> 3) == 0b11110:
        return 3
    if (byte >> 7):
        return 0


def validUTF8(data):
    """utf-8 validation func"""
    char_bytes = 0
    for byte in data:
        byte &= 0xFF
        if char_bytes == 0:
            char_bytes = check_byte(byte)
            if char_bytes == 0:
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            char_bytes -= 1
    return True
