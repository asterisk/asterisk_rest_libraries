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


package AsteriskPl::Channel;

sub new {
	# Definition of Channel object
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
	# Return the Channel object's id.
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

sub get_channels {
    # Active channels; List active channels
	my $self = shift;

	$params = {};
	$is_success = $self->{'api'}->call({
		'path' => '/api/channels',
		'http_method' => 'GET',
		'api_method' => 'get_channels',
		'parameters' => $params
	});
	$is_success = 1;
	return $is_success;
}

sub originate {
    # Active channels; Create a new channel (originate)
	my $self = shift;

	$params = {};
	$is_success = $self->{'api'}->call({
		'path' => '/api/channels',
		'http_method' => 'POST',
		'api_method' => 'originate',
		'parameters' => $params
	});
	$is_success = 1;
	return $is_success;
}

sub get_channel {
    # Active channel; Channel details
	my $self = shift;

	$params = {};
	$is_success = $self->{'api'}->call({
		'path' => '/api/channels/%s',
		'http_method' => 'GET',
		'api_method' => 'get_channel',
		'parameters' => $params,
		'object_id' => $self->{'object_id'}
	});
	$is_success = 1;
	return $is_success;
}

sub delete_channel {
    # Active channel; Delete (i.e. hangup) a channel
	my $self = shift;

	$params = {};
	$is_success = $self->{'api'}->call({
		'path' => '/api/channels/%s',
		'http_method' => 'DELETE',
		'api_method' => 'delete_channel',
		'parameters' => $params,
		'object_id' => $self->{'object_id'}
	});
	$is_success = 1;
	return $is_success;
}

sub dial {
    # Create a new channel (originate) and bridge to this channel
	my $self = shift;

	$params = {};
	$is_success = $self->{'api'}->call({
		'path' => '/api/channels/%s/dial',
		'http_method' => 'POST',
		'api_method' => 'dial',
		'parameters' => $params,
		'object_id' => $self->{'object_id'}
	});
	$is_success = 1;
	return $is_success;
}

sub continue_in_dialplan {
    # Exit application; continue execution in the dialplan
	my $self = shift;

	$params = {};
	$is_success = $self->{'api'}->call({
		'path' => '/api/channels/%s/continue',
		'http_method' => 'POST',
		'api_method' => 'continue_in_dialplan',
		'parameters' => $params,
		'object_id' => $self->{'object_id'}
	});
	$is_success = 1;
	return $is_success;
}

sub reject_channel {
    # Reject a channel
	my $self = shift;

	$params = {};
	$is_success = $self->{'api'}->call({
		'path' => '/api/channels/%s/reject',
		'http_method' => 'POST',
		'api_method' => 'reject_channel',
		'parameters' => $params,
		'object_id' => $self->{'object_id'}
	});
	$is_success = 1;
	return $is_success;
}

sub answer_channel {
    # Answer a channel
	my $self = shift;

	$params = {};
	$is_success = $self->{'api'}->call({
		'path' => '/api/channels/%s/answer',
		'http_method' => 'POST',
		'api_method' => 'answer_channel',
		'parameters' => $params,
		'object_id' => $self->{'object_id'}
	});
	$is_success = 1;
	return $is_success;
}

sub mute_channel {
    # Mute a channel
	my $self = shift;

	$params = {};
	$is_success = $self->{'api'}->call({
		'path' => '/api/channels/%s/mute',
		'http_method' => 'POST',
		'api_method' => 'mute_channel',
		'parameters' => $params,
		'object_id' => $self->{'object_id'}
	});
	$is_success = 1;
	return $is_success;
}

sub unmute_channel {
    # Unmute a channel
	my $self = shift;

	$params = {};
	$is_success = $self->{'api'}->call({
		'path' => '/api/channels/%s/unmute',
		'http_method' => 'POST',
		'api_method' => 'unmute_channel',
		'parameters' => $params,
		'object_id' => $self->{'object_id'}
	});
	$is_success = 1;
	return $is_success;
}

sub record_channel {
    # Record audio to/from a channel; Start a recording
	my $self = shift;

	$params = {};
	$is_success = $self->{'api'}->call({
		'path' => '/api/channels/%s/record',
		'http_method' => 'POST',
		'api_method' => 'record_channel',
		'parameters' => $params,
		'object_id' => $self->{'object_id'}
	});
	$is_success = 1;
	return $is_success;
}
1;
