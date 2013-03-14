#!/usr/bin/env python
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
from utils import get_file_content, wrap_line


LANGUAGE = 'javascript'
FILE_EXTENSION = 'js'
CODE_WRAP_MARKERS = [
    # 1st element used in regex to identify wrappable lines
    #     Remember to comment characters that have special meanings in regex.
    # 2nd element (indent_marker) used in regex to identify index of indention
    # 3rd element (indent_suffix) placed between whitespace indentation and
    #     wrapped line
    # 4th element (indent_offset) is number of chars to add to indentation
    #     index before content
    ('\/\*', '/*', ' * ', 0),
    ('this.\w+ = function', '', '', 2)
]


def make_filename(name):
    """Manipulate a string to form the name without file extension for each
    module in the package.

    'name' will usually be one word, like 'channels'.  Whether singular
    or plural should not be assumed

    """
    name = re.sub('s$', '', name)
    return name.lower()


def make_class_name(name):
    """Manipulate a string to form the name without file extension for each
    module in the package.

    'name' will usually be one word, like 'channels'.  Whether singular
    or plural should not be assumed

    """
    name = re.sub('s$', '', name)
    name = name[0].upper() + name[1:]
    name = re.sub('/', '::', name)
    return name


def make_method_name(name, class_name):
    """Manipulate a string to form the name without file extension for each
    module in the package.

    'name' will usually be one or more words in camelCase, like
    'muteChannel'.  Whether singular or plural should not be assumed.

    """
    return name


def make_param_string(method):
    """Make the string containing the parameter definition for each method
    in a class

    """
    t_attr = get_file_content('%s/templates/method_params_attr.proto'
                              % method.lang)
    if method.param_obj is None:
        return ''

    for p in method.param_obj:
        if p['name'] == "%sId" % (method.file_name):
            continue

        param_name = "%s%s" % (p['name'],
                     p['dataType'][0].upper() + p['dataType'][1:])

        if 'allowMultiple' in p and p['allowMultiple']:
            param_name = param_name + "Array"

        attr = re.sub('\{ATTR_NAME\}', param_name, t_attr)
        attr = re.sub('\{ATTR_ORIG_NAME\}', p['name'], attr)
        method.param_lines.append(attr)

        method.method_params.append(param_name)

    return ', '.join(method.method_params)


def make_method_comment(class_desc, method_desc):
    """Use the class and method descriptions in the Swagger resource files
    to create a comment for the method.

    """
    method_comments = []
    if class_desc:
        method_comments.append(class_desc)
    if method_desc and method_desc != class_desc:
        method_comments.append(method_desc)
    return '\t\t/* %s */' % ('; '.join(method_comments))


def make_api_call_params(method):
    """Format the parameters to the call() method in asterisk_rest_api, the
    util module which handles HTTP requests to Asterisk."""
    params = ["'path': '%s'" % (method.path),
             "'http_method': '%s'" % (method.http_method)]
    if method.method_params:
        params.append("'parameters': params")
    if method.required_id:
        params.append("'object_id': this.object_id")

    return '{\n\t\t\t' + ',\n\t\t\t'.join(params) + '\n\t\t}'


def wrap(codestring):
    """Wrap code created by AsteriskPy to a certain width.

    Define lines to wrap and string to glean indent index from
    in the CODE_WRAP_MARKERS list at the top of this file.

    For many languages, this function may not need to be changed much
    at all.

    In perl, we want to indent at exactly the index of the code marker we use.
    We must append '# ' to the indention, since perl doesn't have multi-line
    comments. Use tabs. Wrap to 70 characters since use of tabs may increase
    visible line length.

    """
    width = 70
    code_lines = codestring.split('\n')
    wrapped_code_lines = []
    for line in code_lines:
        if len(line) < width:
            wrapped_code_lines.append(line)
            continue

        matched = None
        for each in CODE_WRAP_MARKERS:
            match = re.search('^\s+(%s)' % (each[0]), line)
            if match is not None:
                matched = True
                new_line = wrap_line(line, width, each[1], indent_char='\t',
                                     indent_suffix=each[2],
                                     indent_offset=each[3])
                wrapped_code_lines.append(new_line)

        if matched is None:
            wrapped_code_lines.append(line)

    return '\n'.join(wrapped_code_lines)
