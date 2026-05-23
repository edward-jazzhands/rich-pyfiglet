"""
Rich-Pyfiglet Demo

A showcase script for the rich-pyfiglet library.
Run this to see what rich-pyfiglet can do.
"""

from __future__ import annotations
import time
import sys
from typing import Any, cast
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.rule import Rule
from rich.text import Text
from rich.align import Align
from rich.syntax import Syntax
from rich.padding import Padding
from rich import box

from rich_pyfiglet import RichFiglet
from rich_pyfiglet.box_constants import BOX_STYLES

console = Console()


# Helpers


def section(title: str, subtitle: str = "") -> None:
    """Print a section divider."""
    console.print()
    console.print(Rule(f"[bold white]{title}[/]", style="bright_black"))
    if subtitle:
        console.print(Align.center(f"[dim]{subtitle}[/]"))
    console.print()


def pause(seconds: float = 1.2) -> None:
    time.sleep(seconds)


def print_code(snippet: str) -> None:
    console.print(
        Padding(
            Syntax(snippet.strip(), "python", theme="nord", line_numbers=False),
            (0, 4),
        )
    )


# Intro card


def intro() -> None:
    console.clear()
    console.print()

    title_fig = RichFiglet(
        "Rich-PyFiglet",
        font="ansi_regular",
        colors=["#e040fb", "#00e5ff"],
        animation="gradient_down",
        justify="center",
        timer=4.0,
    )
    console.print(title_fig)

    tagline = Text.assemble(
        ("Big ASCII art banners", "bold #e040fb"),
        ("  ·  ", "dim white"),
        ("Rich colors & gradients", "bold #00e5ff"),
        ("  ·  ", "dim white"),
        ("Animated or static", "bold white"),
    )
    console.print(Align.center(tagline))
    console.print()

    install_panel = Panel(
        Align.center("[bold white]pip install rich-pyfiglet[/]"),
        title="[dim]Install[/]",
        border_style="bright_black",
        padding=(0, 4),
    )
    console.print(Padding(install_panel, (0, 8)))
    console.print()
    pause(2)


# Section 1 - Fonts

FONT_SHOWCASE = [
    ("doom", "Hello", ["#ff4444", "#ff8800"], "doom"),
    ("starwars", "Hello", ["#ffe600", "#ff8800"], "starwars"),
    ("larry3d", "Hello", ["#00e5ff", "#0077ff"], "larry3d"),
    ("graffiti", "Hello", ["#e040fb", "#ff4488"], "graffiti"),
    ("ansi_shadow", "Hello", ["#00ff88", "#00ccff"], "ansi_shadow"),
    ("lean", "Hello", ["#ffffff", "#aaaaaa"], "lean"),
]


def fonts_demo() -> None:
    section("Fonts", "571 Figlet fonts are included with Pyfiglet")

    console.print(
        Align.center(
            "[dim]Each banner below uses a different font with a two-color gradient.[/]"
        )
    )
    console.print()

    for font, text, colors, label in FONT_SHOWCASE:
        console.print(
            Rule(
                f"[dim]font=[bold white]{label}[/][/]", style="bright_black", align="left"
            )
        )
        fig = RichFiglet(text, font=font, colors=colors)  # type: ignore[arg-type]
        console.print(fig)
        pause(0.7)

    print_code(
        """
RichFiglet("Hello", font="doom",    colors=["#ff4444", "#ff8800"])
RichFiglet("Hello", font="starwars",colors=["#ffe600", "#ff8800"])
RichFiglet("Hello", font="larry3d", colors=["#00e5ff", "#0077ff"])
    """
    )
    pause(1.5)


# Section 2 - Gradient directions


def gradients_demo() -> None:
    section("Gradient Directions", "Vertical (default) vs horizontal")

    console.print(
        Rule(
            "[dim]vertical gradient  (horizontal=False)[/]",
            style="bright_black",
            align="left",
        )
    )
    console.print()
    console.print(
        RichFiglet(
            "Vertical",
            font="ansi_regular",
            colors=["#ff0080", "#ffcc00"],
        )
    )
    pause(1)

    console.print(
        Rule(
            "[dim]horizontal gradient  (horizontal=True)[/]",
            style="bright_black",
            align="left",
        )
    )
    console.print()
    console.print(
        RichFiglet(
            "Horizontal",
            font="ansi_regular",
            colors=["#ff0080", "#ffcc00"],
            horizontal=True,
        )
    )
    pause(1)

    print_code(
        """
# Vertical (default)
RichFiglet("Vertical",    font="ansi_regular", colors=["#ff0080", "#ffcc00"])

# Horizontal
RichFiglet("Horizontal",, font="ansi_regular", colors=["#ff0080", "#ffcc00"], horizontal=True)
    """
    )
    pause(1.5)


