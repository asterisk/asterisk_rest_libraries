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


class APIClassMethod():
    """Make an APIMethod out of operations in the Swagger description .json

    """
    def __init__(self, param_obj):
        """Initiate APIClassMethod instance

        """
        self.param_dict_lines = ['params = {}']
        self.http_method = param_obj['http_method']
        self.path = param_obj['path']
        self.file_name = param_obj['file_name']
        self.method_params = ['self']
        self.required_id = False
        self.api_summary = ''
        self.method_summary = ''
        self.method_name = ''

        obj_id_re = re.compile('\{\w+\}')
        if obj_id_re.search(self.path):
            self.required_id = True
            self.path = re.sub(obj_id_re, '%s', self.path)

    def set_method_summary(self, summary):
        """Set the method summary"""
        self.method_summary = summary

    def set_api_summary(self, summary):
        """Set the class summary"""
        self.api_summary = summary

    def set_method_name(self, nickname):
        """Set the method name"""
        self.method_name = re.sub('([A-Z]{1,1})', r'_\1', nickname)
        self.method_name = self.method_name.lower()
        self.method_name = self.method_name.replace('_%s'
                                                    % (self.file_name), '')

    def set_parameters(self, param_obj):
        """Construct an array of required and optional method parameters
        in the format: name_type[_list][=None]
             objectId_number
             query='both'

        """
        for p in param_obj:
            if p['name'] == "%sId" % (self.file_name):
                continue

            param_name = "%s_%s" % (p['name'], p['dataType'])
            print "param_name: %s" % (param_name)

            if 'allowMultiple' in p and p['allowMultiple']:
                param_name = param_name + "_list"

            print "param_name: %s" % (param_name)
            param_name = re.sub('([A-Z]{1,1})', r'_\1', param_name)
            print "param_name: %s" % (param_name)
            param_name = param_name.lower()
            print "param_name: %s" % (param_name)
            self.param_dict_lines.append("        if %s:" % (param_name))
            self.param_dict_lines.append("            params['%s'] = %s"
                                         % (p['name'], param_name))

            if 'defaultValue' in p:
                p['defaultValue'] = "'%s'" % (p['defaultValue'])
            else:
                p['defaultValue'] = None

            param = "%s=%s" % (param_name, p['defaultValue'])

            self.method_params.append(param)

    def get_param_string(self):
        """Return the string of all method parameters for method definition"""
        return ', '.join(self.method_params)

    def construct_file_contents(self, template):
        """Construct and return the contents of the method definition"""
        template = re.sub('\{API_METHOD_NAME\}', self.method_name, template)
        template = re.sub('\{PARAMS\}', self.get_param_string(), template)
        params = ["'%s'" % (self.path),
                  "http_method='%s'" % (self.http_method)]
        if self.method_name:
            params.append("api_method='%s'" % (self.method_name))
        if self.method_params:
            params.append("parameters=params")
        if self.required_id:
            params.append("object_id=self.object_id")

        template = re.sub('\{API_CALL_PARAMS\}', ', '.join(params), template)
        method_comment = ''
        method_comment = '"""%s\n\n        %s\n\n        """' \
            % (self.api_summary, self.method_summary)
        template = re.sub('\{METHOD_COMMENTS\}', method_comment, template)
        template = re.sub('\{BUILD_API_CALL_PARAMS\}',
                          '\n'.join(self.param_dict_lines), template)

        return template


class APIClass():
    """Make a collection of APIMethods and collect other information
    necessary to write out class file.

    """
    def __init__(self, param_obj):
        """Initiate new APIClass object"""
        self.methods = []

        try:
            resource = param_obj['resourcePath']
            match = re.search('/(\w+)', resource)
            self.file_name = match.group(1)
        except KeyError:
            print "param obj has no attr resourcePath \n %s" % (param_obj)
            try:
                path = param_obj[0]['path']
                match = re.search('/api/(\w+)', path)
                self.file_name = match.group(1)
            except KeyError:
                #print "param obj has no attr [0]['path']"
                pass

        if self.file_name is None:
            raise AttributeError("No file name.")

        self.file_name = re.sub('s$', '', self.file_name)
        self.class_name = self.file_name[0].upper() + self.file_name[1:]

        for api in param_obj['apis']:
            if 'operations' not in api:
                continue

            for op in api['operations']:
                method = APIClassMethod({
                    'http_method': op['httpMethod'],
                    'file_name': self.file_name,
                    'path': api['path'],
                })
                if 'parameters' in op:
                    method.set_parameters(op['parameters'])
                if 'description' in api:
                    method.set_api_summary(api['description'])
                if 'summary' in op:
                    method.set_method_summary(op['summary'])
                if 'nickname' in op:
                    method.set_method_name(op['nickname'])

                self.methods.append(method)

    def construct_file_contents(self, template):
        """Construct and return the class definition for the file
        We can't construct methods here, because we need to move some
        methods to the Asterisk class.

        """
        template = re.sub('\{CLASS_NAME\}', self.class_name, template)
        template = re.sub('\{FILE_NAME\}', self.file_name, template)
        return template
