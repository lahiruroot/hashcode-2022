#!/usr/bin/env python3

import numpy as np

def process_data(file_path):
    fh = open(file_path)

    fh.close()

def write_data(data, file_path="out.txt"):
    oh = open(file_path, 'w')
    oh.write(data)
    oh.close()

if __name__ == '__main__':
    process_data("in.txt")
