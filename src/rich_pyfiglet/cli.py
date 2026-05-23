# standard library
from __future__ import annotations
from typing import get_args, cast, Any
import random as random_module
from pathlib import Path

# third party
import rich_click as click
from click.core import Command
from rich.console import Console
import rich.traceback as traceback
from rich.color import ColorParseError

# project
from rich_pyfiglet.rich_figlet import ANIMATION_TYPE, JUSTIFICATION
from rich_pyfiglet.fonts_list import ALL_FONTS
from rich_pyfiglet.box_constants import BOX_STYLES

# NOTE: The rich traceback would create a console for stderr anyway, but this allows
# us to re-use the same console object for faster startup.
console_stderr = Console(stderr=True)
traceback.install(console=console_stderr)

# Rich-click Config
click.rich_click.MAX_WIDTH = 130  # purely aesthetic - anything over 130 looks too wide
click.rich_click.SHOW_ARGUMENTS = True
click.rich_click.COMMANDS_BEFORE_OPTIONS = True
click.rich_click.THEME = "cargo-robo"
click.rich_click.USE_MARKDOWN = True
# colorschemes: #~ [default, star, quartz, quartz2, cargo, forest, nord, dracula, solarized]
# theme types: #~ [box, slim, modern, robo, nu]
# nord, dracula, and solarized are "risky" according to the docs.


class DefaultRichGroup(click.RichGroup):
    """A RichGroup that supports a default command."""

    # NOTE: 'ignore_unknown_options' in `context_settings` tells Click "If you see a flag
    # you don't recognize, don't exit (yet). Just pass it down the chain." It's necessary to
    # make our 'default command' work, because we need options to be used on the main group
    # and then be passed down to the default command. Without this, it would see that any
    # option (ie. --font) does not exist on the main group and raise an error. Of course,
    # it will still raise an error if the option does not exist on the subcommand either.

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self.default_command = kwargs.pop("default", None)
        context_settings = kwargs.setdefault("context_settings", {})
        context_settings["ignore_unknown_options"] = True
        super().__init__(*args, **kwargs)

    def parse_args(self, ctx: click.Context, args: Any) -> list[str]:
        # If absolutely no arguments were provided, inject the default command
        if not args and self.default_command:
            args.insert(0, self.default_command)
        return super().parse_args(ctx, args)

    def resolve_command(
        self, ctx: click.Context, args: Any
    ) -> tuple[str | None, Command | None, list[str]]:
        # If arguments were provided, but the first one isn't a registered subcommand,
        # assume they are arguments meant for the default command.
        if args and self.default_command and args[0] not in self.commands:
            # Don't inject if they are just asking for help on the main group
            if args[0] not in ["-h", "--help"]:
                args.insert(0, self.default_command)

        return super().resolve_command(ctx, args)


font_help = "Set the font. Use the fonts command to see a list of available fonts"
width_help = "Set the width of the text. If not set, the terminal width will be used"
justify_help = "Set the justification of the text. Can be 'left', 'center', or 'right'"
colors_help = (
    "Pass in a color or a list of colors. Colors can be hex, RGB, or named colors. "
    "If using a list, separate colors with colons: 'red:green:blue'. For supported "
    "named colors, see: https://rich.readthedocs.io/en/stable/appendix/colors.html"
)
animation_help = (
    "Set the animation type. Can be 'gradient_up', 'gradient_down', 'smooth_strobe', "
    "or 'fast_strobe'. Requires at least 2 colors to be set"
)
quality_help = (
    "Set the gradient quality. Default is auto, which will calculate all gradients in "
    "your color list to match either the width (in horizontal mode) or the height "
    "(in vertical mode) of the rendered banner"
)
fps_help = (
    "Set the animation frames per second. Default is 5 fps, unless using the "
    "'fast_strobe' animation type, which defaults to 1.5 fps"
)
horizontal_help = (
    "Flag to render the gradient horizontally. "
    "Note that this setting will be ignored if animate is set to True"
)
border_help = (
    "Set the border type. Use the borders command to see a list of available borders"
)
border_color_help = (
    "Set the border color. Available colors is the same as the colors option."
)
random_help = "Randomize the font"
dev_help = "Run CLI in verbose/dev mode. This will print extra debug information"

# get the main help text from the file
main_help_path = Path(__file__).parent / "main_help.md"
main_help = main_help_path.read_text()


@click.group(cls=DefaultRichGroup, default="figlet", help=main_help)
@click.command_panel("Commands", commands=["figlet", "demo", "fonts", "borders"])  # type: ignore[unused-ignore]
def cli() -> None:
    pass


