from celery.task import task

@task
def add_user(username, password):
    print "add_user(%s, %s)" % (username, password)
    return True

@task
def do_on_all_machines(somearg):
    print "do_on_all_machines(%s)" % somearg
    return True
