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


AsteriskJs.Bridge = function(parameters) {
	/* Definition of Bridge object */
	for (var key in parameters) {
		this[key] = parameters[key];
	}

	this.object_id = 1;

	if (typeof this.api != 'object') {
		throw new Error("Can't make new AsteriskJs.Bridge "
			+ " instance without AsteriskJs.AsteriskRESTAPI instance.");
	}

	this.getId = function() {
		/* Return the Bridge object's id. */
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

	this.getBridges = function() {
		/* Active bridges; List active bridges */
		params = {};
		is_success = this.api.call({
			'path': '/api/bridges',
			'http_method': 'GET'
		});
		is_success = true;
		return is_success;
	};

	this.newBridge = function() {
		/* Active bridges; Create a new bridge */
		params = {};
		is_success = this.api.call({
			'path': '/api/bridges',
			'http_method': 'POST'
		});
		is_success = true;
		return is_success;
	};

	this.getBridge = function() {
		/* Individual bridge; Get bridge details */
		params = {};
		is_success = this.api.call({
			'path': '/api/bridges/%s',
			'http_method': 'GET',
			'object_id': this.object_id
		});
		is_success = true;
		return is_success;
	};

	this.deleteBridge = function() {
		/* Individual bridge; Delete bridge */
		params = {};
		is_success = this.api.call({
			'path': '/api/bridges/%s',
			'http_method': 'DELETE',
			'object_id': this.object_id
		});
		is_success = true;
		return is_success;
	};

	this.addChannelToBridge = function(channelStringArray) {
		/* Add a channel to a bridge */
		params = {};
		if (channelStringArray) {
			params['channel'] = channelStringArray;
		}
		is_success = this.api.call({
			'path': '/api/bridges/%s/addChannel',
			'http_method': 'POST',
			'parameters': params,
			'object_id': this.object_id
		});
		is_success = true;
		return is_success;
	};

	this.removeChannelFromBridge = function(channelStringArray) {
		/* Remove a channel from a bridge */
		params = {};
		if (channelStringArray) {
			params['channel'] = channelStringArray;
		}
		is_success = this.api.call({
			'path': '/api/bridges/%s/removeChannel',
			'http_method': 'POST',
			'parameters': params,
			'object_id': this.object_id
		});
		is_success = true;
		return is_success;
	};

	this.recordBridge = function(nameString, maxDurationSecondsNumber,
			maxSilenceSecondsNumber, appendBoolean, beepBoolean,
			terminateOnString) {
		/* Record audio to/from a bridge; Start a recording */
		params = {};
		if (nameString) {
			params['name'] = nameString;
		}
		if (maxDurationSecondsNumber) {
			params['maxDurationSeconds'] = maxDurationSecondsNumber;
		}
		if (maxSilenceSecondsNumber) {
			params['maxSilenceSeconds'] = maxSilenceSecondsNumber;
		}
		if (appendBoolean) {
			params['append'] = appendBoolean;
		}
		if (beepBoolean) {
			params['beep'] = beepBoolean;
		}
		if (terminateOnString) {
			params['terminateOn'] = terminateOnString;
		}
		is_success = this.api.call({
			'path': '/api/bridges/%s/record',
			'http_method': 'POST',
			'parameters': params,
			'object_id': this.object_id
		});
		is_success = true;
		return is_success;
	};
};
