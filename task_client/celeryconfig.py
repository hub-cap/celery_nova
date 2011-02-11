from socket import gethostname

BROKER_HOST = "localhost"
BROKER_PORT = 5672
# BROKER_USER = "admin"
# BROKER_PASSWORD = "admin72"
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