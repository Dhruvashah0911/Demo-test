# from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework.authtoken.models import Token
# from rest_framework.response import Response
# from api.models import user1
# from api.serializers.UserSerializers import UserSerializer


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = user1.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [IsAuthenticated]


# class UserLogIn(ObtainAuthToken):

#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data,
#                                            context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token = Token.objects.get(user=user)
#         return Response({
#             'token': token.key,
#             'id': user.pk,
#             'username': user.username
#         })


# myapp/views.py
# from django.contrib.auth import authenticate
# from django.contrib.auth.models import User
# from django.http import JsonResponse
# from rest_framework.authtoken.models import Token
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import AllowAny

# @api_view(['POST'])
# @permission_classes([AllowAny])
# def obtain_token(request):
#     email = request.data.get('email')
#     password = request.data.get('password')

#     user = authenticate(request, username=email, password=password)

#     if user is not None and user.is_active:
#         token, created = Token.objects.get_or_create(user=user)
#         return JsonResponse({'token': token.key})
#     else:
#         return JsonResponse({'error': 'Invalid credentials'}, status=401)
