#!/usr/bin/perl

use strict;
package ParseArgs;

###############################################################################
# Copyright (c) 2013 Erin Spiceland
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#	Redistributions of source code must retain the above copyright
#	notice, this list of conditions and the following disclaimer.
#
#	Redistributions in binary form must reproduce the above
#	copyright notice, this list of conditions and the following
#	disclaimer in the documentation and/or other materials
#	provided with the distribution.
#
#	The name of Digium, Inc., or the name of any Contributor,
#	may not be used to endorse or promote products derived from this
#	software without specific prior written permission.
#
# THIS SOFTWARE IS NOT FAULT TOLERANT AND SHOULD NOT BE USED IN ANY
# SITUATION ENDANGERING HUMAN LIFE OR PROPERTY.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# ``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT HOLDERS AND CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
# OF THE POSSIBILITY OF SUCH DAMAGE.
###############################################################################

###############################################################################
# take a reference to the @ARGV array, parse command line arguments, return
# defaults object with command line options added in.
# Supports the following syntaxes:
# 	-a                        a=1
# 	-a option                 a=option
# 	--string=option           string=option
# 	--string                  string=1
# 	-aftg                     a=1, f=1, t=1, g=1
###############################################################################

sub parse($$) {
	my $a = shift;
	my $vars = shift;
	for (my $i = 0; $i < scalar @{$a}; $i++) {
		if (${$a}[$i] =~ /^--/) {
			${$a}[$i] =~ s/^--//;
			if (${$a}[$i] =~ /=/) {
				${$a}[$i] =~ /([^=]+)=*([^=]*)/;
				$vars->{$1} = $2 || "";
			} else {
				${$a}[$i] =~ /([^=]+)/;
				$vars->{$1} = 1;
			}
		} elsif (${$a}[$i] =~ /^-/) {
			${$a}[$i] =~ s/^-//;
			foreach (split(//, ${$a}[$i])) {
				$vars->{$_} = 1 if $_;
			}
		} else {
			if (${$a}[$i-1] =~ /^.{1,1}$/ && $vars->{${$a}[$i-1]} == 1) {
				$vars->{${$a}[$i-1]} = ${$a}[$i];
			}
		}
	}
	return $vars;
}

1;
