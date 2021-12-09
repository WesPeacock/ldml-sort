# LDML-Sort #

This repo contains a Python program to perform a line sort on STDIN using a collating sequence from Unicode Locale Data Markup Language (LDML) file.

If no LDML file is specified, the program sorts using the  Default Unicode Collation Element Table (DUCET)

By default, the data is normalized before sorting.

### Bugs

This program is mostly a proof of concept, illustrating simple LDML collation extraction and sorting of STDIN.

I'm not sure it handles line endings properly.

No error handling of the LDML (e.g. more than one *collation*)

No error handling for invalid Unicode data.