#!/usr/bin/python3
"""
Module for UTF-8 validation
"""


def validUTF8(data):
    """
    Method to determine if a given data set represents a valid UTF-8 encoding.
    :param data: List of integers representing bytes
    :return: True if data is a valid UTF-8 encoding, else return False
    """
    num_bytes = 0

    for num in data:
        bin_repr = format(num, '#010b')[-8:]

        if num_bytes == 0:
            if bin_repr.startswith('0'):
                continue
            elif bin_repr.startswith('110'):
                num_bytes = 1
            elif bin_repr.startswith('1110'):
                num_bytes = 2
            elif bin_repr.startswith('11110'):
                num_bytes = 3
            else:
                return False
        else:
            if not bin_repr.startswith('10'):
                return False
            num_bytes -= 1

    return num_bytes == 0
