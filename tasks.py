from celery.task import task
from celery.task.sets import subtask
import time


@task
def add_user(username, password, callback=None):
    print "add_user(%s, %s)" % (username, password)
    result = True
    callback_immediate(callback, result)
    time.sleep(2)
    return result

@task
def do_on_all_machines(somearg, callback=None):
    print "do_on_all_machines(%s)" % somearg
    result = True
    callback_immediate(callback, result)
    time.sleep(2)
    return result

def callback_immediate(callback, result):
    if callback is not None:
        print "calling back immediately w/ %s" % result
        subtask(callback).apply(result)