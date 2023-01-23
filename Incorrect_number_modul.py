import logging

class Incorrect_number(Exception):
    def __init__(self, msg, correct):
        self.msg = msg
        self.correct = correct

    def __str__(self):
        return f'{self.msg}, {self.correct}'

logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)-27s %(levelname)-8s %(message)s ')

filehandler = logging.FileHandler('logger.log')
console_handler = logging.StreamHandler()
filehandler.setLevel(logging.INFO)
filehandler.setFormatter(formatter)
logger.addHandler(filehandler)
logger.addHandler(console_handler)