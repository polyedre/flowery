<!--
This is an example of markdown file that can be played as a presentation with flowery.

To try it, just run:

```
python -m flowery demo_presentation.md
```
-->
# First Slide

This is a classic slide with a text content.

# Text Formatting

This is a slide with formatting. Text can be **bold** or *italic*.

# Quote

Some text can be quoted:

> This is a citation

# Code bloc

This is a slide with a code `inline` and syntactically highlighted code bloc:

```py
def iter_first_last(values: Iterable[T]) -> Iterable[Tuple[bool, bool, T]]:
    """Iterate and generate a tuple with a flag for first and last value."""
    iter_values = iter(values)
    try:
        previous_value = next(iter_values)
    except StopIteration:
        return
    first = True
    for value in iter_values:
        yield first, False, previous_value
        first = False
        previous_value = value
    yield first, True, previous_value
```

# Sections

This slide has 2 sections:

Up

---

Down

# List

This is a slide that contains lists.

1. First item
1. Second item
    1. Subitem
  
- Apple
- Banana
- Pineapple

# Colors

[bold][blue]A [magenta]colored[/magenta] text[/blue][/bold].

# Tables

This is a table.

| Fruit | Price |
|---|---|
| Apple | $1 |

# Links

This is a [link](www.duckduckgo.com). Links are just colored in cyan.
