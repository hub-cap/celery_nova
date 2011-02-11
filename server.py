from tasks import add_user, do_on_all_machines

# getting around the weird bug i found w/ celery Q based on my configs (grrrrr).
do_on_all_machines.apply_async(args=["foo"], queue="celery")

# Base case, sending to all tasks
do_on_all_machines.apply_async(args=["FOO"])
print "sent do_on_all_machines\n\n"

# Case where its sent to a single task node
add_user.apply_async(args=["user", "pass"], queue="guestagents.host1")
print "sent add_user\n\n"