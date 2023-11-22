import logging


class StreamColoredFormatter(logging.Formatter):

    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    default_format = "%(asctime)s - [%(levelname)s] - %(message)s"
    error_format = "%(asctime)s - [%(levelname)s] - %(message)s (%(filename)s:%(lineno)d)"

    FORMATS = {
        logging.DEBUG: grey + default_format + reset,
        logging.INFO: grey + default_format + reset,
        logging.WARNING: yellow + default_format + reset,
        logging.ERROR: red + error_format + reset,
        logging.CRITICAL: bold_red + error_format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)