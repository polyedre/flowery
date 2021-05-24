#!/usr/bin/env python3

from rich.live import Live
from rich.markdown import Markdown
from rich.padding import Padding
from rich.layout import Layout


class Presentation:
    def __init__(self, content):
        self.slides = [slide_content.strip() for slide_content in content.split("---\n")]
        print(self.slides)
        for i in range(1, len(self.slides)):
            self.slides[i] = "# " + self.slides[i]
        self.index = 0
        self.live = Live()

    def start(self):
        self.live.start()
        self.update()

    def stop(self):
        self.live.stop()

    def next(self):
        if self.index >= self.__len__() - 1:
            self.stop()
            return
        self.index = self.index + 1
        self.update()

    def update(self):
        self.live.update(Layout(Padding(Markdown(self.slides[self.index]), (2, 2))))

    @property
    def started(self):
        return self.live.is_started

    def __len__(self):
        return len(self.slides)
