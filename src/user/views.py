from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import parsers
from .serializers import UserRegistrationSerializer, UserLoginSerializer

User = get_user_model()


class UserRegistrationView(APIView):

    @swagger_auto_schema(
        request_body=UserRegistrationSerializer
    )
    def post(self, request):
        """
        Handle POST requests for user registration.

        This method handles incoming POST requests containing user registration data.
        It validates the registration data using the UserRegistrationSerializer.
        If the data is valid, a new user is created and an email verification link
        is sent to the user's email address.

        Returns:
            Response: The response indicating the status of the registration request.
        """
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser)

    @swagger_auto_schema(
        request_body=UserLoginSerializer
    )
    def post(self, request, *args, **kwargs):
        """
        This view handles user login requests.
        """
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogoutView(APIView):
    """
    This view handles user logout requests by removing their refresh tokens.
    """

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data.get("refresh_token")
            if not refresh_token:
                return Response({"detail": "Refresh token is required."}, status=status.HTTP_400_BAD_REQUEST)

            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"detail": "Logout failed. " + str(e)}, status=status.HTTP_400_BAD_REQUEST)