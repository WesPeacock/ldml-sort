#!/usr/bin/perl
my $USAGE = "Usage: $0 --ldml languagecode.ldml";

my $debug=0;
my $checktags=0; #Stop after checking the validity of the tags

use 5.016;
use strict;
use warnings;
use English;
use utf8;
use open qw/:std :utf8/;
use XML::LibXML;
use Getopt::Long;
GetOptions (
	'ldml:s'   => \(my $ldmlfilename= "test.ldml"), # ldml filename
#	'debug'       => \my $debug,
	) or die "$USAGE\n";

my $ldmltree = XML::LibXML->load_xml(location => $ldmlfilename);
my ($icu) = $ldmltree->findnodes('/ldml/collations/collation[@type="standard"]/cr/text()');
$icu =~ s/.*?CDATA\[//;
$icu =~ s/\]\]\>$//;
say $icu;
