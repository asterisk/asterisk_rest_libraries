"""
 Copyright (C) 2013 Digium, Inc.

 Erin Spiceland <espiceland@digium.com>

 See http://www.asterisk.org for more information about
 the Asterisk project. Please do not directly contact
 any of the maintainers of this project for assistance;
 the project provides a web site, mailing lists and IRC
 channels for your use.

 This program is free software, distributed under the terms
 detailed in the the LICENSE file at the top of the source tree.

"""


import re


"""List of tuples defining lines to wrap.  The first element is a string to
match to idenfity the line. The second is a string at whose index to indent
the next line"""
replacements = [
    ('def', '('),
    ('self._api.call', '('),
    ('"""', '"""'),
]


def wrap(codestring, width):
    """Wrap code created by AsteriskPy to a certain width.

    Currently only wraps the following lines:

    def xxxxxxxxx(args):
    self._api.call(args)

    Currently only indents to 1 character greater than first
    occurance of open parenthesis: (

    """
    code_lines = codestring.split('\n')
    wrapped_code_lines = []
    for line in code_lines:
        if len(line) < width:
            wrapped_code_lines.append(line)
            continue

        matched = None
        for each in replacements:
            match = re.search('^\s+(%s)' % (each[0]), line)
            if match is not None:
                matched = True
                new_line = wrap_line(line, width, each[1])
                wrapped_code_lines.append(new_line)

        if matched is None:
            wrapped_code_lines.append(line)

    return '\n'.join(wrapped_code_lines)


def wrap_line(text, width, indent_marker):
    """
    A word-wrap function that preserves existing line breaks
    and most spaces in the text. Expects that existing line
    breaks are posix newlines (\n).

    Loop through iterable created by splitting the text by a space.
    Construct lines with words and spaces until $width is reached.
    Start a new line with a newline when $width is reached.

    """
    paren_index = text.find(indent_marker)
    indent = ' ' * (paren_index+1)

    def make_delimiter(line, word, width):
        """Determine whether we will add this word to the current line
        or begin a new line.

        """
        isbreak = len(line)-line.rfind('\n')-1 + \
            len(word.split('\n', 1)[0]) >= width
        if isbreak:
            return '\n%s' % (indent)
        else:
            return ' '

    return reduce(lambda line, word, width=width: '%s%s%s' %
                  (line, make_delimiter(line, word, width),
                  word), text.split(' '))
