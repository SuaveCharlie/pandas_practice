import logging


def get_logger(level=logging.INFO, **kwargs) -> None:
    """Creates a simple logger with a basic setting and standardised formatting"""
    _handlers = [logging.StreamHandler()]
    _date_format = "%Y-%m-%d %H:%M:%S"

    if level < logging.INFO:
        _format = "[%(asctime)s] /%(levelname)s - %(filename)s:%(module)s:%(lineno)d - %(message)s"

    else:
        _format = "[%(asctime)s] %(levelname)s - %(message)s"

    logging.basicConfig(
        level=level,
        format=kwargs.get("custom_format") or _format,
        datefmt=kwargs.get("custom_date_format") or _date_format,
        handlers=_handlers,
    )
    logging.info("Initialised logger")
