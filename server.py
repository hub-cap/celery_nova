from tasks import add_user

# Case where its sent to a single task node
add_user.apply_async(args=["user", "pass"], routing_key="guestagents.host1").get()
add_user.apply_async(args=["user", "pass"], routing_key="guestagents.host1").get()
print "sent add_user 2x times to the same host\n\n"