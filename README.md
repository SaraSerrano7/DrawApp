# DRAWAPP #

## How to use ##

This is the version for Python of DrawApp that works for Windows.

Actually there are three languages supported: 
- English -- 'en'
- Spanish -- 'es'
- Catalan -- 'ca'

To switch easily between languages, line 10:

    translate = gettext.translation(<language>, localedir, languages=[<language>])

must be changed, where `<language>` is one of the three languages mentioned before.

When the program is executed with run configuration 'main', you must answer 3 questions:
- The shape you want to draw (line, square or circle)
- The color you want your figure to be (red, green or blue)
- The size you want your figure to be (little, medium or big)

Then, the figure drawn is shown.

## How internationalization has been done ##

- Every string hardcoded in `main.py` has been surrounded by _()
- Folder `i18n` has been added with `msgfmt.py` and `pygettext.py`
- Directory structure `locales` has been created.
- `pygettext.py` is executed with run configuration 'pygettext main', and `messages.pot` is created.
- There is a copy of `messages.pot` created for every language supported, placed in its folder, named <language.po> and translated.
- `msgfmt.py` has been executed, once per every language, with run configurations named 'msgfmt main <language>'
