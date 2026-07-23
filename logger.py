import logging


class LogGen:

    @staticmethod
    def loggen():

        logger = logging.getLogger()

        file_handler = logging.FileHandler("automation.log")

        formatter = logging.Formatter(
            "%(asctime)s : %(levelname)s : %(name)s : %(message)s"
        )

        file_handler.setFormatter(formatter)

        if not logger.hasHandlers():
            logger.addHandler(file_handler)

        logger.setLevel(logging.INFO)

        return logger