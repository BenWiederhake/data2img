#!/usr/bin/env python3

from PIL import Image


def convert(in_file, w, h, out_file):
    with open(in_file, 'rb') as in_fp:
        data = in_fp.read()
    w = int(w)
    h = int(h)
    if w * h != len(data):
        print('{}*{} = {} pixels, but in-file has {} bytes.'.format(w, h, w * h, len(data)))
        return False
    img = Image.frombytes('L', (w, h), data)
    with open(out_file, 'wb') as out_fp:
        img.save(out_fp)
    return True


def run(argv):
    if len(argv) != 5:
        print("Usage: {} <DATA-IN-FILE> <WIDTH> <HEIGHT> <IMAGE-OUT-FILE>".format(argv[0]))
        return False
    return convert(*argv[1:])


if __name__ == "__main__":
    from sys import argv
    if not run(argv):
        exit(1)
