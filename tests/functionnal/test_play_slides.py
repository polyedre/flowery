#!/usr/bin/env python3

from flowery import Flowery
import unittest

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
    def test_play_3_slides(self):
        presentation = Flowery(EXAMPLE_PRESENTATION)
        self.assertEqual(len(presentation), 3)

        for _ in range(len(presentation)):
            presentation.next()


if __name__ == "__main__":
    unittest.main()
