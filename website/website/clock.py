import datetime
import time
import random
import json

from ws4redis.publisher import RedisPublisher
from ws4redis.redis_store import RedisMessage

from pytz import timezone, utc
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.date import DateTrigger

import logging
logging.basicConfig()

TIME_ZONE = utc


class Clock(object):
    
    def __str__(self):
        return "O'clock: {0} | P'clock: {1}".format(self.oclock() , self.pclock())

    def __init__(self):
        self.delta = 0
        self.laps = {"hour": 24, "minute": 60, "second": 60}
        self.sch = BackgroundScheduler(timezone=utc)
        self.sch.start()
        now = datetime.datetime.now()
        then = now + datetime.timedelta(seconds=(70 - now.second))
        self.sch.add_job(self.new_minute, 'date', run_date=then)
        self.redis_publisher = RedisPublisher(facility="pclock", broadcast=True)

    def pclock(self):
        return datetime.datetime.now() + datetime.timedelta(seconds=self.delta)

    def oclock(self):
        return datetime.datetime.now()
    
    def new_minute(self):
        print "WOW"
        self.printc()
        last = random.randint(-20, 20)
        self.laps["second"] = 60 + last
        print "New minute elapsed. Next minute will last {0} seconds.".format(self.laps["second"])
        msg = RedisMessage(json.dumps({"type": "second", "laps": self.laps["second"]}))
        self.redis_publisher.publish_message(msg)
        self.delta += last
        self.sch.add_job(self.new_minute, 'date', run_date=datetime.datetime.now() + datetime.timedelta(seconds=self.laps["second"] + 10))


    def printc(self):
        print self.__str__()
