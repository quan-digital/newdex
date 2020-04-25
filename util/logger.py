# coding=utf-8

import logging

def setup_logger(name, level= logging.INFO):
    '''Set up a logger to print to terminal.
    Available levels: logging.(DEBUG|INFO|WARN|ERROR)'''
    logger = logging.getLogger(name)
    logger.setLevel(level)
    ch = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger