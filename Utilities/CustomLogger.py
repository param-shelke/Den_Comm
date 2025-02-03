# import logging
#
#
# class LogGen:
#     @staticmethod
#     def loggen():
#         logging.basicConfig(filename=r"C:\Users\Prem\Python\PycharmProjects\Den_Comm\Logs\automation.log",
#                             format="%(asctime)s : %(levelname)s: %(message)s",
#                             datefmt="%m/%d/%Y %I:%M:%S %p",
#                             level=logging.INFO)  # ✅ Set logging level directly
#
#         logger = logging.getLogger()  # ✅ Corrected way to create a logger
#         return logger
import inspect
import logging


class LogGen:

    @staticmethod
    def loggen():
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)
        logfile = logging.FileHandler(r'C:\Users\Prem\Python\PycharmProjects\Den_Comm\Logs\cred_kart.log')
        # s = "C:\Users\Prem\Python\PycharmProjects\Den_Comm\Logs"
        # Fix the typo in the formatter
        format = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(funcName)s - %(message)s")

        logfile.setFormatter(format)

        # Set the logging level before adding the handler
        logger.setLevel(logging.INFO)

        logger.addHandler(logfile)

        return logger
