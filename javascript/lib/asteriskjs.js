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

AsteriskJs = function(parameters) {
	/* Initiate new AsteriskJs instance.
	 * Takes optional string host, string port, boolean https. */
	if (!XMLHttpRequest) {
		throw new Error("AsteriskJs depends on XMLHttpRequest.");
	}

	this.init = function(parameters) {
		for (var key in parameters) {
			this[key] = parameters[key];
		}

		this.api = new AsteriskJs.AsteriskRESTAPI({
			'api_url': parameters.api_url,
			'responseHandler': this.responseHandler
		});
		this.asterisk = new AsteriskJs.Asterisk({'api': this.api});

		this.getAsteriskInfo
			= this.asterisk.getAsteriskInfo.bind(this.asterisk);
		return this;
	};

	this.getEndpoints = function() {
		/* Return a list of all Endpoints from Asterisk. */
		response = this.api.call({
			'path': '/api/endpoints',
			'http_method': 'GET'
		});
		/* Temporary until method is implemented */
		result_list = [
			new AsteriskJs.Endpoint({'api': this.api}),
			new AsteriskJs.Endpoint({'api': this.api})
		];
		/*result_list = [];
		for (var i = 0; i < response.endpoints.length; i++) {
			var x = response.endpoints[i];
			x.api = this.api;
			push result_list = new AsteriskJs.Endpoint({'api': this.api}),
		}*/
		return result_list;
	};

	this.getChannels = function() {
		/* Return a list of all Channels from Asterisk. */
		response = this.api.call({
			'path': '/api/channels',
			'http_method': 'GET'
		});
		/* Temporary until method is implemented */
		result_list = [
			new AsteriskJs.Channel({'api': this.api}),
			new AsteriskJs.Channel({'api': this.api})
		];
		/*result_list = [];
		for (var i = 0; i < response.channels.length; i++) {
			var x = response.channels[i];
			x.api = this.api;
			push result_list = new AsteriskJs.Channel({'api': this.api}),
		}*/
		return result_list;
	};

	this.getBridges = function() {
		/* Return a list of all Bridges from Asterisk. */
		response = this.api.call({
			'path': '/api/bridges',
			'http_method': 'GET'
		});
		/* Temporary until method is implemented */
		result_list = [
			new AsteriskJs.Bridge({'api': this.api}),
			new AsteriskJs.Bridge({'api': this.api})
		];
		/*result_list = [];
		for (var i = 0; i < response.bridges.length; i++) {
			var x = response.bridges[i];
			x.api = this.api;
			push result_list = new AsteriskJs.Bridge({'api': this.api}),
		}*/
		return result_list;
	};

	this.getRecordings = function() {
		/* Return a list of all Recordings from Asterisk. */
		response = this.api.call({
			'path': '/api/recordings',
			'http_method': 'GET'
		});
		/* Temporary until method is implemented */
		result_list = [
			new AsteriskJs.Recording({'api': this.api}),
			new AsteriskJs.Recording({'api': this.api})
		];
		/*result_list = [];
		for (var i = 0; i < response.recordings.length; i++) {
			var x = response.recordings[i];
			x.api = this.api;
			push result_list = new AsteriskJs.Recording({'api': this.api}),
		}*/
		return result_list;
	};

	this.getEndpoint = function(objectId) {
		/* Return Endpoint specified by objectId. */
		response = this.api.call({
			'path': '/api/endpoints',
			'http_method': 'GET',
			'objectId': objectId
		});

		/* Temporary until method is implemented
		response.endpoint.api = this.api;
		result = new AsteriskJs.Endpoint(response.endpoint);*/
		result = new AsteriskJs.Endpoint({'api': this.api});
		return result;
	};

	this.getChannel = function(objectId) {
		/* Return Channel specified by objectId. */
		response = this.api.call({
			'path': '/api/channels',
			'http_method': 'GET',
			'objectId': objectId
		});

		/* Temporary until method is implemented
		response.channel.api = this.api;
		result = new AsteriskJs.Channel(response.channel);*/
		result = new AsteriskJs.Channel({'api': this.api});
		return result;
	};

	this.getBridge = function(objectId) {
		/* Return Bridge specified by objectId. */
		response = this.api.call({
			'path': '/api/bridges',
			'http_method': 'GET',
			'objectId': objectId
		});

		/* Temporary until method is implemented
		response.bridge.api = this.api;
		result = new AsteriskJs.Bridge(response.bridge);*/
		result = new AsteriskJs.Bridge({'api': this.api});
		return result;
	};

	this.getRecording = function(objectId) {
		/* Return Recording specified by objectId. */
		response = this.api.call({
			'path': '/api/recordings',
			'http_method': 'GET',
			'objectId': objectId
		});

		/* Temporary until method is implemented
		response.recording.api = this.api;
		result = new AsteriskJs.Recording(response.recording);*/
		result = new AsteriskJs.Recording({'api': this.api});
		return result;
	};

	this.createChannel = function(params) {
		/* In Asterisk, originate a channel. Return the Channel. */
		result = this.api.call({
			'path': '/api/channels',
			'http_method': 'POST',
			'parameters': params
		});
		/* Temporary until method is implemented
		result = new AsteriskJs.Channel(response.channel); */
		result = new AsteriskJs.Channel({'api': this.api});
		return result;
	};

	this.createBridge = function(params) {
		/* In Asterisk, bridge two or more channels. Return the Bridge. */
		result = this.api.call({
			'path': '/api/bridges',
			'http_method': 'POST',
			'parameters': params
		});
		/* Temporary until method is implemented
		result = new AsteriskJs.Bridge(response.bridge); */
		result = new AsteriskJs.Bridge({'api': this.api});
		return result;
	};

	this.addEventHandler = function(eventName, handler) {
		/* Add a general event handler for Stasis events.
		 * For object-specific events, use the object's
		 * addEventHandler instead. */
		return true;
	};

	this.removeEventHandler = function(eventName, handler) {
		/* Remove a general event handler for Stasis events.
		 * For object-specific events, use the object's
		 * removeEventHandler instead. */
		return true;
	};
};
