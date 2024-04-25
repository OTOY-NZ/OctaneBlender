# <pep8 compliant>

import logging
import sys
from octane import core


def setup_logger(name, log_file, level=logging.INFO):
    """Set up a logger with specified settings."""
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Create a file handler that logs to a specified file
    # handler = logging.FileHandler(log_file, mode='w')
    # handler.setFormatter(formatter)

    # Create and configure the logger
    logger = logging.getLogger(name)
    logger.setLevel(level)
    # logger.addHandler(handler)

    return logger


def add_console_handler(logger, level=logging.INFO):
    """Add a console handler to the logger."""
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)
    console_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(console_handler)
    logger.propagate = False


def exception_to_string(exception_object, message=None):
    if message is None:
        message = "An error occurred: %s" % str(exception_object)
    return message


# Logger functions
def debug(message):
    global __logger
    __logger.debug(message)


def info(message):
    global __logger
    __logger.info(message)


def warning(message):
    global __logger
    __logger.warning(message)


def error(message):
    global __logger
    __logger.error(message)


def critical(message):
    global __logger
    __logger.critical(message)


def exception(exception_object, message=None, exc_info=True):
    global __logger
    message = exception_to_string(exception_object, message)
    __logger.error(message, exc_info=exc_info)


# Logger and report functions
def debug_and_report(message, report):
    debug(message)
    report({'DEBUG'}, message)


def info_and_report(message, report):
    info(message)
    report({'INFO'}, message)


def warning_and_report(message, report):
    warning(message)
    report({'WARNING'}, message)


def error_and_report(message, report):
    error(message)
    report({'ERROR'}, message)


def critical_and_report(message, report):
    critical(message)
    report({'CRITICAL'}, message)


def exception_and_report(exception_object, report, message=None, exc_info=True):
    message = exception_to_string(exception_object, message)
    exception(exception_object, message, exc_info)
    report({'ERROR'}, message)


# Set up a logger
__logger_level = logging.DEBUG if core.DEBUG_MODE else logging.INFO
__logger = setup_logger("Octane", "octane_blender_addon.log", __logger_level)
add_console_handler(__logger, __logger_level)
