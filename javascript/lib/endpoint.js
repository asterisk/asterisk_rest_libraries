/*****************************************************************************
* Copyright (C) 2013 Digium, Inc.
* All Rights Reserved.
******************************************************************************
* @Package: AsteriskJS
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


AsteriskJs.Endpoint = function(parameters) {
	/* Definition of Endpoint object */
	for (var key in parameters) {
		this[key] = parameters[key];
	}

	this.object_id = 1;

	if (typeof this.api != 'object') {
		throw new Error("Can't make new AsteriskJs.Endpoint "
			+ " instance without AsteriskJs.AsteriskRESTAPI instance.");
	}

	this.getId = function() {
		/* Return the Endpoint object's id. */
		return this.object_id;
	};

	this.addEventHandler = function(eventName, handler) {
		/* Add an event handler for Stasis events on this object.
		 * For general events, use AsteriskJs.Asterisk.addEventHandler
		 * instead. */
		return true;
	};

	this.removeEventHandler = function(eventName, handler) {
		/* Remove an event handler for Stasis events on this object.
		 * For general events, use AsteriskJs.Asterisk.removeEventHandler
		 * instead. */
		return true;
	};

	this.getEndpoints = function(withTypeStringArray) {
		/* Asterisk endpoints; List available endoints */
		params = {};
		if (withTypeStringArray) {
			params['withType'] = withTypeStringArray;
		}
		is_success = this.api.call({
			'path': '/endpoints',
			'http_method': 'GET',
			'parameters': params
		});
		is_success = true;
		return is_success;
	};

	this.getEndpoint = function() {
		/* Single endpoint; Details for an endpoint */
		params = {};
		is_success = this.api.call({
			'path': '/endpoints/%s',
			'http_method': 'GET',
			'object_id': this.object_id
		});
		is_success = true;
		return is_success;
	};
};
