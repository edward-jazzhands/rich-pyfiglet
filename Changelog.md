# Changelog for Rich-Pyfiglet

## 0.2.0 (2025-07-24)

- Deleted the `rich-pyfiglet` github repository. This project is no longer a fork of Pyfiglet. The only reason it was a fork was to add various features I wanted (type hinting, some methods, etc). My type hinting additions were all merged upstream. The few methods I added can just be subclassed now. So there's no reason for this to be a fork anymore. Thus, I nuked it.
- As far as this library is concerned, almost nothing has changed. Except that Pyfiglet is now just a dependency instead of being vendored in as part of the fork. I consider this a major win.
- Added the `fonts_list.py` file since Rich-Pyfiglet no longer stores any of the Figlet fonts itself, and I still wanted to provide a hard-coded list for auto-completion and such.
- Added error checking for non-existent fonts. The rich class now simply raises a rich `ColorParseError` if the font does not exist, which is caught by the CLI and printed as an error message. You can catch this error in your own code if using the RichFiglet class.

## 0.1.4

- Merged the Big type hinting and modernization upgrade from Pyfiglet upstream (written by me, my first major contribution to Pyfiglet)

## 0.1.3

- Added some docstrings to some of the utility methods and marked all the internal rendering/animation methods as private using an underscore.

## 0.1.2

- Fixed mistake in docstring from not updating to match new parameters.

## 0.1.0

- Start of package - split Rich-Pyfiglet out from Textual-Pyfiglet.
