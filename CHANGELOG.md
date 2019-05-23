# 2019.1
## New Optimised Language

* GitHub Flavored Markdown
* Python via [MagicPython]

MagicPython is supported over the core `language-python` as it provides better
highlighting.  In particular, it supports newer features and is more in-tune
with Python 3 (for example, `print` is not a keyword).  If you use Atom for
Python development, I wholeheartedly recommend MagicPython.

## Other Changes
* The versioning scheme was changed to a date-based one.
    * The switch was made because semantic versioning didn't make sense as
      there's no public API exposed by this theme.
* The current line is not highlighted anymore.
* The cursor colour is now a solid black (IDLE New default) instead of a solid
  blue.

[MagicPython]: https://www.atom.io/packages/magicpython
