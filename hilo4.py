import threading
import time
import logging

#https://github.com/estebancode/Proyectos-Python


def daemon():
    logging.debug('Starting')
    time.sleep(2)
    logging.debug('Exiting')

def non_daemon():
    logging.debug('Starting')
    logging.debug('Exiting')

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(threadName)s %(message)s',
	#format='(%(threadName)-10s) %(message)s',
	#datefmt='%Y-%m-%d %H:%M:%S',
	filename='myapp.log',
	filemode='w'
)

d = threading.Thread(name='daemon', target=daemon, daemon=True)

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()
d.join()
t.join()
