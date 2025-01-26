from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status, views
from rest_framework.authtoken.models import Token
from auth_services.serializers import RegistrationSerializer, LoginSerializer


# Registration View
class RegistrationView(views.APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        print(request)
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'user_id': user.id,
                'phone_number': user.phone_number,
                'name': user.name,
                'email': user.email,
                'national_id_number': user.national_id_number,
                'token': token.key
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Login View
class LoginView(views.APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        print(request.data)
        print(serializer)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'user_id': user.id,
                'phone_number': user.phone_number,
                'name': user.name,
                'email': user.email,
                'national_id_number': user.national_id_number,
                'token': token.key
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
