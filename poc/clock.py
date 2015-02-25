import datetime
import time
import random
import sched


class Clock(object):
    
    def __init__(self):
        self.delta = 0
        self.sch = sched.scheduler(time.time, time.sleep)

    def get_time(self):
        return datetime.datetime.now() + datetime.timedelta(0, self.delta)
    

    def new_minute(self):
        self.printc()
        last = random.randint(-20, 20)
        print "New minute elapsed. Next minute will last {0} seconds.".format(60 + last)
        self.delta += last
        self.sch.enter(60 + last, 1, self.new_minute, ())
        self.sch.run()

    def printc(self):
        print "O'clock: {0} | P'clock: {1}".format(datetime.datetime.now() , self.get_time())