# Section 3 - Multi-color gradients

PALETTES = [
    ("Sunset", ["#ff4500", "#ff8c00", "#ffd700", "#ff69b4"]),
    ("Ocean", ["#001f5b", "#0077b6", "#00b4d8", "#90e0ef"]),
    ("Aurora", ["#00ff88", "#00ccff", "#aa00ff"]),
    ("Inferno", ["#000000", "#ff0000", "#ff8800", "#ffff00"]),
]


def multicolor_demo() -> None:
    section(
        "Multi-color Gradients",
        "Pass as many colors as you like (Note: These are not presets).",
    )

    for name, palette in PALETTES:
        console.print()
        console.print(RichFiglet(text=name, font="dos_rebel", colors=palette))
        console.print()
        swatch = " ".join(f"[{c}]██[/]" for c in palette)
        console.print(f"  {swatch}")
        console.print()
        pause(0.7)

    print_code(
        """
RichFiglet(text="Sunset", font="dos_rebel",
           colors=["#ff4500", "#ff8c00", "#ffd700", "#ff69b4"])
    """
    )
    pause(1.5)


# Section 4 - Borders

BORDERS = [
    ("ROUNDED", "cyan1"),
    ("DOUBLE", "gold1"),
    ("HEAVY", "red1"),
    ("DOUBLE_EDGE", "medium_purple1"),
    ("ASCII", "green_yellow"),
]


def borders_demo() -> None:
    section("Borders", "All Rich box styles are supported")

    for border_name, color in BORDERS:
        console.print(
            Rule(f"[dim]border={border_name!r}[/]", style="bright_black", align="left")
        )
        fig = RichFiglet(
            border_name,
            font="small_slant",
            colors=["white", color],
            # cast here because python type checkers don't like it when you pass a
            # variable into an arg that expects a string literal:
            border=cast(BOX_STYLES, border_name),
            border_color=color,
        )
        console.print(fig)
        pause(0.5)

    print_code(
        """
RichFiglet("ROUNDED", font="small_slant",
           colors=["white", "cyan1"],
           border="ROUNDED", border_color="cyan1")
    """
    )
    pause(1.5)


# Section 5 - Animations

ANIMATIONS: list[tuple[str, dict[str, Any]]] = [
    (
        "gradient_down",
        dict(
            font="ansi_regular",
            colors=["#e040fb", "#00e5ff"],
            border="HEAVY",
            border_color="#e040fb",
            timer=5.0,
        ),
    ),
    (
        "gradient_up",
        dict(
            font="ansi_shadow",
            colors=["#ff4444", "#ffcc00"],
            border="ROUNDED",
            border_color="#ffcc00",
            timer=5.0,
        ),
    ),
    (
        "smooth_strobe",
        dict(
            font="dos_rebel",
            colors=["bright_blue", "bright_yellow", "bright_red"],
            timer=8.0,
        ),
    ),
    (
        "fast_strobe",
        dict(
            font="big_money-nw",
            colors=["#ff4444", "#ffcc00", "#00ff88", "#00ccff"],
            fps=1.5,
            timer=6.0,
        ),
    ),
]


def animations_demo() -> None:
    section(
        "Animations",
        "gradient_down · gradient_up · smooth_strobe · fast_strobe\n"
        "  [dim](Each animation runs for 5 s - press Ctrl+C to skip to the next)[/]",
    )
    pause(1)

    for anim_name, kwargs in ANIMATIONS:
        console.print()
        console.print(
            Align.left(f"[bold white]animation=[italic cyan]{anim_name!r}[/][/]")
        )
        console.print()
        fig = RichFiglet(anim_name.replace("_", " "), animation=anim_name, **kwargs)  # type: ignore
        console.print(fig)
        pause(0.8)

    print_code(
        """
RichFiglet("gradient down", font="ansi_regular",
           colors=["#e040fb", "#00e5ff"],
           animation="gradient_down", timer=5.0)
    """
    )
    pause(1.5)


