import datetime
import time
import random

from pytz import timezone, utc
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.date import DateTrigger

import logging
logging.basicConfig()

TIME_ZONE = utc


class Clock(object):
    
    def __str__(self):
        return "O'clock: {0} | P'clock: {1}".format(datetime.datetime.now() , self.get_time())

    def __init__(self):
        self.delta = 0
        self.sch = BackgroundScheduler(timezone=utc)
        self.sch.start()
        self.sch.add_job(self.new_minute, 'date')

    def get_time(self):
        return datetime.datetime.now() + datetime.timedelta(0, self.delta)
    

    def new_minute(self):
        self.printc()
        last = random.randint(-20, 20)
        print "New minute elapsed. Next minute will last {0} seconds.".format(60 + last)
        self.delta += last
        self.sch.add_job(self.new_minute, 'date', run_date=datetime.datetime.now() + datetime.timedelta(seconds= 60 + last))

    def printc(self):
        print self.__str__()
