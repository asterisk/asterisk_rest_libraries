/*****************************************************************************
* Copyright (C) 2013 Digium, Inc.
* All Rights Reserved.
******************************************************************************
* @Package: AsteriskRESTAPI
* @Authors: Erin Spiceland <espiceland@digium.com>
*
* See http://www.asterisk.org for more information about
* the Asterisk project. Please do not directly contact
* any of the maintainers of this project for assistance;
* the project provides a web site, mailing lists and IRC
* channels for your use.
*
* This program is free software, distributed under the terms
* detailed in the the LICENSE file at the top of the source tree.
*
*****************************************************************************/
AsteriskJs.AsteriskRESTAPI = function(parameters) {
	/* Handle HTTP requests to Asterisk */
	var this_ = this;
	for (var key in parameters) {
		this[key] = parameters[key];
	}

	if (!this.stasis_base) {
		throw new Error("Can't call Asterisk REST API without stasis_base.");
	}

	if (!this.stasis_base.match(/https*:\/\/.+\/stasis\/*/i)) {
		throw new Error("stasis_base value is invalid: " + this.stasis_base);
	}

	this.call = function(params) {
		/*
		Call an Asterisk API method, call responseHandler with request info
		"data" including URI and parameters.

		responseHandler(response, data);

		success indicates the success or failure of the Asterisk API call.
		response is a dictionary constructed by json.dumps(json_string)
		error is a message.

		If the API call is successful but Asterisk returns invalid JSON, error
		will be "Invalid JSON." and response will be the unchanged content
		of the response.
		*/

		if (!this.hasOwnProperty('responseHandler')) {
			this.responseHandler = function(response, data) {
				console.log('default responseHandler');
				console.log(response);
			};
		}

		if (!params) {
			throw new Error('No params.');
		}

		if (!params.http_method) {
			throw new Error('No HTTP method.');
		}


		if (params.object_id) {
			params.path = params.path.replace(/\%s/ig, params.object_id);
		}

		var uri = this.stasis_base + params.path;
		var response;
		var xhr = new XMLHttpRequest();

		/* Params go in the URI for GET, DELETE, same format for
		 * POST and PUT, but they must be sent separately after the
		 * request is opened. */
		var paramString = make_param_string(params.parameters);
		if (['GET', 'DELETE'].indexOf(params.http_method) > -1) {
			uri += paramString;
			paramString = null;
		}

		xhr.open(params.http_method, uri);
		if (['POST', 'PUT'].indexOf(params.http_method) > -1) {
			try {
				xhr.setRequestHeader(
					'Content-type',
					'application/x-www-form-urlencoded'
				);
			} catch (e) {
				console.log("Can't set content-type header in readyState "
					+ xhr.readyState + ". " + e.message);
			}
			xhr.setRequestHeader('Content-length', params.length);
			xhr.setRequestHeader('Connection', 'close');
		} else if (['GET', 'DELETE'].indexOf(params.http_method) == -1) {
			throw new Error('Illegal HTTP request method '
				+ params.http_method);
		}

		try {
			xhr.send(paramString);
		} catch (e) {
			console.log("Can't call xhr.send. " + e.message);
		}
		xhr.onreadystatechange = function() {
			if (this.readyState !== 4) { return; }
			if (this.status === 0) { return; }
			/*console.log('readyState is ' + this.readyState + " and status is "
				+ this.status + " and text is " + this.statusText);*/
			if ([200, 204, 205, 302, 404, 418].indexOf(this.status) > -1) {
				this_.responseHandler(this, {
					'uri' : uri,
					'params' : params.parameters
				});
			} else {
				console.log('unexpected response ' + this.status);
			}
		};
	};

	var make_param_string = function(params) {
		/* Turn key/value and key/list pairs into an HTTP URL parameter string.
		var1=value1&var2=value2,value3,value4 */
		var strings = [];
		for (var name in params) { if (params.hasOwnProperty(name)) {
			/* Skip objects -- We won't know how to name these. */
			if (typeof params[name] == 'array') {
				strings.push([name, params[name].join(',')].join('='));
			} else if (typeof params[name] != 'object'
					&& typeof params[name] != 'function') {
				strings.push([name, params[name]].join('='));
			}
		}}
		if (strings.length > 0) {
			return '?' + strings.join('&');
		} else {
			return '';
		}
	};
};
