import logging
import sys


def get_logger(log_file_path="training.log"):
    """
    Return a logger object to record information in a log file.

    Args:
        log_file_path (str, optional): The path of the log file, where logs will be saved.

    Example Usage:
    ```
    logger = get_logger('log.log')
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.error("This is an error message")
    logger.warning("This is a warning message")
    logger.critical("This is a critical message")
    ```
    """
    logger = logging.getLogger("logger001")
    logger.setLevel(logging.INFO)

    # Create and set a FileHandler (output to file)
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setLevel(logging.INFO)

    # Create and set a StreamHandler (output to console)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)

    # Create Formatter
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s", # log format
        datefmt="%Y-%m-%d %H:%M:%S" # time format
    )

    # bind the formatter to the handlers
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    #sys.stdout = StreamToLogger(logger, logging.INFO)
    #sys.stderr = StreamToLogger(logger, logging.ERROR)

    return logger


# TODO: tqdm progress bar will also be recorded. Waiting for a fix.
class StreamToLogger:
    """a class to redirect stdout and stderr to a logger"""
    def __init__(self, logger, log_level=logging.INFO):
        self.logger = logger
        self.log_level = log_level

    def write(self, message):
        if message.strip() and not message == '[]':
            # BUG: Jupyter notebook seems to have a bug: when editing a cell, the logger will output "[]" to the console, so we add a check to disable it.
            self.logger.log(self.log_level, message.strip())

    def flush(self):
        pass
