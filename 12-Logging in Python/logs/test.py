from logger import logging

def add(a,b):
    logging.debug("The addition operation is talking place ")
    return a + b

logging.debug("The additipm function is call")

add(10,15)

