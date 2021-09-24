from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from accounts.api.serializers import UserCreateSerializer


# login view
class LoginAPIView(APIView):
    permission_classes = []

    def post(self, request):
        username = request.data["username"]
        password = request.data["password"]

        # user authentication
        user = authenticate(username=username, password=password)

        if user is not None:
            # if user is active
            if user.is_active:
                # user login
                login(request, user)
                # get existing token if exist
                token = Token.objects.filter(user=user).first()
                # if token doesn't exists, create new token
                if token is None:
                    token = Token.objects.create(user=user)

                return Response({"success":True,"message":"Successfully logged in","data":{"token": token.key}}, status=status.HTTP_200_OK)
            else:
                return Response({"success":False,"message":"User is not active. Contact administrator!","data":{}}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"success":False,"message":"Username and Password Doesn't match!","data":{}}, status=status.HTTP_400_BAD_REQUEST)


# logout view
class LogoutAPIView(APIView):

    def post(self, request):
        token = (request.headers["Authorization"])[6:]
        # delete active token
        Token.objects.get(key=token).delete()
        # flush the current session
        request.session.flush()

        return Response({"success":True, "message": "Logout successful!","data":{}}, status=status.HTTP_200_OK)


# register view
class RegisterAPIView(APIView):
    permission_classes = []

    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            instance = serializer.save()
            return Response({"success":True,"message":"Registered Successfully!","data":{}}, status=status.HTTP_200_OK)
        return Response({"success":False,"message":"Error while registering!","data":{}}, status=status.HTTP_400_BAD_REQUEST)
        