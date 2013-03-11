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


package AsteriskPl::Bridge;

sub new {
	# Definition of Bridge object
	my ($class, %self) = @_;
	$self{'object_id'} = 1;
	if (ref $self{'api'} ne 'AsteriskPl::AsteriskRESTAPI') {
		die("Can't make new AsteriskPl::Asterisk instance with no "
			. "AsteriskPl::AsteriskRESTAPI instance.");
	}
	bless \%self, $class;
	return \%self;
}

sub get_id {
	# Return the Bridge object's id.
	my $self = shift;
	return $self->{'object_id'}
}

sub add_event_handler {
	# Add an event handler for Stasis events on this object.
	# For general events, use Asterisk.add_event_handler instead.
	my $self = shift;
	my $event_name = shift;
	my $handler = shift;
}

sub remove_event_handler {
	# Remove an event handler for Stasis events on this object.
	# For general events, use Asterisk.remove_event_handler instead.
	my $self = shift;
	my $event_name = shift;
	my $handler = shift;
}

sub get_bridges {
    # Active bridges; List active bridges
	my $self = shift;

	$params = {};
	$is_success = $self->{'api'}->call({
		'path' => '/api/bridges',
		'http_method' => 'GET',
		'api_method' => 'get_bridges',
		'parameters' => $params
	});
	$is_success = 1;
	return $is_success;
}

sub new_bridge {
    # Active bridges; Create a new bridge
	my $self = shift;

	$params = {};
	$is_success = $self->{'api'}->call({
		'path' => '/api/bridges',
		'http_method' => 'POST',
		'api_method' => 'new_bridge',
		'parameters' => $params
	});
	$is_success = 1;
	return $is_success;
}

sub get_bridge {
    # Individual bridge; Get bridge details
	my $self = shift;

	$params = {};
	$is_success = $self->{'api'}->call({
		'path' => '/api/bridges/%s',
		'http_method' => 'GET',
		'api_method' => 'get_bridge',
		'parameters' => $params,
		'object_id' => $self->{'object_id'}
	});
	$is_success = 1;
	return $is_success;
}

sub delete_bridge {
    # Individual bridge; Delete bridge
	my $self = shift;

	$params = {};
	$is_success = $self->{'api'}->call({
		'path' => '/api/bridges/%s',
		'http_method' => 'DELETE',
		'api_method' => 'delete_bridge',
		'parameters' => $params,
		'object_id' => $self->{'object_id'}
	});
	$is_success = 1;
	return $is_success;
}

sub add_channel_to_bridge {
    # Add a channel to a bridge
	my $self = shift;

	$params = {};
	$is_success = $self->{'api'}->call({
		'path' => '/api/bridges/%s/addChannel',
		'http_method' => 'POST',
		'api_method' => 'add_channel_to_bridge',
		'parameters' => $params,
		'object_id' => $self->{'object_id'}
	});
	$is_success = 1;
	return $is_success;
}

sub remove_channel_from_bridge {
    # Remove a channel from a bridge
	my $self = shift;

	$params = {};
	$is_success = $self->{'api'}->call({
		'path' => '/api/bridges/%s/removeChannel',
		'http_method' => 'POST',
		'api_method' => 'remove_channel_from_bridge',
		'parameters' => $params,
		'object_id' => $self->{'object_id'}
	});
	$is_success = 1;
	return $is_success;
}

sub record_bridge {
    # Record audio to/from a bridge; Start a recording
	my $self = shift;

	$params = {};
	$is_success = $self->{'api'}->call({
		'path' => '/api/bridges/%s/record',
		'http_method' => 'POST',
		'api_method' => 'record_bridge',
		'parameters' => $params,
		'object_id' => $self->{'object_id'}
	});
	$is_success = 1;
	return $is_success;
}
1;
