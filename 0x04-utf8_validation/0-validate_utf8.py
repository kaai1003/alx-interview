#!/usr/bin/python3
"""UTF-8 check Module"""


def check_byte(byte):
    """check number of bytes"""
    count = 0
    mask = 1 << 7
    while mask & byte:
        count += 1
        mask = mask >> 1
    return count


def validUTF8(data):
    """utf-8 validation func"""
    char_bytes = 0
    for byte in data:
        if char_bytes == 0:
            char_bytes = check_byte(byte)
            if char_bytes == 0:
                continue
            if char_bytes == 1 or char_bytes > 4:
                return False
        else:
            byte = byte & 0xFF
            if (byte >> 6) != 0b10:
                return False
        char_bytes -= 1
    return True