# Section 6 - Use inside a Rich script (practical example)


def practical_demo() -> None:
    section(
        "Real-World Usage",
        "Drop RichFiglet anywhere you'd use console.print()",
    )

    # Simulate an app startup header
    console.print(
        RichFiglet(
            "MyApp v2.0",
            font="small_slant",
            colors=["#00ff88", "#00ccff"],
            border="ROUNDED",
            border_color="#00ccff",
        )
    )

    table = Table(
        title="[bold white]Startup Checks[/]",
        box=box.ROUNDED,
        border_style="bright_black",
        header_style="bold cyan",
        show_lines=True,
    )
    table.add_column("Check", style="white")
    table.add_column("Status", justify="center")
    table.add_column("Detail", style="dim")

    rows = [
        ("Config file", "[green]✓ OK[/]", "~/.myapp/config.toml"),
        ("Database", "[green]✓ OK[/]", "postgres://localhost:5432"),
        ("Cache", "[green]✓ OK[/]", "Redis 7.2"),
        ("Auth service", "[yellow]⚠ SLOW[/]", "179 ms - above threshold"),
        ("Feature flags", "[green]✓ OK[/]", "3 flags active"),
    ]
    for row in rows:
        table.add_row(*row)
        pause(0.2)

    console.print(Padding(table, (0, 4)))
    console.print()

    print_code(
        """
# Works exactly like any other Rich renderable
console.print(
    RichFiglet("MyApp v2.0", font="small_slant",
               colors=["#00ff88", "#00ccff"],
               border="ROUNDED", border_color="#00ccff")
)
console.print(my_rich_table)
    """
    )
    pause(2)


# Outro


def outro() -> None:
    section("Credits")

    links = Table.grid(padding=(0, 3), expand=True)
    links.add_column(justify="right", style="dim")
    links.add_column(style="bold white")
    links.add_row("PyPI", "pip install rich-pyfiglet")
    links.add_row("UV", "uv tool install rich-pyfiglet")
    links.add_row("Pipx", "pipx install rich-pyfiglet")
    links.add_row("GitHub", "https://github.com/edward-jazzhands/rich-pyfiglet")
    links.add_row("", "")
    links.add_row("", "[dim]Built on [bold]Rich[/] + [bold]Pyfiglet[/][/]")
    links.add_row("", "")
    links.add_row("Rich", "https://github.com/textualize/rich")
    links.add_row("Pyfiglet", "https://github.com/pwaller/pyfiglet")

    console.print(Align.center(links))
    console.print()

    console.print(
        RichFiglet(
            "Thanks!",
            font="slant",
            colors=["yellow", "magenta2"],
            border="DOUBLE_EDGE",
            border_color="#e040fb",
            justify="center",
        )
    )


# Entry point

SECTIONS = {
    "intro": intro,
    "fonts": fonts_demo,
    "gradients": gradients_demo,
    "multicolor": multicolor_demo,
    "borders": borders_demo,
    "animations": animations_demo,
    "practical": practical_demo,
    "credits": outro,
}


def run(start_at: str | None = None) -> None:
    """
    Run the full demo, or play a specific section.

    Args:
        start_at: Name of the section to play (e.g. "fonts", "animations").
                  If None, runs from the beginning.
    """

    if start_at:
        start_at = start_at.lower()
        if start_at not in SECTIONS:
            raise ValueError(
                f"Section {start_at} not found. Choose from: {SECTIONS.keys()}"
            )
        fn = SECTIONS[start_at]
        try:
            fn()
        except KeyboardInterrupt:
            console.print()
    else:
        for fn in SECTIONS.values():
            try:
                fn()
            except KeyboardInterrupt:
                # Ctrl+C inside an animation block - continue to next section
                console.print()


if __name__ == "__main__":
    # Optional: pass a section name as CLI arg to jump straight to it
    # e.g.  python demo.py animations
    start = sys.argv[1] if len(sys.argv) > 1 else None
    run(start_at=start)
