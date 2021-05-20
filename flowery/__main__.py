#!/usr/bin/env python3

import os
import sys
import time

from flowery import Presentation


def show_help():
    print(f"Usage: {sys.argv[0]} FILENAME")


if __name__ == "__main__":

    if len(sys.argv) < 2:
        show_help()
        sys.exit(1)

    filename = sys.argv[1]
    try:
        with open(filename) as data_stream:
            file_content = data_stream.read()
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)

    presentation = Presentation(file_content)
    presentation.start()

    for _ in range(len(presentation)):
        time.sleep(1)
        presentation.next()

    presentation.stop()
