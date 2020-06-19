import jwt
from signup.models import Users
def auth(func):
    def wrapper(self, request, **kwargs):
        auth_token = request.headers.get('Authorization')
        payload = jwt.decode(auth_token, 'secret')
        user = Users.objects.get(id=payload["id"])
        request.user=user
        return func(self, request, **kwargs)
    return wrapper
