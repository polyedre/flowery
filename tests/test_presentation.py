#!/usr/bin/env python3

import unittest
from unittest.mock import patch

from flowery import Presentation


class TestPresentation(unittest.TestCase):
    def test_can_be_instantiated(self):
        presentation = Presentation("""# Slide""")

    def test_fail_if_empty(self):
        with self.assertRaises(TypeError):
            presentation = Presentation()

    def test_2_slides_if_2_titles(self):
        presentation = Presentation(
            """# Slide 1
# Slide 2"""
        )
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
        presentation = Presentation(
            """# Slide 1
# Slide 2"""
        )
        presentation.start()
        update.reset_mock()

        presentation.next()

        update.assert_called()
        presentation.stop()
