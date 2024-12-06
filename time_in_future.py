import time
import logging
import threading
from datetime import datetime, timedelta

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s')

def time_in_future():
    current_datetime = datetime.now()
    logging.debug('current_datetime:{} type:{}'.format(current_datetime, type(current_datetime)))
    current_datetime += timedelta(seconds=1)
    logging.debug('current_datetime:{} type:{}'.format(current_datetime, type(current_datetime)))

    time_string = '14:55:49'
    current_datetime = datetime.strptime(time_string, '%H:%M:%S')
    logging.debug('current_datetime:{} type:{}'.format(current_datetime, type(current_datetime)))
    current_datetime += timedelta(seconds=1)
    logging.debug('current_datetime:{} type:{}'.format(current_datetime, type(current_datetime)))

    time_string = '31.12.2024 23:59:59'
    current_datetime = datetime.strptime(time_string, '%d.%m.%Y %H:%M:%S')
    logging.debug('current_datetime:{} type:{}'.format(current_datetime, type(current_datetime)))
    current_datetime += timedelta(seconds=1)
    logging.debug('current_datetime:{} type:{}'.format(current_datetime, type(current_datetime)))

    time_string = '28.02.2024 23:59:59'
    current_datetime = datetime.strptime(time_string, '%d.%m.%Y %H:%M:%S')
    logging.debug('current_datetime:{} type:{}'.format(current_datetime, type(current_datetime)))
    current_datetime += timedelta(seconds=1)
    logging.debug('current_datetime:{} type:{}'.format(current_datetime, type(current_datetime)))

    time_string = '28.02.2023 23:59:59'
    current_datetime = datetime.strptime(time_string, '%d.%m.%Y %H:%M:%S')
    logging.debug('current_datetime:{} type:{}'.format(current_datetime, type(current_datetime)))
    current_datetime += timedelta(seconds=1)
    logging.debug('current_datetime:{} type:{}'.format(current_datetime, type(current_datetime)))

if __name__ == '__main__':
    time_in_future()
