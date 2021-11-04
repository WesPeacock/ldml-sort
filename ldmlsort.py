#!/usr/bin/env python3
import argparse
import sys, icu
parser = argparse.ArgumentParser()
parser.add_argument("--ldml", help="ldml file name")
parser.add_argument("--debug", help="debug mode", action='store_true')
parser.add_argument("--nonorm", help="do not normalize input unless specified in ldml", action='store_true')
args = parser.parse_args()
if args.debug and args.ldml: print(args.ldml, file=sys.stderr)
stringnorm = '' if args.nonorm else '[normalization on]\n'
from lxml import etree
coll = ""
if args.ldml:
    ldmltree = etree.parse(args.ldml)
    collxpath = "/ldml/collations/collation[@type=\"standard\"]/cr/text()"
    coll = ldmltree.xpath(collxpath)
stringcoll = stringnorm+"".join(coll)
if args.debug: print(stringcoll, file=sys.stderr)
lines = sys.stdin.readlines()
rbc = icu.RuleBasedCollator(stringcoll)
lines = sorted(lines, key=rbc.getSortKey)
sys.stdout.write(''.join(lines))
sys.stdout.write('\n')


