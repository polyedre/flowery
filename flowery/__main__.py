#!/usr/bin/env python3

import sys
import time

from pynput import keyboard

from flowery import Presentation


def show_help():
    print(f"Usage: {sys.argv[0]} FILENAME")

def on_press(_):
    pass

def on_release(key):
    if key == keyboard.Key.space:
        presentation.next()
        return presentation.started
    if key == keyboard.Key.esc:
        # Stop listener
        return False

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

    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
