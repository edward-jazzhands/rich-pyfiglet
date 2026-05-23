import subprocess
from pathlib import Path
from rich.console import Console
from rich.terminal_theme import SVG_EXPORT_THEME
from rich_pyfiglet import RichFiglet

SNAPSHOTS_DIR = Path("tests/snapshots")
SNAPSHOTS_DIR.mkdir(exist_ok=True)

# -- Helpers --

def diff_snapshots(test_name: str, extension: str):
    diff = subprocess.run(
        [
            "diff",
            "-q",
            f"tests/snapshots/{test_name}.{extension}",
            f"tests/snapshots_historical/{test_name}.{extension}"
        ],
        capture_output=True,
        text=True
    )
    assert diff.returncode == 0, f"Output does not match expected " \
        f"for {test_name}:\n{diff.stdout}\n{diff.stderr}"

def console_factory() -> Console:
    console = Console(width=80, record=True)
    console.print()  # we want a blank line at the top
    return console

def save_n_diff(console: Console, test_name: str):

    console.save_svg(
        f"tests/snapshots/{test_name}.svg", clear=False,
        title=test_name, theme=SVG_EXPORT_THEME
    )
    console.save_text(
        f"tests/snapshots/{test_name}.txt", clear=False
    )
    diff_snapshots(test_name, "svg")
    diff_snapshots(test_name, "txt")

# -- Test functions --

def test_standard_color():
    test_name = "test_standard_color"
    console = console_factory()
    rich_fig = RichFiglet(
        "Rich - PyFiglet",
        colors=["#ff0000", "blue1"],
        width=80,
        dev_mode=True
        
    )
    console.print(rich_fig)
    save_n_diff(console, test_name)

def test_standard():
    test_name = "test_standard"
    console = console_factory()
    rich_fig = RichFiglet(
        "Rich - PyFiglet",
        width=80,
        dev_mode=True
    )
    console.print(rich_fig)
    save_n_diff(console, test_name)


def test_standard_color_horizontal():
    test_name = "test_standard_color_horizontal"
    console = console_factory()
    rich_fig = RichFiglet(
        "Rich - PyFiglet",
        colors=["#ff0000", "blue1"],
        horizontal=True,
        width=80,
        dev_mode=True
    )
    console.print(rich_fig)
    save_n_diff(console, test_name)

def test_standard_with_border():
    test_name = "test_standard_with_border"
    console = console_factory()
    rich_fig = RichFiglet(
        "Rich - PyFiglet",
        colors=["#ff0000", "blue1"],
        horizontal=True,
        border="ROUNDED",
        border_color="magenta1",
        width=80,
        dev_mode=True
    )
    console.print(rich_fig)
    save_n_diff(console, test_name)     

def test_slant():
    test_name = "test_slant"
    console = console_factory()
    rich_fig = RichFiglet(
        "Rich - PyFiglet",
        font="slant",
        width=80,
        dev_mode=True
    )
    console.print(rich_fig)
    save_n_diff(console, test_name)    

def test_ansi_shadow_with_color():
    test_name = "test_ansi_shadow_with_color"
    console = console_factory()
    rich_fig = RichFiglet(
        "Rich - PyFiglet",
        font="ansi_shadow",
        colors=["#ff0000", "blue1"],
        width=80,
        dev_mode=True
    )
    console.print(rich_fig)
    save_n_diff(console, test_name)         

def test_ansi_shadow_color_horizontal():
    test_name = "test_ansi_shadow_color_horizontal"
    console = console_factory()
    rich_fig = RichFiglet(
        "Rich - PyFiglet",
        font="ansi_shadow",
        colors=["#ff0000", "blue1"],
        horizontal=True,
        width=80,
        dev_mode=True
    )
    console.print(rich_fig)
    save_n_diff(console, test_name)  

def test_justify_with_border():
    test_name = "test_justify_with_border"
    console = console_factory()
    rich_fig = RichFiglet(
        "test",
        font="graffiti",
        horizontal=True,
        border="ROUNDED",
        justify="center",
        width=80,
        dev_mode=True,
    )
    console.print(rich_fig)
    save_n_diff(console, test_name)   