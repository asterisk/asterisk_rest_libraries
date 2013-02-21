#!/usr/bin/perl

use strict;
use LWP::UserAgent;
use Data::Dumper;
use JSON;

my $HOST = '192.168.1.124';
#my $HOST = '10.24.67.73';
my $PORT = '8088';
my $REQ = $ARGV[0];
my $JSON_PATH = '/home/erin/api_stuff';

my $ua = LWP::UserAgent->new;
my $j = JSON->new->utf8;

foreach my $file (glob("$JSON_PATH/*.json")) {
	# skip if file size is 0
	next if -z $file;
	my $res = get_JSON_from_file($file);

	# skip if JSON is missing some key things
	next if !$res->{'apis'};
	next if !$res->{'resourcePath'};

	foreach my $api (@{$res->{'apis'}}) {
		# skip if there are no operations
		next if !$api->{'operations'};
		foreach my $op (@{$api->{'operations'}}) {
			my $uri = "http://$HOST:$PORT/stasis" . $api->{'path'};
			if ($uri =~ /[{}]/) {
				print "\tSkipping object-specific request\n";
				next;
			}
			my $paramObj = generate_params($op->{'parameters'});
			my $response;
			if ($op->{'httpMethod'} eq 'GET') {
				my $paramString = make_param_string($paramObj);
				$response = $ua->get("$uri$paramString");
			} elsif ($op->{'httpMethod'} eq 'POST') {
				$response = $ua->post($uri, $paramObj);
			#} elsif ($op->{'httpMethod'} eq 'DELETE') {
			#	my $paramString = make_param_string($paramObj);
			#	$response = $ua->delete("$uri$paramString");
			} elsif ($op->{'httpMethod'} eq 'PUT') {
				$response = $ua->put($uri, $paramObj);
			}
			next if !$response;
			print $op->{'responseClass'}, ' ', $op->{'httpMethod'}, ' ',
				$uri, "\n";
			if ($response->content =~ /connection refused/i) {
				print "Can't contact server.\n";
				exit(1);
			}
			if ($response->content) {
				if (eval { JSON::XS::decode_json($response->content); 1; } ) {
					my $content = JSON::XS::decode_json($response->content);
					print "\t", $response->status_line, "\n";
				} else {
					print "\tINVALID JSON\n";
					print $response->content, "\n";
				}
			}
		}
	}
}

sub ddump($) {
	my $ref = shift;
	if ($ref) {
		print Data::Dumper::Dumper($ref), "\n";
	}
}

sub get_JSON_from_file($) {
	my $file = shift;
	open INF, $file;
	my $json = join('', <INF>);
	close INF;
	return JSON::XS::decode_json($json);
}

sub generate_params($) {
	my $params = shift;
	my $res = {};
	foreach my $param (@$params) {
		if ($param->{'dataType'} eq 'string') {
			$res->{$param->{'name'}} = $param->{'allowMultiple'}
				? 'example' : ['example', 'string'];
		} elsif ($param->{'dataType'} eq 'number') {
			$res->{$param->{'name'}} = $param->{'allowMultiple'}
				? 20 : ['20', '8'];
		} elsif ($param->{'dataType'} eq 'boolean') {
			$res->{$param->{'name'}} = $param->{'allowMultiple'}
				? 'true' : ['true', 'false'];
		}
	}
	return $res;
}

sub make_param_string($) {
	my $params = shift;
	my $strings = [];
	foreach my $name (keys %$params) {
		if (ref $params->{$name} eq 'ARRAY') {
			push @$strings, join('=', $name, join(',', @{$params->{$name}}));
		} elsif (ref $params->{$name} eq 'SCALAR') {
			push @$strings, join('=', $name, $params->{$name});
		}
	}
	return '?' . join('&', @$strings);
}

