#!/usr/bin/env python3

import unittest
from unittest.mock import patch

from flowery import Presentation

ONE_SLIDE="# Slide"
TWO_SLIDES="""# Slide 1
---
# Slide 2
"""

THREE_HEADINGS_NO_LINES="""# Slide 1
# Slide 2
# Slide 3"""

ONE_HEADING_THREE_LINES="""---
# Slide
---
Some text"""

class TestPresentation(unittest.TestCase):
    def test_can_be_instantiated(self):
        Presentation(ONE_SLIDE)

    def test_fail_if_empty(self):
        with self.assertRaises(TypeError):
            Presentation()

    def test_2_slides_if_2_titles(self):
        presentation = Presentation(TWO_SLIDES)
        self.assertEqual(len(presentation), 2)

    def test_1_slide_if_no_title(self):
        presentation = Presentation("Simple content")
        self.assertEqual(len(presentation), 1)

    @patch.object(Presentation, "update")
    def test_first_slide_shown_on_start(self, update):
        presentation = Presentation("Simple content")

        presentation.start()

        update.assert_called()
        presentation.stop()

    @patch.object(Presentation, "update")
    def test_next_slide_shown_on_next(self, update):
        presentation = Presentation(TWO_SLIDES)
        presentation.start()
        update.reset_mock()

        presentation.next()

        update.assert_called()
        presentation.stop()

    def test_break_on_thematic_lines(self):
        self.assertEqual(len(Presentation(THREE_HEADINGS_NO_LINES)), 1)
        self.assertEqual(len(Presentation(ONE_HEADING_THREE_LINES)), 3)
