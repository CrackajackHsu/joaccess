import logging
from slavehandler import SlaveHandler

class dht11(SlaveHandler):
    def __init__(self):
        SlaveHandler.__init__(self)
        
    def do_mount(self):
        logging.debug('do_mount')

    def do_remount(self):
        logging.debug('do_remount')

    def do_unmount(self):
        logging.debug('do_unmount')