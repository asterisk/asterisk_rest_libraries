#!/usr/bin/perl -w

use strict;
use LWP::UserAgent;
use Data::Dumper;
use JSON;
use lib 'lib';
use ParseArgs;

my $defaults = {
	'host' => '192.168.1.124',
	'port' => '8088',
	'path' => 'test_resources',
};
my $args = ParseArgs::parse(\@ARGV, $defaults);

my $ua = LWP::UserAgent->new;
my $j = JSON->new->utf8;

foreach my $file (glob($args->{'path'} . "/*.json")) {
	# skip if file size is 0
	next if -z $file;

	# skip if JSON is missing some key things
	my $res = get_JSON_from_file($file);
	next if !$res->{'apis'};
	next if !$res->{'resourcePath'};

	foreach my $api (@{$res->{'apis'}}) {
		# skip if there are no operations
		next if !$api->{'operations'};
		foreach my $op (@{$api->{'operations'}}) {
			my $uri = "http://" . $args->{'host'} . ":" . $args->{'port'}
				. "/stasis" . $api->{'path'};
			if ($uri =~ /[{}]/) {
				$uri =~ s/\{\w+\}/1/i;
			}
			my $paramObj = generate_params($op->{'parameters'});
			my $response;
			if ($op->{'httpMethod'} eq 'GET') {
				my $paramString = make_param_string($paramObj);
				$response = $ua->get("$uri$paramString");
			} elsif ($op->{'httpMethod'} eq 'POST') {
				$response = $ua->post($uri, $paramObj);
			} elsif ($op->{'httpMethod'} eq 'DELETE') {
				my $paramString = make_param_string($paramObj);
				$response = $ua->delete("$uri$paramString");
			} elsif ($op->{'httpMethod'} eq 'PUT') {
				$response = $ua->put($uri, $paramObj);
			}
			next if !$response;
			print sprintf("%s %s %s\n", $op->{'responseClass'},
				$op->{'httpMethod'}, $uri);
			if ($response->content =~ /connection refused/i) {
				print "Can't contact server.\n";
				exit(1);
			}
			if ($response->content) {
				if (eval { JSON::XS::decode_json($response->content); 1; }) {
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
