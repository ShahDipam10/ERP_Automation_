import logging
import os

class LogGen:
    """Logger utility class to generate and configure logging for automation tests."""

    @staticmethod
    def loggen():
        """Creates and configures a logger instance."""
        log_dir = ".\\logs"  # Directory where log files are stored
        log_file = os.path.join(log_dir, "automation.log")  # Log file path

        # Ensure Logs directory exists
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)  # Create logs directory if it doesn't exist

        logger = logging.getLogger()  # Get logger instance

        # Clear existing handlers to avoid duplicate logs
        if logger.hasHandlers():
            logger.handlers.clear()

        # Configure logging format, level, and output file
        logging.basicConfig(
            filename=log_file,
            format='%(asctime)s: %(levelname)s: %(message)s',  # Log format
            datefmt='%m/%d/%Y %I:%M:%S %p',  # Date format
            level=logging.INFO,  # Log level set to INFO
            force=True  # Ensure new configuration applies
        )

        return logger  # Return configured logger instance
