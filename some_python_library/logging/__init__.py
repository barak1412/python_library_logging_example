import logging

# initialize empty handler for library-level logger
logger = logging.getLogger(__name__.split('.')[0])
logger.setLevel(logging.INFO)
logger.addHandler(logging.NullHandler())


# rest of imports
from some_python_library.logging.functions import setup_logging
