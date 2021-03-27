from logging import getLogger
from logging import StreamHandler
from sys import stdout

from uvicorn.logging import ColourizedFormatter

from rucula.core.config import settings


def get_logger():
    """ """
    logger = getLogger("rucula")
    logger.setLevel(settings.LOG_LEVEL)
    log_handler = StreamHandler(stdout)
    format = "%(levelprefix)s %(message)s (%(asctime)s) (%(module)s.py:%(lineno)d)"
    formatter = ColourizedFormatter(fmt=format)
    log_handler.setFormatter(formatter)
    logger.addHandler(log_handler)
    return logger


logger = get_logger()
