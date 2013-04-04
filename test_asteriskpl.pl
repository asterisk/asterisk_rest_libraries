#!/usr/bin/perl
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

use lib 'perl/lib';
use lib 'lib'; # ParseArgs

use ParseArgs;
use AsteriskPl;

my $defaults = {
	'api_url' => 'http://192.168.1.124:8088/stasis'
};
my $args = ParseArgs::parse(\@ARGV, $defaults);
my $ast = AsteriskPl->new(%$args);
my $result = $ast->get_asterisk_info();
print "Asterisk status is ", $result->{'response'}, "\n";

print "Running AsteriskPl::get_endpoints\n";
my $endpoints = $ast->get_endpoints();
print "Running AsteriskPl::get_channels\n";
my $channels = $ast->get_channels();
print "Running AsteriskPl::get_bridges\n";
my $bridges = $ast->get_bridges();
print "Running AsteriskPl::get_recordings\n";
my $recordings = $ast->get_recordings();
print "Running AsteriskPl::create_channel\n";
my $channel = $ast->create_channel({'tech' => 'dummy_params'});
print "Running AsteriskPl::create_bridge\n";
my $bridge = $ast->create_bridge({'tech' => 'dummy_params'});

foreach my $endpoint (@$endpoints) {
	print "got endpoint with id ", $endpoint->get_id(),"\n";
}

foreach my $channel (@$channels) {
	print "got channel with id ", $channel->get_id(), "\n";
	print "method delete returns ", $channel->delete_channel(), "\n";
	print "method reject returns ", $channel->reject_channel(), "\n";
	print "method answer returns ", $channel->answer_channel(), "\n";
	print "method mute returns ", $channel->mute_channel(), "\n";
	print "method unmute returns ", $channel->unmute_channel(), "\n";
	print "method record returns ", $channel->record_channel('rec name'), "\n";
	print "method dial returns ", $channel->dial(), "\n";
	print "method continue_in_dialplan returns ",
		$channel->continue_in_dialplan(), "\n";
	print "method originate returns ", $channel->originate(), "\n";
}

my $chan = AsteriskPl::Channel->new('api' => $ast->{'api'});
foreach my $bridge (@$bridges) {
	print "got bridge with id ", $bridge->get_id(), "\n";
	print "method new_bridge returns ", $bridge->new_bridge(), "\n";
	print "method delete_bridge returns ", $bridge->delete_bridge(), "\n";
	print "method add_channel_to_bridge return ",
		$bridge->add_channel_to_bridge($chan->get_id()), "\n";
	print "method remove_channel_from_bridge returns ",
		$bridge->remove_channel_from_bridge($chan->get_id()), "\n";
	print "method record_bridge returns ",
		$bridge->record_bridge('rec name'), "\n";
}

foreach my $recording (@$recordings) {
	print "got recording with id ", $recording->get_id(), "\n";
	print "method delete_recording returns ",
		$recording->delete_recording(), "\n";
	print "method stop_recording returns ", $recording->stop_recording(), "\n";
	print "method pause_recording returns ",
		$recording->pause_recording(), "\n";
	print "method unpause_recording returns ",
		$recording->unpause_recording(), "\n";
	print "method mute_recording returns ", $recording->mute_recording(), "\n";
	print "method unmute_recording returns ",
		$recording->unmute_recording(), "\n";
}
