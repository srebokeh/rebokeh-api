from django.contrib.auth import get_user_model
from django.http import JsonResponse
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings
from utilities.constant import excluded_paths
import jwt

User = get_user_model()


class AuthenticationMiddleware:
    """
    Middleware class for handling authentication of incoming requests.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/uuuser/') and request.path not in excluded_paths:
            try:
                user = IsAuthenticated().authenticate(request)
                if user is None:
                    return JsonResponse({'Error': 'Authorization token missing'}, status=401)
                request.user = user
            except AuthenticationFailed as e:
                return JsonResponse({'Error': str(e)}, status=401)

        return self.get_response(request)


class IsAuthenticated(BaseAuthentication):
    def authenticate(self, request):
        """
        Authenticate the incoming request. Handling user permissions
        """

        token = request.headers.get('Authorization')

        if not token:
            return None  # Return None if no token is found

        try:
            decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token has expired')
        except jwt.InvalidTokenError:
            raise AuthenticationFailed('Invalid token')

        user_id = decoded_token.get('user_id')
        if user_id is None:
            raise AuthenticationFailed('No user id found in token')

        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise AuthenticationFailed('No user found for given token')

        return [user, None]