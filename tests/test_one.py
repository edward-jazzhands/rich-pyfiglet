import subprocess
from rich.console import Console
from rich_pyfiglet import RichFiglet

def diff_snapshots(test_name: str):
    diff = subprocess.run(
        [
            "diff",
            f"tests/snapshots/{test_name}.svg",
            f"tests/snapshots_historical/{test_name}.svg"
        ],
        capture_output=True,
        text=True
    )
    assert diff.returncode == 0, f"Output does not match expected " \
        f"for {test_name}:\n{diff.stdout}\n{diff.stderr}"

def test_standard_color():
    test_name = "test_standard_color"
    console = Console(width=80, record=True)
    rich_fig = RichFiglet(
        "Rich - PyFiglet",
        colors=["#ff0000", "blue1"],
    )
    console.print(rich_fig)
    console.save_svg(
        f"tests/snapshots/{test_name}.svg",
        title=test_name
    )
    diff_snapshots(test_name)

def test_standard():
    test_name = "test_standard"
    console = Console(width=80, record=True)
    rich_fig = RichFiglet(
        "Rich - PyFiglet",
    )
    console.print(rich_fig)
    console.save_svg(
        f"tests/snapshots/{test_name}.svg",
        title=test_name
    )
    diff_snapshots(test_name)


def test_standard_color_horizontal():
    test_name = "test_standard_color_horizontal"
    console = Console(width=80, record=True)
    rich_fig = RichFiglet(
        "Rich - PyFiglet",
        colors=["#ff0000", "blue1"],
        horizontal=True,
    )
    console.print(rich_fig)
    console.save_svg(
        f"tests/snapshots/{test_name}.svg",
        title=test_name
    )
    diff_snapshots(test_name)

def test_standard_with_border():
    test_name = "test_standard_with_border"
    console = Console(width=80, record=True)
    rich_fig = RichFiglet(
        "Rich - PyFiglet",
        colors=["#ff0000", "blue1"],
        horizontal=True,
        border="ROUNDED",
        border_color="magenta1",
    )
    console.print(rich_fig)
    console.save_svg(
        f"tests/snapshots/{test_name}.svg",
        title=test_name
    )
    diff_snapshots(test_name)     

def test_slant():
    test_name = "test_slant"
    console = Console(width=80, record=True)
    rich_fig = RichFiglet(
        "Rich - PyFiglet",
        font="slant",
    )
    console.print(rich_fig)
    console.save_svg(
        f"tests/snapshots/{test_name}.svg",
        title=test_name
    )
    diff_snapshots(test_name)    

def test_ansi_shadow_with_color():
    test_name = "test_ansi_shadow_with_color"
    console = Console(width=80, record=True)
    rich_fig = RichFiglet(
        "Rich - PyFiglet",
        font="ansi_shadow",
        colors=["#ff0000", "blue1"],
        width=90,
    )
    console.print(rich_fig)
    console.save_svg(
        f"tests/snapshots/{test_name}.svg",
        title=test_name
    )
    diff_snapshots(test_name)         

def test_ansi_shadow_color_horizontal():
    test_name = "test_ansi_shadow_color_horizontal"
    console = Console(width=80, record=True)
    rich_fig = RichFiglet(
        "Rich - PyFiglet",
        font="ansi_shadow",
        colors=["#ff0000", "blue1"],
        width=90,
        horizontal=True,
    )
    console.print(rich_fig)
    console.save_svg(
        f"tests/snapshots/{test_name}.svg",
        title=test_name
    )
    diff_snapshots(test_name)  