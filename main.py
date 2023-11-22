from some_python_library.some_package import very_important_function, function_you_shouldnt_use, bad_function \
    , very_bad_function
from some_python_library.logging import setup_logging


if __name__ == '__main__':
    setup_logging()
    x = very_important_function(8, 7)
    y = function_you_shouldnt_use(0)
    bad_function()
    very_bad_function()