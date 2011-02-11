from socket import gethostname

BROKER_HOST = "localhost"
BROKER_PORT = 5672
CELERY_RESULT_BACKEND = "amqp"
CELERY_DEFAULT_EXCHANGE_TYPE = "fanout"
CELERY_DEFAULT_EXCHANGE = "guestagents"
HOSTNAME = gethostname()

CELERY_IMPORTS = ("tasks", )
CELERY_QUEUES = { 
    "guestagents.%s" % HOSTNAME : {
        "binding_key": "guestagents.%s" % HOSTNAME,
    },
}

BROADCAST = {
    "exchange": "guestagents",
    "exchange_type": "fanout",
}
NODE = {
    "exchange_type": "direct",
    "exchange": "guestagents.node",
}
CELERY_ROUTES = {
    "tasks.do_on_all_machines": BROADCAST,
    "tasks.add_user": NODE,
}