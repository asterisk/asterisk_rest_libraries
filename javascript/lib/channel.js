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


AsteriskJs.Channel = function(parameters) {
	/* Definition of Channel object */
	for (var key in parameters) {
		this[key] = parameters[key];
	}

	this.object_id = 1;

	if (typeof this.api != 'object') {
		throw new Error("Can't make new AsteriskJs.Channel "
			+ " instance without AsteriskJs.AsteriskRESTAPI instance.");
	}

	this.getId = function() {
		/* Return the Channel object's id. */
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

	this.getChannels = function() {
		/* Active channels; List active channels */
		params = {};
		is_success = this.api.call({
			'path': '/api/channels',
			'http_method': 'GET'
		});
		is_success = true;
		return is_success;
	};

	this.originate = function(endpointString, extensionString,
			contextString) {
		/* Active channels; Create a new channel (originate) */
		params = {};
		if (endpointString) {
			params['endpoint'] = endpointString;
		}
		if (extensionString) {
			params['extension'] = extensionString;
		}
		if (contextString) {
			params['context'] = contextString;
		}
		is_success = this.api.call({
			'path': '/api/channels',
			'http_method': 'POST',
			'parameters': params
		});
		is_success = true;
		return is_success;
	};

	this.getChannel = function() {
		/* Active channel; Channel details */
		params = {};
		is_success = this.api.call({
			'path': '/api/channels/%s',
			'http_method': 'GET',
			'object_id': this.object_id
		});
		is_success = true;
		return is_success;
	};

	this.deleteChannel = function() {
		/* Active channel; Delete (i.e. hangup) a channel */
		params = {};
		is_success = this.api.call({
			'path': '/api/channels/%s',
			'http_method': 'DELETE',
			'object_id': this.object_id
		});
		is_success = true;
		return is_success;
	};

	this.dial = function(endpointString, extensionString, contextString)
			{
		/* Create a new channel (originate) and bridge to this channel */
		params = {};
		if (endpointString) {
			params['endpoint'] = endpointString;
		}
		if (extensionString) {
			params['extension'] = extensionString;
		}
		if (contextString) {
			params['context'] = contextString;
		}
		is_success = this.api.call({
			'path': '/api/channels/%s/dial',
			'http_method': 'POST',
			'parameters': params,
			'object_id': this.object_id
		});
		is_success = true;
		return is_success;
	};

	this.continueInDialplan = function() {
		/* Exit application; continue execution in the dialplan */
		params = {};
		is_success = this.api.call({
			'path': '/api/channels/%s/continue',
			'http_method': 'POST',
			'object_id': this.object_id
		});
		is_success = true;
		return is_success;
	};

	this.rejectChannel = function() {
		/* Reject a channel */
		params = {};
		is_success = this.api.call({
			'path': '/api/channels/%s/reject',
			'http_method': 'POST',
			'object_id': this.object_id
		});
		is_success = true;
		return is_success;
	};

	this.answerChannel = function() {
		/* Answer a channel */
		params = {};
		is_success = this.api.call({
			'path': '/api/channels/%s/answer',
			'http_method': 'POST',
			'object_id': this.object_id
		});
		is_success = true;
		return is_success;
	};

	this.muteChannel = function(directionString) {
		/* Mute a channel */
		params = {};
		if (directionString) {
			params['direction'] = directionString;
		}
		is_success = this.api.call({
			'path': '/api/channels/%s/mute',
			'http_method': 'POST',
			'parameters': params,
			'object_id': this.object_id
		});
		is_success = true;
		return is_success;
	};

	this.unmuteChannel = function(directionString) {
		/* Unmute a channel */
		params = {};
		if (directionString) {
			params['direction'] = directionString;
		}
		is_success = this.api.call({
			'path': '/api/channels/%s/unmute',
			'http_method': 'POST',
			'parameters': params,
			'object_id': this.object_id
		});
		is_success = true;
		return is_success;
	};

	this.recordChannel = function(nameString, maxDurationSecondsNumber,
			maxSilenceSecondsNumber, appendBoolean, beepBoolean,
			terminateOnString) {
		/* Record audio to/from a channel; Start a recording */
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
			'path': '/api/channels/%s/record',
			'http_method': 'POST',
			'parameters': params,
			'object_id': this.object_id
		});
		is_success = true;
		return is_success;
	};
};
