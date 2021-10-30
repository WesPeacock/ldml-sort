#!/usr/bin/env python3
import sys, icu
lines = sys.stdin.readlines()
rbc = icu.RuleBasedCollator('&a < d\n&b < f')
lines = sorted(lines, key=rbc.getSortKey)
sys.stdout.write(''.join(lines))
