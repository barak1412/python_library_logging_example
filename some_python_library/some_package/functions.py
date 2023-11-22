from some_python_library.logging import logger


def very_important_function(a, b):
    logger.info(f'Got a = {a}, b = {b}.', extra={'step': 'very_important_function'})
    return a+b


def function_you_shouldnt_use(c):
    logger.warn('why do you use this useless function?')
    return c


def bad_function():
    logger.error('you just applied bad function.')


def very_bad_function():
    logger.critical('you just applied very bad function.')