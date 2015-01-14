from django.contrib.auth.middleware import RemoteUserMiddleware

class HttpUserHeaderAuthMiddleware(RemoteUserMiddleware):
    header = 'HTTP_USER'
