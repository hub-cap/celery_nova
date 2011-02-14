from socket import gethostname

BROKER_HOST = "localhost"
BROKER_PORT = 5672
CELERY_RESULT_BACKEND = "amqp"
CELERY_DEFAULT_EXCHANGE = "guestagents.direct"
HOSTNAME = gethostname()

CELERY_IMPORTS = ("tasks", )

NODE = {
    "exchange_type": "direct",
}
CELERY_ROUTES = {
    "tasks.add_user": NODE,
}