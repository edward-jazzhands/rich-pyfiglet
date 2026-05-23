from typing import get_args, cast
import time
import sys
import random
from rich.console import Console
from rich_pyfiglet import RichFiglet
from rich_pyfiglet.fonts_list import ALL_FONTS


def run() -> None:
    console = Console()

    # random_font = cast(ALL_FONTS, random.choice(get_args(ALL_FONTS)))

    rich_fig = RichFiglet(
        "Rich - PyFiglet",
        font="ansi_regular",
        # width=100, # default = auto-detect terminal width
        colors=["yellow", "magenta1"],
        border="ROUNDED",
        border_color="magenta1",
        justify="center",
        animation="gradient_down",
        timer=5.0,
        # horizontal=True,
        # quality=15,
        # fps=5,
        # dev_mode=True,
    )

    # NOTE: When there's an animation set, the script will hold on that animation
    # and not print anything else passed that line. Unfortunately you cannot make it
    # continue to animate while the script goes passed that point. But you can set
    # a timer so the animation stops on its own after a certain number of seconds.
    # It also shows a message that says "Press ctrl+c to continue" to stop early.
    # Pressing ctrl+c will only stop the animation, not the script.

    console.print(rich_fig)
    for i in range(5):
        console.print(f"Doing some work {i+1}...")
        time.sleep(1)


if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print(e)
        sys.exit(1)