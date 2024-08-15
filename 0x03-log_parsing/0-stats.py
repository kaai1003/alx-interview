#!/usr/bin/python3
"""log parsing module"""
import re
import sys
from typing import Dict


def display_statics(file_size: int, status: Dict) -> None:
    """print log statistics"""
    print("File size: {}".format(file_size))
    for code in status:
        if status[code] > 0:
            print("{}: {}".format(code, status[code]))


if __name__ == "__main__":
    line_pattern = re.compile(
        r'(?P<ip>\S+) - \[(?P<date>[^\]]+)\] "GET /projects/260 HTTP/1.1" (?P<status>\d{3}) (?P<size>\d+)')  # nopep8
    status = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }
    line_count = 0
    file_size = 0
    try:
        for line in sys.stdin:
            line = line.strip()
            input_format = line_pattern.fullmatch(line)
            if (input_format):
                line_count += 1
                file_size += int(input_format.group('size'))
                status_code = int(input_format.group('status'))
                if status_code in status:
                    status[status_code] += 1
            if line_count == 10:
                display_statics(file_size, status)
                line_count = 0
    finally:
        display_statics(file_size, status)
