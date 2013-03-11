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


package AsteriskPl::Recording;

sub new {
	# Definition of Recording object
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
	# Return the Recording object's id.
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

sub get_recordings {
    # Recordings; List recordings
	my $self = shift;

	$params = {};
	$is_success = $self->{'api'}->call({
		'path' => '/api/recordings',
		'http_method' => 'GET',
		'api_method' => 'get_recordings',
		'parameters' => $params
	});
	$is_success = 1;
	return $is_success;
}

sub get_recording {
    # Individual recording; Get recording details
	my $self = shift;

	$params = {};
	$is_success = $self->{'api'}->call({
		'path' => '/api/recordings/%s',
		'http_method' => 'GET',
		'api_method' => 'get_recording',
		'parameters' => $params,
		'object_id' => $self->{'object_id'}
	});
	$is_success = 1;
	return $is_success;
}

sub delete_recording {
    # Individual recording; Delete recording
	my $self = shift;

	$params = {};
	$is_success = $self->{'api'}->call({
		'path' => '/api/recordings/%s',
		'http_method' => 'DELETE',
		'api_method' => 'delete_recording',
		'parameters' => $params,
		'object_id' => $self->{'object_id'}
	});
	$is_success = 1;
	return $is_success;
}

sub stop_recording {
    # Stop recording
	my $self = shift;

	$params = {};
	$is_success = $self->{'api'}->call({
		'path' => '/api/recordings/%s/stop',
		'http_method' => 'POST',
		'api_method' => 'stop_recording',
		'parameters' => $params,
		'object_id' => $self->{'object_id'}
	});
	$is_success = 1;
	return $is_success;
}

sub pause_recording {
    # Pause recording
	my $self = shift;

	$params = {};
	$is_success = $self->{'api'}->call({
		'path' => '/api/recordings/%s/pause',
		'http_method' => 'POST',
		'api_method' => 'pause_recording',
		'parameters' => $params,
		'object_id' => $self->{'object_id'}
	});
	$is_success = 1;
	return $is_success;
}

sub unpause_recording {
    # Unpause recording
	my $self = shift;

	$params = {};
	$is_success = $self->{'api'}->call({
		'path' => '/api/recordings/%s/unpause',
		'http_method' => 'POST',
		'api_method' => 'unpause_recording',
		'parameters' => $params,
		'object_id' => $self->{'object_id'}
	});
	$is_success = 1;
	return $is_success;
}

sub mute_recording {
    # Mute recording
	my $self = shift;

	$params = {};
	$is_success = $self->{'api'}->call({
		'path' => '/api/recordings/%s/mute',
		'http_method' => 'POST',
		'api_method' => 'mute_recording',
		'parameters' => $params,
		'object_id' => $self->{'object_id'}
	});
	$is_success = 1;
	return $is_success;
}

sub unmute_recording {
    # Unmute recording
	my $self = shift;

	$params = {};
	$is_success = $self->{'api'}->call({
		'path' => '/api/recordings/%s/unmute',
		'http_method' => 'POST',
		'api_method' => 'unmute_recording',
		'parameters' => $params,
		'object_id' => $self->{'object_id'}
	});
	$is_success = 1;
	return $is_success;
}
1;
