#!/usr/bin/env python3
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--ldml", help="ldml file name", default="tst.ldml")
args = parser.parse_args()
if args.ldml:
    print(args.ldml)
from lxml import etree
ldmltree = etree.parse(args.ldml)
collxpath = "/ldml/collations/collation[@type=\"standard\"]/cr/text()"
coll = ldmltree.xpath(collxpath)
stringcoll = "".join(coll)
print (stringcoll)
