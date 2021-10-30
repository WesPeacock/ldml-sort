#!/usr/bin/env python3
import argparse
import sys, icu
parser = argparse.ArgumentParser()
parser.add_argument("--ldml", help="ldml file name", default="default.ldml")
args = parser.parse_args()
"""
if args.ldml:
    sys.stderr.write(args.ldml)
"""
from lxml import etree
ldmltree = etree.parse(args.ldml)
collxpath = "/ldml/collations/collation[@type=\"standard\"]/cr/text()"
coll = ldmltree.xpath(collxpath)
stringcoll = "".join(coll)
lines = sys.stdin.readlines()
rbc = icu.RuleBasedCollator(stringcoll)
lines = sorted(lines, key=rbc.getSortKey)
sys.stdout.write(''.join(lines))
sys.stdout.write('\n')