@cli.command()
@click.argument("text", type=str, required=True)
@click.option("--font", "-f", type=str, default="ansi_shadow", help=font_help)
@click.option("--width", "-w", type=int, default=None, help=width_help)
@click.option("--justify", "-j", type=str, default="left", help=justify_help)
@click.option("--colors", "-c", type=str, default=None, help=colors_help)
@click.option("--horizontal", "-h", is_flag=True, default=False, help=horizontal_help)
@click.option("--quality", "-q", type=int, default=None, help=quality_help)
@click.option("--animation", "-a", type=str, default=None, help=animation_help)
@click.option("--fps", type=float, default=None, help=fps_help)
@click.option("--border", "-b", type=str, default=None, help=border_help)
@click.option("--border-color", "-bc", type=str, default=None, help=border_color_help)
@click.option("--random", "-r", is_flag=True, default=False, help=random_help)
@click.option("--dev", "-v", is_flag=True, default=False, help=dev_help)
@click.pass_context
def figlet(
    ctx: click.Context,
    text: str,
    font: str | None,
    width: int | None,
    justify: str,
    colors: str | None,
    horizontal: bool,
    quality: int | None,
    animation: str | None,
    fps: float | None,
    border: str | None,
    border_color: str | None,
    random: bool,
    dev: bool,
) -> None:
    """(Default) Print text using a figlet font"""

    if font not in get_args(ALL_FONTS):
        raise click.UsageError(
            f"Font '{font}' not found. Use fonts command to see available fonts."
        )

    if width and width <= 0:
        raise click.UsageError("Width must be greater than 0.")

    if justify not in get_args(JUSTIFICATION):
        raise click.UsageError(
            f"Justification '{justify}' not found. Must be one of {get_args(JUSTIFICATION)}"
        )

    if animation and (colors is None or ":" not in colors):
        raise click.UsageError(
            "Animate requires at least two colors to be set. Use a list of colors separated by colons.\n"
            "For a list of available colors, see: https://rich.readthedocs.io/en/stable/appendix/colors.html"
        )

    if animation and fps and fps <= 0:
        raise click.UsageError("Animate requires fps be greater than 0.")

    if animation and animation not in get_args(ANIMATION_TYPE):
        raise click.UsageError(
            "Animation type must be 'gradient_up', 'gradient_down', 'smooth_strobe', or 'fast_strobe'."
        )

    if border:
        if border.upper() not in get_args(BOX_STYLES):
            raise click.UsageError(
                f"Border {border} not found. Use borders command to see available borders."
            )
        border = border.upper()

    if border_color and not border:
        raise click.UsageError("Border color can only be used with a border.")

    if random:
        font = random_module.choice(get_args(ALL_FONTS))

    # I don't bother validating the colors because Rich will already give a helpful
    # error if the user enters an invalid color.
    if colors:
        colors_list = colors.split(":")
    else:
        colors_list = None

    from rich_pyfiglet.rich_figlet import RichFiglet

    try:
        rich_figlet = RichFiglet(
            text,
            font=cast(ALL_FONTS, font),
            width=width,
            justify=cast(JUSTIFICATION, justify),
            colors=colors_list,
            horizontal=horizontal,
            animation=cast(ANIMATION_TYPE, animation),
            quality=quality,
            fps=fps,
            border=cast(BOX_STYLES, border),
            border_color=border_color,
            dev_mode=dev,
        )
    except ColorParseError as e:
        raise click.UsageError(f"{e}")
    except Exception as e:
        console_stderr.print(f"Unexpected error: {e}")
        if dev:
            raise
        else:
            ctx.exit(1)

    console = Console()
    console.print(rich_figlet)


@cli.command()
def fonts() -> None:
    """List available fonts"""
    for font in get_args(ALL_FONTS):
        click.echo(f"{font}")


@cli.command()
def borders() -> None:
    """List available borders"""
    for border in get_args(BOX_STYLES):
        click.echo(f"{border}")


SECTIONS = [
    "fonts",
    "gradients",
    "multicolor",
    "borders",
    "animations",
    "practical",
    "credits",
]
start_at_help = (
    "Name of the section to start at. OPTIONS: [fonts, gradients, multicolor, "
    "borders, animations, practical, credits]"
)


@cli.command()
@click.argument("section", type=str, default=None, required=False, help=start_at_help)
def demo(section: str | None) -> None:
    """Run the demo. Optionally start at a specific section."""

    if section and section.lower() not in SECTIONS:
        raise click.UsageError(f"Section {section} not found. Choose from: {SECTIONS}")

    import rich_pyfiglet.demo

    rich_pyfiglet.demo.run(section)


if __name__ == "__main__":
    cli()
