#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Copyright (C) 2013 Digium, Inc.
# All Rights Reserved.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# @Package: AsteriskPl
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

package AsteriskPl;

use LWP::Simple;
use JSON;
use AsteriskPl::AsteriskRESTAPI;
use AsteriskPl::Asterisk;
use AsteriskPl::Bridge;
use AsteriskPl::Channel;
use AsteriskPl::Endpoint;
use AsteriskPl::Recording;

sub new {
	# Initiate new AsteriskPy instance.
	# Takes optional string host, string port, boolean https.
	# Raise requests.exceptions

	my ($class, %self) = @_;

	$self{'api'} = AsteriskPl::AsteriskRESTAPI->new(
		'api_url' => $self{'api_url'}
	);
	$self{'asterisk'} = AsteriskPl::Asterisk->new('api' => $self{'api'});
	bless \%self, $class;
	return \%self;
}

sub get_asterisk_info {
	# Return hash of Asterisk system information
	my $self = shift;
	return $self->{'asterisk'}->get_asterisk_info();
}

sub get_endpoints {
	my $self = shift;
	# Return a list of all Endpoints from Asterisk.
	my $response = $self->{'api'}->call({
		'path' => '/api/endpoints',
		'http_method' => 'GET'
	});
	# Temporary until method is implemented
	$result_list = [
		AsteriskPl::Endpoint->new('api' => $self->{'api'}),
		AsteriskPl::Endpoint->new('api' => $self->{'api'}),
	];
	#$result_list = [];
	#foreach my $x (@{$response->{'endpoints'}}) {
	#	$x->{'api'} = $self->{'api'};
	#	push @$result_list = AsteriskPl::Endpoint->new('api' => $self{'api'}),
	#}
	return $result_list;
}

sub get_channels {
	my $self = shift;
	# Return a list of all Channels from Asterisk.
	my $response = $self->{'api'}->call({
		'path' => '/api/channels',
		'http_method' => 'GET'
	});
	# Temporary until method is implemented
	$result_list = [
		AsteriskPl::Channel->new('api' => $self->{'api'}),
		AsteriskPl::Channel->new('api' => $self->{'api'}),
	];
	#$result_list = [];
	#foreach my $x (@{$response->{'channels'}}) {
	#	$x->{'api'} = $self->{'api'};
	#	push @$result_list = AsteriskPl::Channel->new('api' => $self->{'api'}),
	#}
	return $result_list;
}

sub get_bridges {
	my $self = shift;
	# Return a list of all Bridges from Asterisk.
	my $response = $self->{'api'}->call({
		'path' => '/api/bridges',
		'http_method' => 'GET'
	});
	# Temporary until method is implemented
	$result_list = [
		AsteriskPl::Bridge->new('api' => $self->{'api'}),
		AsteriskPl::Bridge->new('api' => $self->{'api'}),
	];
	#$result_list = [];
	#foreach my $x (@{$response->{'bridges'}}) {
	#	$x->{'api'} = $self->{'api'};
	#	push @$result_list = AsteriskPl::Bridge->new('api' => $self->{'api'}),
	#}
	return $result_list;
}

sub get_recordings {
	my $self = shift;
	# Return a list of all Recordings from Asterisk.
	my $response = $self->{'api'}->call({
		'path' => '/api/recordings',
		'http_method' => 'GET'
	});
	# Temporary until method is implemented
	$result_list = [
		AsteriskPl::Recording->new('api' => $self->{'api'}),
		AsteriskPl::Recording->new('api' => $self->{'api'}),
	];
	#$result_list = [];
	#foreach my $x (@{$response->{'recordings'}}) {
	#	$x->{'api'} = $self->{'api'};
	#	push @$result_list =
	#		AsteriskPl::Recording->new('api' => $self->{'api'}),
	#}
	return $result_list;
}

sub get_endpoint {
	# Return Endpoint specified by object_id.
	my $self = shift;
	my $object_id = shift;
	my $response = $self->{'api'}->call({
		'path' => '/api/endpoints',
		'http_method' => 'GET',
		'object_id' => $object_id,
	});

	# Temporary until method is implemented
	#$response->{'endpoint'}->{'api'} = $self->{'api'};
	#$result = AsteriskPl::Endpoint->new($response->{'endpoint'});
	$result = AsteriskPl::Endpoint->new('api' => $self->{'api'});
	return $result;
}

sub get_channel {
	# Return Channel specified by object_id.
	my $self = shift;
	my $object_id = shift;
	my $response = $self->{'api'}->call({
		'path' => '/api/channels',
		'http_method' => 'GET',
		'object_id' => $object_id,
	});

	# Temporary until method is implemented
	#$response->{'channel'}->{'api'} = $self->{'api'};
	#$result = AsteriskPl::Channel->new($response->{'channel'});
	$result = AsteriskPl::Channel->new('api' => $self->{'api'});
	return $result;
}

sub get_bridge {
	# Return Bridge specified by object_id.
	my $self = shift;
	my $object_id = shift;
	my $response = $self->{'api'}->call({
		'path' => '/api/bridges',
		'http_method' => 'GET',
		'object_id' => $object_id,
	});

	# Temporary until method is implemented
	#$response->{'bridge'}->{'api'} = $self->{'api'};
	#$result = AsteriskPl::Bridge->new($response->{'bridge'});
	$result = AsteriskPl::Bridge->new('api' => $self->{'api'});
	return $result;
}

sub get_recording {
	# Return Recording specified by object_id.
	my $self = shift;
	my $object_id = shift;
	my $response = $self->{'api'}->call({
		'path' => '/api/recordings',
		'http_method' => 'GET',
		'object_id' => $object_id,
	});

	# Temporary until method is implemented
	#$response->{'recording'}->{'api'} = $self->{'api'};
	#$result = AsteriskPl::Recording->new($response->{'recording'});
	$result = AsteriskPl::Recording->new('api' => $self->{'api'});
	return $result;
}

sub create_channel {
	# In Asterisk, originate a channel. Return the Channel.
	my $self = shift;
	my $params = shift;
	my $result = $self->{'api'}->call({
		'path' => '/api/channels',
		'http_method' => 'POST',
		'parameters' => $params,
	});
	# Temporary until method is implemented
	$result = AsteriskPl::Channel->new('api' => $self->{'api'});
	return $result
}

sub create_bridge() {
	#In Asterisk, bridge two or more channels. Return the Bridge.
	my $self = shift;
	my $params = shift;
	my $result = $self->{'api'}->call({
		'path' => '/api/bridges',
		'http_method' => 'POST',
		'parameters' => $params,
	});
	# Temporary until method is implemented
	$result = AsteriskPl::Bridge->new('api' => $self->{'api'});
	return $result
}

sub add_event_handler() {
	# Add a general event handler for Stasis events.
	# For object-specific events, use the object's add_event_handler instead.
	my $self = shift;
	my $event_name = shift;
	my $handler = shift;
	return 1
}

sub remove_event_handler() {
	# Add a general event handler for Stasis events.
	# For object-specific events, use the object's add_event_handler instead.
	my $self = shift;
	my $event_name = shift;
	my $handler = shift;
	return 1
}

1;
