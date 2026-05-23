# Changelog for Rich-Pyfiglet

## [2.0.1] 2026-05-23

### Hot Fix

- Main CLI arg was accidentally set to have a default value of None.

## [2.0.0] 2026-05-23

### Added

**Library additions:**

- Added the `justify` argument to the RichFiglet constructor. This allows you to set the justification of the figlet. Dunno why I didn't add this before honestly.
- Added the `width` argument to the RichFiglet constructor. If not set, the terminal width will be used.
- Added the `timer` argument to the RichFiglet constructor. This allows you to set a timer for the animation to run for, instead of running indefinitely.
- [dev] Added a `dev_console` argument to the RichFiglet constructor which allows you to pass in a console to print debug information to, making it possible to use the same console the RichFiglet is printed to, or make it print to stdout.
- [dev] Added more information to the debug output in dev mode.

The documentation has been updated to reflect these changes.

**CLI additions:**

- Added the `demo` command to run a new demo. The new demo now ships with the package and is much more polished than the old example file.
- Added the `--justify` option.
- Added the `--width` option.
- Added the `--border` flag.
- Added the `--border-color` flag to set the border color.
- Added the `borders` command to list available borders.
- Added the `--random` flag to try out random fonts.
- Added some usage examples to the CLI help menu.
- [dev] Enabled rich tracebacks in the CLI for development.

### Changed

**Library changes:**

- [BREAKING] Removed support for Python 3.9
- Bumped max Rich version up to 15 (#13 by @abulgher).
- [dev] Changed the maximum line length to 90 characters (I repent from my previous usage of 110 characters)
- [dev] Created one `_send_animation_to_worker` function for all the animation functions to share, reduced some code duplication.
- [dev] Small optimization to the logic to remove blank lines.
- [dev] Updated UV build version to >=0.9.24,<0.10.0

**CLI changes:**

- Swapped out regular Click for Rich-Click. Now the help menu prints with colors and rich formatting. This project already had both Rich and Click, so this was a natural choice.
- Updated the CLI UX so `figlet` is now a command, and set to the default command. Usage should remain identical, except that using `rich-pyfiglet` with no arguments or options will no longer print the help menu, and instead shows a "Missing argument" error.
- Changed the `--list` flag to be a command called `fonts`, and removed the leading hyphen "- " on each font name when printing the list.
- Changed the `--dev` flag to print the debug output to stderr instead of stdout, also now uses a Rich console for coloring the output.

**Testing changes:**

- Updated all the historical snapshots. The old ones had some consistency issues, so I updated them to match the new ones. I also added two new snapshot types. It now also snapshots .txt files alongside the .svg files, and diffs both of them. This should provide more comprehensive coverage than the svg snapshots alone.

## [1.0.0] 2025-07-30

### Changed

- Promoted library to 1.0.0 / stable release.
- Bumped required version of Pyfiglet up to the new 1.0.3 release
- Dropped required version of Rich to 12.0.0 (confirmed with Nox testing)
- [dev] Renamed Changelog.md to CHANGELOG.md

### Added

- [dev] Added 2 workflow to .github/workflows:
  - ci-checks.yml - runs Nox testing suite
  - release.yml - Workflow to publish to PyPI and github releases
- [dev] Added 2 scripts to .github/scripts:
  - adds .github/scripts/validate_main.sh
  - adds .github/scripts/tag_release.py
- [dev] Added `/tests` directory with unit tests, a [pytest] section in `pyproject.toml`, and added `just test` command to the justfile.
- [dev] Added Nox testing and `noxfile.py` to run tests in different Python versions and across different versions of Textual.
- [dev] Added pytest dev dependencies.

### Removed

- [dev] Deleted the `pyrightconfig.json` file, since it was not needed anymore (in pyproject.toml now).

## [0.2.0] 2025-07-24

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
