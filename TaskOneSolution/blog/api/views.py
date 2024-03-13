from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import *
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, smart_str
from django.template.loader import render_to_string
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from blog.models import PasswordResetToken,User  
import uuid
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication








############################# Login ##########################

@permission_classes([AllowAny])
@api_view(['POST'])
def user_login(request):
    username = request.data['username']
    password = request.data['password']
    user = authenticate(username=username, password=password)
    if user :
        if user.is_email_verified :
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key, "Message": "welcome to Blog page"}, status=200)
        return Response({'error': 'Email is not activated', "email": user.email}, 401)
    return Response({'error': 'Invalid credentials'}, 401)


####################################---------  logout  -------------###################################
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def user_logout(request):

    request.auth.delete()
    return Response('User Logged out successfully',200) 



############################ Update, Retrieve & Destroy ########################
class RetrieveUpdateDestroyMyUser(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAdminUser,IsAuthenticated)
    authentication_classes=(TokenAuthentication,)
    queryset= User.objects.all()
    serializer_class=UserSerializer


################################### Register User #######################################333
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()

        activation_token = generate_activation_token(user)
        current_site = get_current_site(request)

        PasswordResetToken.objects.create(user=user, token=activation_token)

        send_activation_email(user, activation_token, current_site)

        return Response({"status": "success", "message": "User registered successfully. Check your email for activation."}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


################################------------- Activate Email --------------------################################

def generate_activation_token(user):
    token = str(uuid.uuid4())
    return token

#Send Activation Email
def send_activation_email(user, activation_token, current_site):
    subject = 'Activate Your Account'
    message = render_to_string('blog/activation_email.html', {
        'user': user,
        'protocol': 'http',  
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': activation_token,
    })
    user.email_user(subject, message)

#
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
@csrf_exempt
def activate_user(request, uidb64, token):
    try:
        uid = smart_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        password_reset_token = PasswordResetToken.objects.get(user=user, token=token)
        
        expiration_time = 24 * 60 * 60  # 24 hours in seconds

        if not user.is_email_verified and (timezone.now() - password_reset_token.created_at).total_seconds() < expiration_time:
            user.is_email_verified = True
            user.save()
            password_reset_token.delete()
            return Response({'message': 'Account activated successfully.'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid activation link.'}, status=status.HTTP_400_BAD_REQUEST)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist, PasswordResetToken.DoesNotExist):
        return Response({'message': 'Invalid activation link.'}, status=status.HTTP_400_BAD_REQUEST)