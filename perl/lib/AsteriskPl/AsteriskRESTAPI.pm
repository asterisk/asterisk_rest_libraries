#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Copyright (C) 2013 Digium, Inc.
# All Rights Reserved.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# @Package: AsteriskPl::AsteriskRESTAPI
# @Authors: Erin Spiceland <espiceland@digium.com>
#
# See http://www.asterisk.org for more information about
# the Asterisk project. Please do not directly contact
# any of the maintainers of this project for assistance;
# the project provides a web site, mailing lists and IRC
# channels for your use.
#
# This program is free software, distributed under the terms
# detailed in the the LICENSE file at the top of the source tree.
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

use LWP::UserAgent;
use JSON;

package AsteriskPl::AsteriskRESTAPI;

sub new {
	# Handle HTTP requests to Atserisk
	my ($class, %self) = @_;
	die ("Can't call Asterisk REST API without stasis_base.")
		if !$self{'stasis_base'};
	if ($self{'stasis_base'} !~ /https*:\/\/.+\/stasis\/*/i) {
		die sprintf("stasis_base value is invalid: %s\n", $self{'stasis_base'});
	}
	$self{'ua'} = LWP::UserAgent->new();
	bless \%self, $class;
	return \%self;
}

sub call {
	# Call an Asterisk API method, return a hash of the following structure:
	#
	# {
	#	'success' : 1, # or False
	#	'response' : jsonObject, # or None
	#	'error' : null, # or string
	# }
	#
	# success indicates the success or failure of the Asterisk API call.
	# response is a dictionary constructed by json.dumps(json_string)
	# error is a message.
	#
	# If the API call is successful but Asterisk returns invalid JSON, error
	# will be "Invalid JSON." and response will be the unchanged content
	# of the response.

	my $self = shift;
	my $params = shift;
	my $result = {
		'success' => 0,
		'response' => NULL,
		'error' => NULL,
	};

	die ("Can't call Asterisk REST API without HTTP method.")
		if !$params->{'http_method'};
	die ("Can't call Asterisk REST API without resource path.")
		if !$params->{'http_method'};


	if ($params->{'object_id'}) {
		$params->{'path'} =~ s/\%s/$params->{'object_id'}/ig;
	}
	my $uri = $self->{'stasis_base'} . $params->{'path'};
	my $response;
	print "uri is $uri\n";
	if ($params->{'http_method'} eq 'GET') {
		my $paramString = make_param_string($params->{'parameters'});
		$uri = sprintf("$uri%s", make_param_string($params->{'parameters'}));
		$response = $self->{'ua'}->get($uri);
	} elsif ($params->{'http_method'} eq 'POST') {
		$response = $self->{'ua'}->post($uri, $params->{'parameters'});
	} elsif ($params->{'http_method'} eq 'DELETE') {
		my $paramString = make_param_string($params->{'parameters'});
		$uri = sprintf("$uri%s", make_param_string($params->{'parameters'}));
		$response = $self->{'ua'}->delete($uri);
	} elsif ($params->{'http_method'} eq 'PUT') {
		$response = $self->{'ua'}->put($uri, $params->{'parameters'});
	}

	#print "response is ", $response->status_line, "\n";
	if ($response->content =~ /connection refused/i) {
		print "Can't contact server.\n";
		return $result;
	}

	if (!($response->code eq '418' or $response->code eq '302')) {
		print "Can't contact server.\n";
		$result->{'error'} = $response->status_line;
		$result->{'success'} = 0;
		return $result;
	}

	if ($response->content) {
		if (eval { JSON::XS::decode_json($response->content); 1; } ) {
			$result->{'response'} = JSON::XS::decode_json($response->content);
			$result->{'success'} = 1;
		} else {
			print "\tINVALID JSON\n";
			$result->{'error'} = "INVALID JSON";
			$result->{'success'} = 0;
			print $response->content, "\n";
		}
	}

	return $result;
}

sub make_param_string($) {
	# Turn key/value and key/list pairs into an HTTP URL parameter string.
	# var1=value1&var2=value2,value3,value4
	my $params = shift;
	my $strings = [];
	foreach my $name (keys %$params) {
		# Skip ref HASH -- We won't know how to name these.
		if (ref $params->{$name} eq 'ARRAY') {
			push @$strings, join('=', $name, join(',', @{$params->{$name}}));
		} elsif (ref $params->{$name} eq 'SCALAR') {
			push @$strings, join('=', $name, $params->{$name});
		}
	}
	if (@$strings) {
		return '?' . join('&', @$strings);
	} else {
		return '';
	}
}

1;
