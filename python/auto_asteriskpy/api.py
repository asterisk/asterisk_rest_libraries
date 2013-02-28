"""
 Copyright (C) 2013 Digium, Inc.

 Erin Spiceland <espiceland@digium.com>

 See http://www.asterisk.org for more information about
 the Asterisk project. Please do not directly contact
 any of the maintainers of this project for assistance;
 the project provides a web site, mailing lists and IRC
 channels for your use.

 This program is free software, distributed under the terms of
 the GNU General Public License Version 2. See the LICENSE file
 at the top of the source tree.

"""
import re


class APIClassMethod():
    """Make an APIMethod out of operations in the Swagger description .json
    """
    def __init__(self, param_obj):
        self.http_method = param_obj['http_method']
        self.path = param_obj['path']
        self.file_name = param_obj['file_name']
        self.method_params = ['self']
        self.required_id = False
        self.api_summary = ''
        self.method_summary = ''
        self.param_dict_lines = ['params = {}']

        obj_id_re = re.compile('\{\w+\}')
        if obj_id_re.search(self.path):
            self.required_id = True
            subs = re.subn(obj_id_re, '%s', self.path)
            self.path = subs[0]

    def set_method_summary(self, summary):
        self.method_summary = summary

    def set_api_summary(self, summary):
        self.api_summary = summary

    def set_method_name(self, nickname):
        self.method_name = re.sub('([A-Z]{1,1})', r'_\1', nickname)
        self.method_name = self.method_name.lower()
        self.method_name = self.method_name.replace('_%s' %(self.file_name),'')

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

            if 'allowMultiple' in p and p['allowMultiple']:
                param_name = param_name + "_list"

            self.param_dict_lines.append("        if %s:" % (param_name))
            self.param_dict_lines.append("            params['%s'] = %s" \
                                         % (p['name'], param_name))

            #if 'required' in p and not p['required']:
            if 'defaultValue' in p:
                p['defaultValue'] = "'%s'" % (p['defaultValue'])
            else:
                p['defaultValue'] = None

            param = "%s=%s" % (param_name, p['defaultValue'])

            self.method_params.append(param)

    def get_param_string(self):
        return ', '.join(self.method_params)

    def construct_file_contents(self, template):
        template = re.sub('\{API_METHOD_NAME\}', self.method_name, template)
        template = re.sub('\{PARAMS\}', self.get_param_string(), template)
        params = ["'%s'" % (self.path),
                  "http_method='%s'" % (self.http_method)]
        if self.method_name:
            params.append("api_method='%s'" % (self.method_name))
        if self.method_params:
            params.append("parameters=params")
        if self.required_id:
            params.append("object_id=self.id")

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
        self.methods = []
        self.file_name = self.make_file_name(param_obj)
        self.file_name = re.sub('s$', '', self.file_name)
        self.class_name = self.file_name[0].upper() + self.file_name[1:]
        print "class name is %s" % (self.class_name)

        for api in param_obj['apis']:
            if 'operations' not in api:
                continue

            for op in api['operations']:
                method = APIClassMethod({
                    'http_method' : op['httpMethod'],
                    'file_name' : self.file_name,
                    'path' : api['path'],
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

    def construct_file_contents(self, template, method_template):
        template = re.sub('\{CLASS_NAME\}', self.class_name, template)
        template = re.sub('\{FILE_NAME\}', self.file_name, template)

        for method in self.methods:
            method_string = method.construct_file_contents(method_template)

        return template

    def make_file_name(self, param_obj):
        result = ''
        try:
            resource = param_obj['resourcePath']
            match = re.search('/(\w+)', resource)
            result = match.group(1)
        except KeyError:
            print "param obj has no attr resourcePath \n %s" % (param_obj)
            try:
                path = param_obj[0]['path']
                match = re.search('/api/(\w+)', path)
                result = match.group(1)
            except KeyError:
                print "param obj has no attr [0]['path']"
                pass

        return result
