# LDML-Sort #

This repo contains a Python program to perform a line sort on STDIN using a collating sequence from a Unicode Locale Data Markup Language (LDML) file.

If no LDML file is specified, the program sorts using the  Default Unicode Collation Element Table (DUCET)

By default, the data is normalized before sorting.

### Setup

Here are some instructions for installing the *icu* library that does the heavy lifting:

````python
# Linux: pip install PyICU
# Windows: From https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyicu download the "wheel" (.whl file) to match
# the version of Python ("cp37" for Python 3.7, for example) and Windows ("amd64" for 64-bit Windows) you have.
# Then: pip install PyICU‑2.5‑cp37‑cp37m‑win_amd64.whl (but using the actual .whl file you downloaded)
````

Those instructions are from the documentation at: https://github.com/silnrsi/collation

Additional information about *icu* is available at: https://scriptsource.org/cms/scripts/page.php?item_id=entry_detail&uid=lcepuup9ga

### Bugs

This program is mostly a proof of concept, illustrating simple LDML collation extraction and sorting of STDIN.

I'm not sure it handles line endings properly.

No error handling of the LDML (e.g. more than one *collation*)

No error handling for invalid Unicode data.
