import logging
from some_python_library.logging import logger
from some_python_library.logging.formatters import StreamColoredFormatter
from some_python_library.logging.config import ELASTIC_HOST, ELASTIC_PORT, ELASTIC_PASSWORD, ELASTIC_USER \
    , ELASTIC_INDEX_NAME


def setup_logging():
    # add logging to stdout
    setup_stream_logging()


def setup_stream_logging():
    stdout_handler = logging.StreamHandler()
    stdout_handler.setLevel(logging.INFO)
    stdout_handler.setFormatter(StreamColoredFormatter())
    logger.addHandler(stdout_handler)


def setup_elastic_handler():
    # imported on demand to decrease amount of dependencies
    from cmreslogging.handlers import CMRESHandler

    handler = CMRESHandler(hosts=[{'host': ELASTIC_HOST, 'port': ELASTIC_PORT}],
                           auth_type=CMRESHandler.AuthType.BASIC_AUTH,
                           auth_details=(ELASTIC_USER, ELASTIC_PASSWORD),
                           es_index_name=ELASTIC_INDEX_NAME)
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)

