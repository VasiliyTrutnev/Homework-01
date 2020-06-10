import logging


def My_log():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)


    f_handler = logging.FileHandler('chat_log.txt')
    f_handler.setLevel(logging.INFO)

    f_format = logging.Formatter("%(asctime)s %(levelname)-10s %(module)s %(funcName)s %(message)s")
    f_handler.setFormatter(f_format)

    logger.addHandler(f_handler)

    logger.info('Debug info --> ', exc_info=True)


if __name__ == '__main__':
    My_log()







