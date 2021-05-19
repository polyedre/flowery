#!/usr/bin/env python3

import unittest

from rich.console import Console
from flowery import Presentation

EXAMPLE_PRESENTATION = """# Slide 1

This is the content of the slide

# Slide 2

```sh
ls *
```

# Slide 3

1. First item
2. Second item
"""


class TestPlaySlides(unittest.TestCase):
    def test_first_slide(self):
        presentation = Presentation(EXAMPLE_PRESENTATION)
        with presentation.live.console.capture() as capture:
            presentation.start()
            presentation.stop()
        self.assertIn("Slide 1", capture.get())

    def test_second_slide(self):
        presentation = Presentation(EXAMPLE_PRESENTATION)
        with presentation.live.console.capture() as capture:
            presentation.start()
            presentation.next()
            presentation.stop()
        self.assertIn("Slide 2", capture.get())

    def test_third_slide(self):
        presentation = Presentation(EXAMPLE_PRESENTATION)
        with presentation.live.console.capture() as capture:
            presentation.start()
            presentation.next()
            presentation.next()
            presentation.stop()
        self.assertIn("Slide 3", capture.get())


if __name__ == "__main__":
    unittest.main()
