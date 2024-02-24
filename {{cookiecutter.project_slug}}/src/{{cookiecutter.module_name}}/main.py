import sys

from loguru import logger
from nicegui import color, icon, ui
from {{cookiecutter.module_name}}.utils import first_run, get_options, set_icon

if __name__ in {"__main__", "__mp_main__"}:
    # we need to first remove the default logger and then add a new one for the levels to work
    logger.remove()
    logger.add(sys.stderr, level="DEBUG")

    first_run()
    set_icon()

    options = get_options()

    ui.run(
        port=5000,
        title=options["app_title"],
        dark=True if options["theme_mode"] == "dark" else False,
        reload=True,
        native=True,
        # window_size=(430, 660),
        # on_air=True,
    )
