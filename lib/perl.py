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
from utils import get_file_content


def make_filename(name):
    """Manipulate a string to form the name without file extension for each
    module in the package.

    'name' will usually be one word, like 'channels'.  Whether singular
    or plural should not be assumed

    """
    name = re.sub('s$', '', name)
    name = name[0].upper() + name[1:]
    return 'AsteriskPl/' + name


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
    name = re.sub('([A-Z]{1,1})', r'_\1', name)
    name = name.lower()
    #name = name.replace('_%s' % (class_name.lower()), '')
    return name


def make_param_string(method):
    """Make the string containing the parameter definition for each method
    in a class

    Not necessary in Perl, but we may want to form a number of $ here later.

    """
    return ''


def make_method_comment(class_desc, method_desc):
    """Use the class and method descriptions in the Swagger resource files
    to create a comment for the method.

    """
    method_comments = []
    if class_desc:
        method_comments.append(class_desc)
    if method_desc and method_desc != class_desc:
        method_comments.append(method_desc)
    return '    # %s' % ('; '.join(method_comments))


def make_api_call_params(method):
    """Format the parameters to the call() method in asterisk_rest_api, the
    util module which handles HTTP requests to Asterisk."""
    params = ["'path' => '%s'" % (method.path),
              "'http_method' => '%s'" % (method.http_method)]
    if method.method_name:
        params.append("'api_method' => '%s'" % (method.method_name))
    if method.method_params:
        params.append("'parameters' => $params")
    if method.required_id:
        params.append("'object_id' => $self->{'object_id'}")

    return '{\n\t\t' + ',\n\t\t'.join(params) + '\n\t}'
